# Habitaciones: copiar, pegar y editar en Home Assistant

El **tema Arrel** pone los colores y estilos generales. Estos archivos son **ejemplos de tarjetas**, que añades a tu dashboard por separado. Una vez pegados, los editas en Home Assistant; no necesitas ejecutar scripts, generar archivos ni mantener una configuración externa.

## Instalación

1. Instala **Bubble Card >= 3.2.0** y **Config Template Card** (`iantrich/config-template-card`) desde HACS y recarga el navegador. Config Template Card resuelve las variables del pop-up.
2. En tu dashboard, entra en **Editar → Añadir tarjeta → Manual** y pega todo [arrel-rooms-paste.yaml](arrel-rooms-paste.yaml). Contiene Salón y Dormitorio en un stack horizontal.
3. Añade una tarjeta manual en **la misma vista** pegando [la plantilla de pop-up](arrel-room-popup-paste.yaml). Duplícala para Dormitorio y cambia sus variables. Solo hay un archivo de ejemplo para todos los pop-ups.
4. Edita los datos de ejemplo como se explica abajo. Selecciona el tema Arrel para usar su paleta.

Estas tarjetas no requieren Decluttering Card, card-mod, `!include`, Python ni cambios en `configuration.yaml`. Actualizar el tema mediante HACS no modifica las tarjetas que has pegado.

## Qué cambiar en cada habitación

Abre la tarjeta de habitaciones y entra en su editor YAML. Al principio de cada elemento de `cards` encontrarás estos campos juntos:

```yaml
name: Salón
icon: mdi:sofa
entity: sensor.salon_temperatura
arrel_room:
  humidity: sensor.salon_humedad
  presence: binary_sensor.salon_presencia
  window: binary_sensor.salon_ventana
  light: light.salon
```

| Campo | Qué poner |
| --- | --- |
| `name` | El nombre que quieres mostrar. |
| `icon` | El icono de la habitación, por ejemplo `mdi:sofa`. |
| `entity` | Tu sensor de temperatura. Se usa también en el texto; solo se escribe una vez en esta habitación. |
| `arrel_room.humidity` | Tu sensor de humedad en porcentaje. |
| `arrel_room.presence` | Tu sensor de presencia: `on` detectada, `off` sin presencia. |
| `arrel_room.window` | Tu sensor de ventana: `on` abierta, `off` cerrada. |
| `arrel_room.light` | Tu luz, grupo de luces o interruptor; determina el color del icono. |

Copia los IDs reales desde **Herramientas para desarrolladores → Estados**. `arrel_room` es una configuración propia de este ejemplo: el JavaScript lee sus campos mediante `this.config.arrel_room`. La temperatura se lee de `this.config.entity`. **No cambies nada dentro de `styles` para personalizar las entidades.** Edita el bloque personalizado desde el editor YAML.

Si no tienes humedad, presencia, ventana o luz, puedes omitir ese campo de `arrel_room`. Los sensores ausentes muestran `—`, la ventana sin datos muestra `?` y los indicadores de presencia/luz quedan inactivos. Elimina también el control correspondiente del pop-up. No hace falta configurar un área: el título usa directamente `name`.

## Cómo conectar la habitación con su pop-up

Justo antes de los estilos están las acciones. Cambia los **dos** `navigation_path` si cambias el identificador del pop-up:

```yaml
button_action:
  tap_action:
    action: navigate
    navigation_path: '#room-salon'
tap_action:
  action: navigate
  navigation_path: '#room-salon'
```

En la plantilla de pop-up, el identificador se configura en `variables.popup_id`. Debe ser único en la vista y coincidir exactamente con los dos enlaces de la habitación; no necesita coincidir con un área de Home Assistant.

## Qué cambiar en el pop-up

La [plantilla genérica](arrel-room-popup-paste.yaml) empieza sin dispositivos. Edita solo `variables`: una entidad vacía (`"''"`) omite el control; una sección sin controles desaparece automáticamente. No edites `entities` ni el JavaScript para activar o quitar los dispositivos previstos.

Ejemplo para una cocina sin luces y con un enchufe (campos que debes cambiar dentro de `variables`; conserva los demás):

```yaml
popup_id: "'#room-cocina'"
room_name: "'Cocina'"
room_icon: "'mdi:countertop-outline'"
plug_1: "'switch.enchufe_cocina'"
plug_1_name: "'Enchufe cocina'"
```

`popup_id` debe coincidir con los dos `navigation_path` de la habitación. Conserva las comillas exteriores e interiores: Config Template Card evalúa los valores como expresiones JavaScript.

