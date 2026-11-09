// Lee el código del bloque de Código de GHL que tienes abierto en el editor
// y devuelve su huella SHA-256, para compararla con la del último publicado.
// Uso: con el editor de código del bloque abierto, ejecutar con la herramienta
// de Playwright que corre código sobre la página (parámetro filename).
// Por defecto devuelve solo longitud y huella. Pon CON_CODIGO = true únicamente si
// la huella no coincide con la apuntada y necesitas el código en vivo como copia.
async (page) => {
  const CON_CODIGO = false;
  const fb = page.frames().find(f => f.name() === 'funnel-builder') || page.mainFrame();
  return await fb.evaluate(async (conCodigo) => {
    const cms = document.querySelectorAll('.CodeMirror');
    if (!cms.length) return { ok: false, reason: 'no hay editor de código abierto' };
    const v = cms[cms.length - 1].CodeMirror.getValue();
    const h = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(v));
    return { ok: true, len: v.length,
             sha: [...new Uint8Array(h)].map(x => x.toString(16).padStart(2, '0')).join(''),
             ...(conCodigo ? { codigo: v } : {}) };
  }, CON_CODIGO);
}
