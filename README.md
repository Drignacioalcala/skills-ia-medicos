# Skills de IA para médicos

Biblioteca de *skills* para profesionales sanitarios que trabajan con un agente de IA (Claude Code o Codex): un asistente que, además de conversar, lee y escribe archivos y ejecuta programas en tu ordenador. Nace de una propuesta de la comunidad de [red sanitarIA](https://redsanitaria.es).

## Qué es esto

Una **skill** es un archivo de texto con instrucciones para que el agente haga una tarea concreta siempre de la misma manera. Se parece a un protocolo del servicio: no hay que explicarlo cada vez, basta con pedirlo.

Este repositorio (la carpeta pública donde están publicadas) reúne doce. Dos se usan tal cual (`verifica-citas` y `lee-tu-whatsapp`). Las otras diez son **configurables**: no traen el estilo ni los datos de otra persona, sino que te hacen unas preguntas, miran tu propio material y te dejan montada **tu** versión.

## Para qué sirve

Para las tareas que un médico repite al trabajar con una IA y que conviene hacer siempre bien: comprobar una bibliografía, escribir con voz propia, tener los proyectos ordenados, seguir lo que se publica de su tema, preparar documentos y material docente, y tener tu web al día.

## Por qué es importante

Usar una IA sin método da resultados distintos cada día y deja pasar errores que en medicina cuentan: una cita que no existe, un dato de un paciente donde no debe, un texto que no suena a ti, un aviso enviado a todo un curso. Estas skills fijan el método y ponen los controles dentro del proceso. Todas se han probado (con casos ficticios o en uso real) y se han corregido con los fallos que aparecieron; sus límites están escritos.

## Las skills

Cada una tiene su propia página con qué es, para qué sirve, por qué importa y sus límites.

| Skill | Para qué sirve | Qué te deja |
|---|---|---|
| [verifica-citas](skills/verifica-citas/) | Comprobar que las referencias de un texto existen, que título, primer autor, año, revista y DOI coinciden, y que no están retractadas | Un informe con cada cita verificada, dudosa, no localizada o retractada. Se usa tal cual |
| [ordena-tu-espacio-de-trabajo](skills/ordena-tu-espacio-de-trabajo/) | Tener las carpetas en orden para que el agente encuentre cada proyecto y sepa en qué estado está | Tu estructura de carpetas, un archivo de estado por proyecto, un catálogo y una carpeta para lo que instales |
| [crea-tu-estilo](skills/crea-tu-estilo/) | Que el agente redacte correos y mensajes con tu voz | Tu skill de estilo, sacada de tus correos o de 15-20 textos tuyos |
| [monta-tu-manual-de-estilo](skills/monta-tu-manual-de-estilo/) | Que lo que publicas (redes, boletín, vídeo) tenga voz propia y no suene a IA | Tu manual: estructuras por canal, palabras vetadas y lista de control |
| [configura-tu-cierre](skills/configura-tu-cierre/) | Que el agente recuerde de un día para otro en qué quedó cada proyecto | Tu ritual de cierre de sesión y los archivos de memoria |
| [monta-tu-plantilla-documentos](skills/monta-tu-plantilla-documentos/) | Guías para pacientes, protocolos y apuntes siempre con tu imagen | Tu plantilla y una skill que genera y revisa el PDF |
| [configura-tu-transcriptor](skills/configura-tu-transcriptor/) | Pasar notas de voz, reuniones y clases a texto, acta o apuntes (el audio no sale de tu ordenador; el texto sí lo lee tu agente) | Un transcriptor instalado en local y tu flujo de audio a documento |
| [concurso-cierre-charla](skills/concurso-cierre-charla/) | Terminar una charla con un concurso de preguntas | Tu skill de concursos, con tu formato y el archivo para tu plataforma |
| [vigila-tu-tema](skills/vigila-tu-tema/) | Estar al día de lo que se publica sobre tu tema | Una vigilancia bibliográfica mensual en PubMed con cada referencia comprobada |
| [opera-tu-campus-virtual](skills/opera-tu-campus-virtual/) | Subir material y preparar tareas en Moodle | Tu skill con las recetas probadas en tu campus |
| [lee-tu-whatsapp](skills/lee-tu-whatsapp/) | Que el agente resuma chats, busque mensajes y descargue audios de tu WhatsApp para Mac, sin conectarse a tu cuenta ni enviar nada | Resúmenes, búsquedas, audios en Descargas y respuestas en borrador. Se usa tal cual (solo Mac) |
| [monta-tu-web-en-ghl](skills/monta-tu-web-en-ghl/) | Tener una web a medida en GoHighLevel con tu dominio y que tu agente la publique y la cambie cuando se lo pidas | Tu web publicada, su guía de estilo y una carpeta con copia y registro de cada cambio |

Si no sabes por cuál empezar: `verifica-citas` da resultado el primer día, y `ordena-tu-espacio-de-trabajo` hace que todas las demás funcionen mejor.

## Cómo se instala una skill

### La forma fácil: dásela a tu agente

Abre Claude Code o Codex y pídeselo con tus palabras:

> Instala la skill `crea-tu-estilo` del repositorio https://github.com/Drignacioalcala/skills-ia-medicos siguiendo su archivo INSTALAR.md.

El agente descarga el repositorio en tu carpeta de infraestructura (la carpeta donde guardas las herramientas que instalas), te cuenta qué hace la skill, la enlaza y te dice cómo usarla. Para actualizar más adelante: «actualiza las skills de skills-ia-medicos».

Después abre una conversación nueva y di, por ejemplo: «quiero que escribas como yo».

### A mano

1. Descarga este repositorio: botón verde «Code» (arriba a la derecha de la lista de archivos) → «Download ZIP», y descomprímelo.
2. Copia la carpeta de la skill que quieras (por ejemplo `skills/crea-tu-estilo`) a la carpeta de skills de tu agente:

| Agente | Carpeta en Mac y Linux | Carpeta en Windows |
|---|---|---|
| Claude Code | `~/.claude/skills/` | `%USERPROFILE%\.claude\skills\` |
| Codex | `~/.agents/skills/` | `%USERPROFILE%\.agents\skills\` |

Si la carpeta no existe, créala.

3. Abre una conversación nueva. La skill ya está disponible.

Las skills de este repositorio son las mismas para los dos agentes: son archivos de texto con el mismo formato.

## Tres normas de la casa

1. **Aquí no hay contraseñas ni claves de nadie, y tu skill tampoco debe llevarlas.** Si un servicio te pide una clave, es la tuya y se guarda fuera de la carpeta de la skill.
2. **Los datos de pacientes no deben pasar por el agente.** Un agente en la nube envía fuera de tu ordenador todo lo que lee. Las skills están escritas para que no lea historias, correos clínicos ni transcripciones con datos de pacientes.
3. **El agente propone, tú decides.** Ninguna de estas skills envía correos, publica ni borra nada por su cuenta.

## Proponer una skill

Si tienes una skill que te funciona y quieres compartirla, cuéntalo en la comunidad. Antes de publicarla se revisa que no lleve claves, datos de pacientes ni datos personales, y se prueba con un caso ficticio.

## Licencia

MIT. Úsalas, adáptalas y compártelas.