| Campos | Uso |
| --- | --- |
| `light_1`, `light_2`, `light_3` | Hasta tres luces regulables opcionales. |
| `light_1_name`, `light_2_name`, `light_3_name` | Nombres de esas luces. |
| `plug_1`, `plug_2` | Hasta dos enchufes o interruptores opcionales. |
| `plug_1_name`, `plug_2_name` | Nombres de los enchufes; ninguno está ligado a un aspirador. |
| `temperature`, `humidity`, `presence`, `window` | Sensores opcionales e independientes. |
| `window_name` | Nombre del contacto, por ejemplo Ventana o Puerta. |
| `climate`, `climate_window` | Termostato y su contacto opcional; solo necesitas Better Thermostat UI Card si rellenas `climate`. |
| `purifier` | Ventilador/purificador opcional con control de velocidad. |

Para desactivar un dispositivo vuelve a poner su entidad en `"''"`. Los nombres no activan controles por sí solos. Las parejas se reorganizan automáticamente y el último botón impar queda a ancho completo. Si todo está vacío aparece una indicación de configuración. Una entidad configurada pero no disponible conserva su control para que puedas detectar el problema.

La habitación y el pop-up siguen siendo independientes: configura sus entidades en ambas tarjetas. No hay build ni archivo externo. No definas variables globales de Config Template Card con los mismos nombres.

## Añadir o quitar habitaciones

- Para añadir otras dos habitaciones, duplica la tarjeta de la fila y cambia los campos iniciales de cada habitación y sus enlaces.
- Duplica también un pop-up por cada habitación nueva, cambiando su bloque `variables`.
- Para una sola habitación, elimina el segundo elemento de `cards` en el stack horizontal y conserva solo el pop-up que uses.
- Para quitar una habitación, elimina su bloque y su tarjeta de pop-up.

## Indicadores y comprobación

El icono se colorea cuando la luz está encendida. El punto indica presencia. `▣` significa ventana abierta y `?` ventana sin datos. La temperatura respeta la unidad del sensor; los valores desconocidos se muestran como `—`.

Después de guardar, comprueba que cada habitación abre su pop-up, que el botón de luz controla la entidad correcta y que los indicadores se actualizan. Los estilos dependen de selectores de Bubble Card. Validación local del YAML y de la lógica JavaScript; pendiente de prueba visual en Home Assistant.

