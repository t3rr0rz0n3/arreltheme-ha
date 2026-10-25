# Panel de habitaciones

Panel completo inspirado en la referencia: dos columnas, iconos elevados, estado de luces, temperatura/humedad, presencia y pop-up por habitación. Claro y oscuro siguen el tema Arrel. El icono se vuelve dorado cuando la luz está encendida; el punto es azul con presencia y gris sin ella. `▣` indica ventana abierta y `?` ventana sin datos. Los valores desconocidos se muestran como `—`.

La cabecera muestra la temperatura media de los sensores disponibles (solo si usan la misma unidad) y el número de ventanas abiertas; `?` indica que faltan datos de alguna ventana. Los indicadores de cabecera son informativos. No se incluyen los desplegables de cabecera/pie de la imagen; cada tarjeta de habitación sí abre sus controles. Es una adaptación del diseño, pendiente de comprobar visualmente en Home Assistant.

## Dependencias

Instala desde HACS y comprueba que los recursos JavaScript están cargados:

- Bubble Card >= 3.2.0 (`Clooos/Bubble-Card`).
- Decluttering Card (`custom-cards/decluttering-card`).
- card-mod, en una versión compatible con tu Home Assistant (`thomasloven/lovelace-card-mod`).
- Tema Arrel actualizado. No requiere Mushroom ni Navbar para este panel independiente.

## Instalación como dashboard de prueba

1. Copia los dos YAML de `cards/` a `/config/cards/`.
2. Copia `dashboards/arrel-rooms.yaml` a `/config/dashboards/`.
3. En `/config/cards/arrel-rooms.yaml`, modifica únicamente los bloques de variables dentro de `arrel_rooms` en la cabecera. Las entidades de ejemplo no se crean automáticamente: usa entidades existentes. Las anclas YAML (`&id001`) y referencias (`*id001`) reutilizan cada bloque en la cuadrícula. Para añadir o quitar habitaciones, ajusta tanto la lista de cabecera como su instancia `custom:decluttering-card` en la cuadrícula.
4. Añade esta entrada a tu bloque `lovelace.dashboards` existente de `configuration.yaml`:

```yaml
arrel-habitaciones:
  mode: yaml
  title: Habitaciones
  icon: mdi:floor-plan
  show_in_sidebar: true
  filename: dashboards/arrel-rooms.yaml
```

Comprueba la configuración y reinicia para registrar el dashboard. Selecciona Arrel y prueba ambos modos.

La cabecera usa `arrel_rooms` como configuración de sus plantillas JavaScript locales; no es una opción estándar de Bubble Card. No hace falta editar el JavaScript.

## Configuración de una habitación

```yaml
type: custom:decluttering-card
template: arrel_room
variables:
  - area: salon
  - name: Salón
  - icon: mdi:sofa
  - temperature: sensor.salon_temperatura
  - humidity: sensor.salon_humedad
  - presence: binary_sensor.salon_presencia
  - window: binary_sensor.salon_ventana
  - light: light.salon
```

`area` es el ID de área (no su nombre visible). Se usa para el hash único `#room-salon` y para buscar su nombre. El nombre `name` sirve de reserva y de cabecera del pop-up. No autodescubre entidades: así puedes escoger qué sensor y qué luz o grupo representa cada habitación. Usa IDs de área habituales (letras, números, guiones bajos); no introduzcas comillas ni código en las variables. No repitas un área en la misma vista porque duplicaría el hash.

Los sensores de presencia y ventana deben tener estado `on`/`off`. El grupo de luz puede ser `light` o `switch`; el botón principal es de encendido/apagado. Humedad debe estar en porcentaje. La temperatura respeta la unidad del sensor. Las cinco entidades son necesarias para el pop-up completo; si una habitación carece de alguno de esos dispositivos, crea una variante de la plantilla quitando ese control en vez de inventar una entidad.

## Añadirlo a un dashboard existente

En un dashboard YAML, añade en la raíz `decluttering_templates: !include ../cards/arrel-room-templates.yaml` si el dashboard vive en `/config/dashboards/`. Si ya tienes plantillas, combina ambos mapas, sin duplicar la clave. Luego añade `!include ../cards/arrel-rooms.yaml` a la lista de tarjetas de tu vista.

Para un dashboard gestionado desde la interfaz, pega el contenido de `arrel-room-templates.yaml` bajo la clave raíz `decluttering_templates` en el editor de configuración sin procesar; después pega `arrel-rooms.yaml` como tarjeta manual. `!include` solo funciona en dashboards YAML, no en el editor de tarjetas.

Puedes colocar una sola instancia `custom:decluttering-card` en cualquier vista que tenga las plantillas definidas: incluye tanto su tarjeta como su pop-up. Para mantener el diseño de la referencia, coloca varias instancias dentro de una cuadrícula nativa de dos columnas.

## Pruebas y mantenimiento

Prueba a 360, 390, 768 y 1440 px, con nombres largos y zoom. Comprueba icono de luz, presencia, ventana, sensores desconocidos y cada pop-up (abrir, cerrar, Escape/Atrás y alternar luz). Prueba cambios de humedad/presencia mientras la temperatura permanece constante. Si usas Navbar, verifica que el pop-up quede por encima de ella.

Los estilos usan selectores de Bubble Card; una actualización de esa tarjeta puede requerir ajustes. No se ha ejecutado esta tarjeta en un Home Assistant real. HACS actualiza el tema, pero estos YAML se copian aparte. Conserva tu archivo personalizado `arrel-rooms.yaml` al actualizar; los estilos compartidos están en `arrel-room-templates.yaml`.

Fuentes: [Bubble Card](https://github.com/Clooos/Bubble-Card), [Decluttering Card](https://github.com/custom-cards/decluttering-card), [card-mod](https://github.com/thomasloven/lovelace-card-mod).
