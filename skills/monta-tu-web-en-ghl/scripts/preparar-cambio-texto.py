#!/usr/bin/env python3
"""Prepara un cambio de texto (errata, dato, frase) en un bloque de Código de GHL ya publicado.

Uso: python3 preparar-cambio-texto.py "texto actual exacto" "texto nuevo" [salida.js]

Crea una función para la herramienta de Playwright que ejecuta código sobre la página.
Con el editor de código del bloque abierto, hace la sustitución dentro del navegador,
sin que el código de la web pase por la conversación, y solo si se cumplen tres guardas:
  1. el texto actual aparece exactamente una vez;
  2. el texto nuevo no está ya en la página;
  3. la longitud final cambia exactamente lo esperado.
Si alguna falla, no toca nada y devuelve el motivo. Devuelve la huella SHA-256 de antes
y de después, para compararlas con la apuntada en ESTADO.md.
"""
import base64
import pathlib
import sys

PLANTILLA = """async (page) => {
  const VIEJO = "%s";
  const NUEVO = "%s";
  const fb = page.frames().find(f => f.name() === 'funnel-builder') || page.mainFrame();
  return await fb.evaluate(async ([v64, n64]) => {
    const dec = b => new TextDecoder('utf-8').decode(Uint8Array.from(atob(b), c => c.charCodeAt(0)));
    const huella = async t => [...new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(t)))]
      .map(x => x.toString(16).padStart(2, '0')).join('');
    const viejo = dec(v64), nuevo = dec(n64);
    const cms = document.querySelectorAll('.CodeMirror');
    if (!cms.length) return { ok: false, reason: 'no hay editor de código abierto' };
    const cm = cms[cms.length - 1].CodeMirror;
    const actual = cm.getValue();
    const veces = actual.split(viejo).length - 1;
    if (veces !== 1) return { ok: false, reason: 'el texto actual aparece ' + veces + ' veces (debe ser 1)' };
    if (nuevo && actual.includes(nuevo)) return { ok: false, reason: 'el texto nuevo ya está en la página' };
    const final = actual.replace(viejo, () => nuevo);
    if (final.length !== actual.length - viejo.length + nuevo.length) return { ok: false, reason: 'longitud inesperada' };
    cm.setValue(final);
    if (cm.save) cm.save();
    const ta = (cm.getTextArea && cm.getTextArea()) || document.querySelector('textarea.hl-custom-code-editor');
    if (ta) {
      Object.getOwnPropertyDescriptor(HTMLTextAreaElement.prototype, 'value').set.call(ta, final);
      ta.dispatchEvent(new Event('input', { bubbles: true }));
      ta.dispatchEvent(new Event('change', { bubbles: true }));
    }
    return { ok: true, sha_antes: await huella(actual), sha_despues: await huella(cm.getValue()),
             len_antes: actual.length, len_despues: cm.getValue().length };
  }, [VIEJO, NUEVO]);
}
"""


def b64(texto):
    return base64.b64encode(texto.encode("utf-8")).decode("ascii")


def main():
    if len(sys.argv) not in (3, 4):
        sys.exit('Uso: python3 preparar-cambio-texto.py "texto actual" "texto nuevo" [salida.js]')
    viejo, nuevo = sys.argv[1], sys.argv[2]
    if not viejo:
        sys.exit("El texto actual no puede estar vacío.")
    destino = pathlib.Path(sys.argv[3] if len(sys.argv) == 4 else "cambio-texto.inyectar.js")
    destino.write_text(PLANTILLA % (b64(viejo), b64(nuevo)), encoding="utf-8")
    print(f"Script: {destino.resolve()}")


if __name__ == "__main__":
    main()