Referencia: [documentación oficial de Bubble Card](https://github.com/Clooos/Bubble-Card#readme).

## Probar en tu dashboard sin publicar

1. Copia `themes/arrel.yaml` a la ubicación donde ya tienes instalado el tema y ejecuta **Herramientas para desarrolladores → Acciones → `frontend.reload_themes`**. Si prefieres mantener intacta una instalación HACS, prueba una copia del tema con otro nombre raíz y selecciónala temporalmente. Tras publicar podrás actualizar Arrel desde HACS.
2. Selecciona Arrel en el perfil o en la vista y recarga el navegador. Los fondos compartidos, radios de 24 px y bordes eliminados se aplican mediante el tema; las tarjetas personalizadas con estilos fijos pueden ignorarlos.
3. Instala Config Template Card y comprueba su recurso `/hacsfiles/config-template-card/config-template-card.js` si aparece «Custom element doesn't exist». Recarga el navegador después de instalarlo.
4. En una vista de pruebas, pega la fila de habitaciones y dos copias de la plantilla de pop-up. Usa tus entidades y los IDs `#room-salon` y `#room-dormitorio`.
5. Abre ambos pop-ups por separado. Comprueba cerrar, volver a abrir, Atrás y alternar la luz. Cambia humedad o ventana manteniendo fija la temperatura y verifica que los estados se actualicen. Comprueba también que las actualizaciones no interrumpan el pop-up abierto: Config Template Card vuelve a crear su tarjeta cuando cambia una entidad observada, por lo que este comportamiento debe validarse con tu versión de Bubble Card.
6. Comprueba claro/oscuro y móvil/escritorio. En las tarjetas de calendario, cuenta atrás o navegación de tu dashboard que mantengan bordes o fondos propios, revisa sus opciones de estilo: el tema no puede sustituir CSS fijado dentro de una tarjeta personalizada.

No hace falta reinstalar el dashboard de ejemplo ni modificar tus entidades para probar el nuevo diseño. La captura no contiene el YAML de tus tarjetas personalizadas; el tema unifica las variables comunes, pero sus ajustes particulares requieren ese YAML.

Referencia de variables: [Config Template Card](https://github.com/iantrich/config-template-card#readme).

## Navbar con el mismo diseño

Usa [arrel-navbar-paste.yaml](arrel-navbar-paste.yaml). Si ya tienes una navbar, copia solo su bloque `styles` en el editor YAML de la tarjeta existente y conserva tus rutas. El ejemplo aplica la superficie de las habitaciones, radios de 24 px, fondos de iconos de 16 px, colores de texto del tema y elimina las sombras en móvil y escritorio. El menú desplegable comparte el estilo de los botones.

Recarga el tema y el navegador. Comprueba que una tarjeta nativa, una Bubble Card y la navbar tienen fondos y bordes coherentes en claro y oscuro. No es necesario instalar card-mod ni Mushroom para esta navbar.

## Regular el brillo de las luces

La plantilla de pop-up usa `button_type: slider` para la luz: mantén pulsada la barra y arrastra; el porcentaje aparece a la derecha y se aplica al soltar. El icono permite encender/apagar. Usa una entidad `light` regulable; un `switch` o `input_boolean` solo admite encendido/apagado y debe conservar `button_type: switch`.

El recorrido completo tiene un fondo ligeramente separado y una sombra interior difusa, sin borde. Actualiza el tema y ejecuta `frontend.reload_themes`; copia también el control de luz actualizado a los pop-ups ya pegados. El tema por sí solo no cambia `switch` a `slider`. Prueba 10 %, 50 % y 100 %, apagado, claro y oscuro. Comprueba que al soltar se mantiene abierto el pop-up y que el brillo real cambia.

El mismo acabado se aplica a los sliders de la demo y al recorrido del reproductor de Navbar cuando se utiliza. Las luces simuladas de la demo siguen siendo interruptores porque son `input_boolean`; los controles nativos conservan su recorrido y mando propios.

## Termostato Better Thermostat

Copia [arrel-thermostat-paste.yaml](arrel-thermostat-paste.yaml) en **Editar dashboard → Añadir tarjeta → Manual**. Requiere **Better Thermostat UI Card** instalado desde HACS, en una versión que incluya `custom:better-thermostat-normal-climate-card`, y el tema **Arrel** seleccionado. No necesita card-mod, Config Template Card ni un build. Si utilizas la integración Better Thermostat, comprueba la compatibilidad entre las versiones de la integración y su tarjeta.

El ejemplo conserva tu configuración:

```yaml
type: custom:better-thermostat-normal-climate-card
entity: climate.termostat_menjador_zigbee
name: Termostat
window_sensor: binary_sensor.window_menjador_zigbee_contact
humidity_sensor: sensor.temperature_menjador_zigbee_humidity
low_battery_threshold: 10
show_current_as_primary: false
show_secondary: true
colors:
  heat: deep-purple
```

Modifica `entity`, `window_sensor` y `humidity_sensor` si cambias de dispositivo; `name` es el título y `low_battery_threshold` el umbral de batería baja. Se mantiene el morado para identificar calefacción. Si prefieres el acento azul de Arrel, cambia únicamente `colors.heat` a `var(--primary-color)`.

La superficie usa las variables nativas del tema: `ha-card-background`, `ha-card-border-radius`, `ha-card-border-width` y `ha-card-box-shadow`. Así comparte fondo, esquinas de 24 px y ausencia de borde/sombra con las habitaciones, Bubble Card y Navbar Card, conservando el dial y los colores funcionales del termostato. No hace falta pegar CSS adicional.

Para probar: actualiza el tema si todavía tienes una versión anterior, ejecuta `frontend.reload_themes`, selecciona Arrel y recarga el navegador. Añade la tarjeta y comprueba temperatura actual/objetivo, humedad, indicador de ventana y modos disponibles, en claro y oscuro y en móvil. Ajustar la consigna actúa sobre tu termostato real. Validación local del YAML y revisión del código de la tarjeta; pendiente de prueba visual en Home Assistant.

Referencia: [Better Thermostat UI Card — configuración y colores](https://github.com/KartoffelToby/better-thermostat-ui-card#readme).

## Pop-ups con dos botones por fila

Los controles configurados se agrupan por parejas dentro de Iluminación, Ambiente y Enchufes. Termostato y purificador quedan a ancho completo. La plantilla ofrece tres huecos para luces y dos para enchufes; añadir más requiere ampliar las variables, las referencias de `entities` y la lista correspondiente en el JavaScript. No es necesario hacerlo para quitar dispositivos.

Para probar, configura un solo enchufe: no deben aparecer Iluminación ni Ambiente. Añade otro enchufe y comprueba la fila de dos. Vacía ambos y comprueba que desaparece la sección. Revisa móvil y claro/oscuro. Comprueba también que las actualizaciones no cierren el pop-up: Config Template Card recrea su contenido cuando cambia una entidad observada.
