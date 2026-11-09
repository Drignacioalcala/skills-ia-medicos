# Monta tu web en GHL

> Diseña tu web a medida con tu agente de IA, publícala en GoHighLevel con tu dominio y cámbiala después con solo pedirlo.

📄 **[Descarga esta guía en PDF](https://assets.cdn.filesafe.space/5jsS54V4yegM9CEB1eAv/media/4698ee8c-bd07-4056-9479-eceb68238239.pdf)**, maquetada para leerla o compartirla.

## Qué es

Una guía y una skill para tener una web hecha a medida (no una plantilla) alojada en **GoHighLevel** (GHL), la plataforma de marketing que muchos profesionales ya usan para formularios, citas, cursos y correos. La web la escribe tu agente de IA (Claude Code o Codex) en tu ordenador. Después la sube a GHL y, a partir de ese momento, la mantiene: tú le dices el cambio con tus palabras y él lo hace, lo revisa y lo publica.

La guía sirve para dos lectores:

- **Tú**: aquí tienes el proceso explicado paso a paso, sin necesidad de saber programar.
- **Tu agente**: el archivo [`SKILL.md`](SKILL.md) tiene las instrucciones técnicas, las comprobaciones y los errores que ya conocemos. Si se lo das, no tiene que descubrirlos solo.

## Para qué sirve

- Tener una web con aspecto profesional y propio, no el de una plantilla más.
- Que la web viva dentro de GHL, junto a tus formularios, calendarios y correos, con tu dominio (por ejemplo, `www.tuconsulta.es`).
- Corregir una errata, cambiar un horario o añadir una sección diciéndolo en una frase.
- Que todo lo que publiques (otras páginas, guías, presentaciones) lleve la misma imagen, gracias a una guía de estilo.

## Por qué es importante

Las plantillas de los creadores de webs se parecen todas entre sí, y modificarlas a mano obliga a pelearse con muchos menús. Si haces la web en HTML (el lenguaje con el que están escritas las páginas web), el diseño no tiene límites. El problema hasta ahora era que había que saber escribirlo y mantenerlo.

Con un agente ese problema desaparece, pero aparecen otros: GHL tiene trampas que no se ven a simple vista. Por ejemplo, estropea el código largo cuando se pega a mano, o una página puede parecer guardada sin estarlo. Esta guía recoge esas trampas para que ni tú ni tu agente caigáis en ellas.

## Cómo funciona, en una imagen

Funciona como una obra con su arquitecto. En tu ordenador está **el plano** (el HTML y las imágenes). GHL es **el solar con dirección postal** (el hosting, es decir, el servidor que muestra la web, y el dominio). Tu agente es **el arquitecto y el contratista a la vez**: dibuja el plano, lo construye en el solar y vuelve cada vez que quieres hacer una reforma.

```
Tu carpeta (en tu ordenador)          GoHighLevel (en internet)
├── guía de estilo                    ├── Medios: tus imágenes
├── imágenes                ───────►  └── Sitio web
└── web en HTML                            └── página con un bloque de «Código»
                                              donde vive tu HTML
```

## Lo que necesitas

- **Una cuenta de GHL** con permiso para crear sitios web en tu subcuenta. La subcuenta es el espacio de tu negocio dentro de GHL.
- **Claude Code o Codex**: cualquiera de los dos sirve y en esta guía los tratamos igual.
- **Google Chrome**, para que el agente pueda trabajar en GHL con tu sesión iniciada:
  - Claude Code: la extensión «Claude in Chrome». Se activa abriendo Claude Code con `claude --chrome` o escribiendo `/chrome` dentro.
  - Codex: según la versión y el país, puede ofrecer su propia extensión de Chrome. Tu agente lo comprueba.
  - En los dos agentes vale también **Playwright**, un programa que maneja una ventana de navegador aparte. Es el método más fiable para el paso de subir la web, y la skill explica cómo instalarlo. En esa ventana tendrás que iniciar sesión en GHL una vez. Si te da problemas el botón «Iniciar sesión con Google», entra con tu correo y tu contraseña de GHL.
- **Tu dominio**, si quieres usar uno propio. Se puede empezar sin él con la dirección que da GHL.
- Opcional, pero recomendable: **el conector oficial de GHL** (MCP), que permite al agente consultar tu cuenta sin pasar por el navegador. Lo explicamos en el paso 6.

## El proceso, paso a paso

### Paso 1 · Crea la carpeta del proyecto

Pídele a tu agente: «Vamos a montar mi web en GHL; crea la carpeta del proyecto». Creará una carpeta con este orden:

- `imagenes/`: mete aquí tus fotos, tu logo y lo que quieras que aparezca.
- `guia-de-estilo.md`: colores, tipos de letra, tono y normas de tu marca.
- `paginas/`: el HTML de cada página.
- `publicado/`: una copia de lo que hay en internet cada vez que se publica, para poder volver atrás.
- `ESTADO.md`: dónde está todo (dirección de la web, nombre de la página en GHL, fecha del último cambio).

Todo esto está en tu ordenador. Nada sale a internet hasta el paso 4.

### Paso 2 · Haz la guía de estilo (merece la pena)

Antes de diseñar, pídele que te ayude a definir tu guía de estilo: dos o tres colores, uno o dos tipos de letra, cómo hablas a tus pacientes o alumnos y qué no quieres nunca. Si ya tienes logotipo o una web que te guste, dáselos como referencia.

Es como el protocolo de un servicio: se escribe una vez y luego todo sale igual. Con ella, la segunda página de tu web, tu próxima guía en PDF o tu presentación tendrán el mismo aspecto sin tener que explicarlo otra vez.

### Paso 3 · Diseña la web en tu ordenador

Descríbele la web como se la describirías a un diseñador: para quién es, qué secciones quieres (presentación, servicios, quién eres, opiniones, contacto, pedir cita) y qué te gusta de otras webs. El agente escribe el HTML y te lo abre en el navegador.

Revisa y pide cambios todas las veces que haga falta: «el título más grande», «quita esta sección», «en el móvil se ve apretado». Aquí no hay prisa: los cambios son gratis y no los ve nadie.

> No hace falta usar «Sites» ni otro creador de webs de ChatGPT o de otra herramienta: el agente trabaja directamente sobre tu carpeta.

### Paso 4 · Súbela a GHL

Cuando la web te guste, pídele: «Súbela a GHL como una página nueva del sitio web X, con la dirección /inicio».

1. **Inicias tú la sesión en GHL** en el navegador que use el agente. El agente nunca necesita tu contraseña.
2. El agente **sube las imágenes** a la sección «Medios» de GHL. Cada imagen recibe una dirección de internet, y el agente cambia en el HTML la ruta de tu ordenador por esa dirección. Por eso no basta con copiar el HTML: un HTML no lleva las imágenes dentro, solo dice dónde encontrarlas.
3. **Crea la página** en tu sitio web de GHL y le añade un bloque de tipo «Código» (Custom HTML), que es donde vive tu web.
4. **Mete el HTML en ese bloque por el método seguro**: no lo copia y pega, porque GHL estropea el código largo cuando se pega a mano.
5. **Guarda, comprueba que lo guardado está completo y, con tu «sí», publica**. Después abre la dirección pública y comprueba que se ve lo nuevo.

Si quieres hacerlo tú a mano, puedes: Sitios → Sitios web → tu web → Añadir página → añade el elemento «Código» → abre el editor de código → pega → Guardar → Guardar página → Publicar. Es razonable si la web es corta. Si es larga, revisa después que no falte ningún trozo.

### Paso 5 · Revisa en móvil y en ordenador, y conecta tu dominio

Pídele capturas de la página publicada a dos anchos, móvil y ordenador. Mira que no haya texto cortado, columnas aplastadas ni imágenes que no carguen.

El dominio propio se conecta una sola vez, en los ajustes de GHL («Dominios»), añadiendo en tu proveedor de dominio los registros que te indique GHL. El agente puede guiarte, pero los cambios en tu proveedor de dominio los haces tú.

Antes de anunciarla, comprueba también lo legal: aviso legal, política de privacidad y de cookies y, si es la web de una consulta, la normativa de publicidad sanitaria de tu comunidad autónoma. Si la web tiene un formulario, que pida lo mínimo (nombre, contacto, preferencia de cita) y lleve una casilla de consentimiento sin marcar. El motivo de consulta o los síntomas son datos de salud: mejor no pedirlos por la web.

### Paso 6 (opcional) · Conecta el MCP oficial de GHL

Un **MCP** es un conector que da a tu agente acceso directo a una herramienta, sin pasar por el navegador. GHL tiene uno oficial y ya no hace falta crear ni copiar claves: lo autorizas iniciando sesión, igual que cuando entras con Google en otra aplicación.

No tienes que escribir nada técnico. Basta con pedírselo a tu agente: «conecta el MCP oficial de GHL». Él ejecuta la orden, se abre una ventana de GHL, eliges tu subcuenta y aceptas. Si quieres hacerlo tú, estas son las órdenes:

- Claude Code: `claude mcp add --transport http leadconnector https://services.leadconnectorhq.com/mcp/anthropic/v2`
- Codex: `codex mcp add leadconnector --url https://services.leadconnectorhq.com/mcp/openai/v2/codex` y después `codex mcp login leadconnector`

Las direcciones pueden cambiar. Si alguna falla, el agente consulta la página oficial de GHL sobre su servidor MCP.

**Qué hace y qué no:** con él, el agente puede ver tus sitios y páginas, tus medios, formularios, redirecciones, contactos y mucho más. **No puede cambiar el HTML de una página**: eso sigue haciéndose por el navegador. Por eso decimos que tiene funciones parciales. Al autorizarlo, concede solo los permisos que vayas a usar y **ninguno de borrado**.

## Después: cómo se gestiona la web

Este es el día a día. Abres tu agente y le dices el cambio:

> «En la web, cambia el horario de los martes a 16:00-20:00.»
> «Hay una errata en "otorrinolaringólogo" en la sección de servicios.»
> «Añade una sección de preguntas frecuentes con estas cinco preguntas.»

El agente comprueba que tiene copia de lo publicado, hace **solo ese cambio** sobre la versión en vivo (no rehace la página entera), te enseña el antes y el después y, cuando le dices que sí, publica y comprueba que el cambio se ve en internet.

### ¿Y si quiero corregir una errata yo mismo, sin el agente?

Es la duda más frecuente. Tienes tres opciones:

1. **Pedírselo al agente en una frase** (recomendado). Es lo más rápido y él comprueba que no se ha roto nada.
2. **Cambiarlo tú en el editor de código de GHL**: abre la página, haz clic en el bloque de código, «Abrir editor de código», busca la palabra (Ctrl+F o Cmd+F), corrígela, Guardar → Guardar página → Publicar. Para un cambio de una palabra funciona bien. Lo que da problemas es pegar bloques grandes. Cuando lo hagas, avisa a tu agente la próxima vez («he corregido una errata a mano»), para que trabaje sobre la versión publicada y no sobre su copia antigua.
3. **Dejar en bloques normales de GHL los textos que cambian a menudo** (novedades, horarios, avisos). Una página de GHL puede mezclar tu bloque de código con bloques de texto normales, que se editan escribiendo encima, como en un procesador de textos. Lo diseñado va en el código; lo que cambia cada semana, en bloques de texto. Pídele al agente que prepare la página así desde el principio.

## Límites y garantías

- **Tú inicias la sesión** en GHL. El agente no pide, no escribe y no guarda tu contraseña.
- **No se borra nada** en GHL: ni páginas, ni webs, ni imágenes. Si hay que borrar, lo haces tú.
- **No publica nada sin tu «sí»**, después de enseñarte el resultado. Antes de cada cambio se asegura de tener copia de lo que hay publicado.
- **Sin claves dentro de archivos**: el conector oficial se autoriza iniciando sesión. Si alguna vez usas una clave de GHL, va en un archivo aparte, nunca en la carpeta de la web ni en nada que compartas.
- **Ningún dato de pacientes** en la web ni en la carpeta del proyecto.
- Los nombres de los menús de GHL cambian con las actualizaciones y con el idioma. Si un botón no está donde dice la guía, el agente lo busca en pantalla y te lo dice.

## Cómo se usa

Una vez instalada la skill, abre una conversación nueva con tu agente y pídelo con tus palabras:

- «Quiero montar mi web en GHL.»
- «Sube esta web a GoHighLevel.»
- «Cambia el texto de la portada de mi web.»

---

Instalación: ver la [portada del repositorio](../../README.md#cómo-se-instala-una-skill). Las instrucciones que sigue el agente están en [`SKILL.md`](SKILL.md).
