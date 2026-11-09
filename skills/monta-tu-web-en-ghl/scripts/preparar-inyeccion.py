#!/usr/bin/env python3
"""Prepara un fragmento HTML para inyectarlo en un bloque de Código de GHL.

Uso: python3 preparar-inyeccion.py ruta/al/fragmento.html

Crea, junto al fragmento, un archivo <nombre>.inyectar.js: una función para la
herramienta de Playwright que ejecuta código sobre la página. Con el editor de
código del bloque ya abierto, escribe el HTML directamente en el editor
(CodeMirror) del constructor de páginas, sin pegar, y devuelve la huella
SHA-256 de lo que ha quedado escrito para compararla con la del archivo.
"""
import base64
import hashlib
import pathlib
import re
import sys

PLANTILLA = """async (page) => {
  const B64 = "%s";
  const fb = page.frames().find(f => f.name() === 'funnel-builder') || page.mainFrame();
  return await fb.evaluate(async (b64) => {
    const html = new TextDecoder('utf-8').decode(Uint8Array.from(atob(b64), c => c.charCodeAt(0)));
    const cms = document.querySelectorAll('.CodeMirror');
    if (!cms.length) return { ok: false, reason: 'no hay editor de código abierto' };
    const cm = cms[cms.length - 1].CodeMirror;
    const antes = cm.getValue().length;
    cm.setValue(html);
    if (cm.save) cm.save();
    const ta = (cm.getTextArea && cm.getTextArea()) || document.querySelector('textarea.hl-custom-code-editor');
    if (ta) {
      Object.getOwnPropertyDescriptor(HTMLTextAreaElement.prototype, 'value').set.call(ta, html);
      ta.dispatchEvent(new Event('input', { bubbles: true }));
      ta.dispatchEvent(new Event('change', { bubbles: true }));
    }
    const v = cm.getValue();
    const h = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(v));
    return { ok: true, antes, len: v.length,
             sha: [...new Uint8Array(h)].map(x => x.toString(16).padStart(2, '0')).join('') };
  }, B64);
}
"""


def main():
    if len(sys.argv) != 2:
        sys.exit("Uso: python3 preparar-inyeccion.py ruta/al/fragmento.html")
    origen = pathlib.Path(sys.argv[1])
    texto = origen.read_text(encoding="utf-8")
    # CodeMirror trabaja con saltos de línea \n: normalizar para que la huella coincida.
    texto = texto.replace("\r\n", "\n")
    if re.search(r"<(head|body|html)[\s>]|<!doctype", texto, re.I):
        print("Aviso: el fragmento contiene <!DOCTYPE>, <html>, <head> o <body>. "
              "Dentro de GHL debe ir sin ellos.")
    datos = texto.encode("utf-8")
    destino = origen.with_suffix(".inyectar.js")
    destino.write_text(PLANTILLA % base64.b64encode(datos).decode("ascii"), encoding="utf-8")
    print(f"Script: {destino}")
    print(f"Caracteres: {len(texto)}")
    print(f"Huella SHA-256: {hashlib.sha256(datos).hexdigest()}")


if __name__ == "__main__":
    main()
