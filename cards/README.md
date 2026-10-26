# Habitaciones: copiar, pegar y editar en Home Assistant

El **tema Arrel** pone los colores y estilos generales. Estos archivos son **ejemplos de tarjetas**, que añades a tu dashboard por separado. Una vez pegados, los editas en Home Assistant; no necesitas ejecutar scripts, generar archivos ni mantener una configuración externa.

## Instalación

1. Instala **Bubble Card >= 3.2.0** desde HACS. El ejemplo completo de Salón también requiere **Better Thermostat UI Card** y **Mushroom**; puedes eliminar sus controles si no los usas. Recarga el navegador.
2. En tu dashboard, entra en **Editar → Añadir tarjeta → Manual** y pega todo [arrel-rooms-paste.yaml](arrel-rooms-paste.yaml). Contiene Salón y Dormitorio en un stack horizontal.
3. Añade una tarjeta manual en **la misma vista** pegando [la plantilla de pop-up](arrel-room-popup-paste.yaml). Duplícala para Dormitorio y cambia `hash`, nombre, icono y las entidades de sus controles. Solo hay un archivo de ejemplo para todos los pop-ups.
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
    navigation_path: '#menjador'
tap_action:
  action: navigate
  navigation_path: '#menjador'
```

En el pop-up, configura `hash: '#menjador'`. Debe ser único en la vista y coincidir con los dos `navigation_path` de la habitación. Para Dormitorio utiliza `#room-dormitorio`, que es el enlace del ejemplo de habitaciones.

## Qué cambiar en el pop-up

El [ejemplo de Salón](arrel-room-popup-paste.yaml) es YAML directo, basado en tu configuración. Empieza con:

```yaml
type: custom:bubble-card
card_type: pop-up
hash: '#menjador'
name: Salón
icon: mdi:sofa
show_close_button: true
cards:
  # Controles del pop-up
```

Edita `hash`, `name` e `icon` y cambia el campo `entity` de cada control. En el termostato revisa también `window_sensor` y `humidity_sensor`. En el chip del filtro revisa su `entity` y la entidad escrita dentro de `content`. No hay variables ni una lista adicional de entidades que mantener, y no necesitas Config Template Card.

Incluye tres luces, temperatura/humedad, presencia/contacto, dos enchufes, termostato, purificador y sus chips informativos. El contacto `binary_sensor.door_casa_zigbee_contact` conserva el nombre «Ventana» de tu ejemplo; cámbialo a «Puerta» si corresponde.

Para añadir un dispositivo duplica su tarjeta dentro de `cards` y cambia nombre y entidad. Para quitarlo elimina su tarjeta y, si queda vacío, su stack o separador. Puedes borrar secciones completas para dejar únicamente lo básico. Las filas `horizontal-stack` contienen dos controles; un control impar puede ir a ancho completo. La tarjeta de habitaciones y el pop-up se editan por separado.

## Añadir o quitar habitaciones

- Para añadir otras dos habitaciones, duplica la tarjeta de la fila y cambia los campos iniciales de cada habitación y sus enlaces.
- Duplica también un pop-up por cada habitación nueva, cambiando `hash`, nombre, icono y entidades.
- Para una sola habitación, elimina el segundo elemento de `cards` en el stack horizontal y conserva solo el pop-up que uses.
- Para quitar una habitación, elimina su bloque y su tarjeta de pop-up.

## Indicadores y comprobación

El icono se colorea cuando la luz está encendida. El punto indica presencia. `▣` significa ventana abierta y `?` ventana sin datos. La temperatura respeta la unidad del sensor; los valores desconocidos se muestran como `—`.

Después de guardar, comprueba que cada habitación abre su pop-up, que el botón de luz controla la entidad correcta y que los indicadores se actualizan. Los estilos dependen de selectores de Bubble Card. Validación local del YAML y de la lógica JavaScript; pendiente de prueba visual en Home Assistant.

Referencia: [documentación oficial de Bubble Card](https://github.com/Clooos/Bubble-Card#readme).

## Probar en tu dashboard sin publicar

1. Copia `themes/arrel.yaml` a la ubicación donde ya tienes instalado el tema y ejecuta **Herramientas para desarrolladores → Acciones → `frontend.reload_themes`**. Si prefieres mantener intacta una instalación HACS, prueba una copia del tema con otro nombre raíz y selecciónala temporalmente. Tras publicar podrás actualizar Arrel desde HACS.
2. Selecciona Arrel en el perfil o en la vista y recarga el navegador. Los fondos compartidos, radios de 24 px y bordes eliminados se aplican mediante el tema; las tarjetas personalizadas con estilos fijos pueden ignorarlos.
3. Instala las tarjetas que conserves en el pop-up: Bubble Card, Better Thermostat UI Card y Mushroom. Config Template Card ya no es necesario para este ejemplo.
4. En una vista de pruebas pega las habitaciones y el pop-up. Comprueba que sus enlaces coinciden (`#menjador` para Salón). Si duplicas el pop-up para Dormitorio, usa `#room-dormitorio` y adapta sus controles.
5. Abre los pop-ups, comprueba cerrar, Atrás, luces y actualizaciones de sensores. Las acciones controlan los dispositivos reales configurados.
6. Comprueba claro/oscuro y móvil/escritorio. En las tarjetas de calendario, cuenta atrás o navegación de tu dashboard que mantengan bordes o fondos propios, revisa sus opciones de estilo: el tema no puede sustituir CSS fijado dentro de una tarjeta personalizada.

No hace falta reinstalar el dashboard de ejemplo ni modificar tus entidades para probar el nuevo diseño. La captura no contiene el YAML de tus tarjetas personalizadas; el tema unifica las variables comunes, pero sus ajustes particulares requieren ese YAML.

El pop-up es una Bubble Card directa; ya no tiene el contenedor que recreaba su contenido al cambiar sensores.

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

Conserva `horizontal-stack` para parejas de controles. El termostato, purificador y los botones impares pueden ocupar todo el ancho. Duplica o elimina los bloques directamente desde el editor YAML del dashboard. No hay generación de tarjetas ni build.

## Tiempo en una fila

Pega [arrel-weather-paste.yaml](arrel-weather-paste.yaml) en una tarjeta manual. Cambia `entity` y `name` al principio: el icono queda a la izquierda, la temperatura grande en el centro y la localidad con estado/humedad a la derecha. Todo abre Más información al pulsar. No usa subbotones inferiores ni Config Template Card.

La temperatura se lee de la misma entidad meteorológica y respeta `temperature_unit`; sin datos muestra `—`. El estilo comparte la superficie Arrel de las otras tarjetas. Solo cambia la composición de esta tarjeta, sin modificar Navbar ni los controles nativos.

Sustituye la tarjeta meteorológica anterior completa, no solo sus estilos. Comprueba el diseño en móvil y escritorio, claro/oscuro, textos largos y temperaturas negativas. Validación local del YAML y del formateo; pendiente de prueba visual en Home Assistant.

## Resumen de grupos existentes

No modifiques tus grupos si ya contienen los dispositivos correctos. Se leen `light.home_bulbs`, `switch.home_plug`, `binary_sensor.home_window` y `binary_sensor.home_door`. Confirma que esos son sus IDs reales y que tienen el atributo `entity_id`; si difieren, sustituye todas las apariciones del ID en `packages/arrel_summary.yaml`. No se crean grupos, automatizaciones ni acciones sobre tus dispositivos.

1. Copia [arrel_summary.yaml](../packages/arrel_summary.yaml) a `/config/packages/arrel_summary.yaml` si ya cargas paquetes desde esa carpeta.
2. Si todavía no cargas paquetes, integra esto en el bloque `homeassistant` existente de `configuration.yaml`, sin duplicarlo:

   ```yaml
   homeassistant:
     packages: !include_dir_named packages
   ```

3. Comprueba la configuración y reinicia Home Assistant. Si ya utilizas otra organización de paquetes, conserva esa estructura y añade allí el archivo. Esto se hace una vez; después gestionas los miembros desde tus grupos habituales.
4. Comprueba en Estados que existen `sensor.arrel_resumen_luces`, `sensor.arrel_resumen_enchufes`, `sensor.arrel_resumen_ventanas` y `sensor.arrel_resumen_puertas`. Si había IDs ocupados, adapta los `entity` de las tarjetas a los IDs asignados.
5. Pega [arrel-summary-paste.yaml](arrel-summary-paste.yaml) como tarjeta manual: contiene tres botones. Opcionalmente añade [arrel-plugs-summary-paste.yaml](arrel-plugs-summary-paste.yaml) como otra tarjeta.

Los sensores cuentan miembros `on`, también dentro de grupos anidados, sin duplicar IDs. Los atributos `missing_count` y `member_count` permiten distinguir datos incompletos. Un grupo inexistente, vacío o sin lista de miembros muestra «Sin datos». Si hay miembros desconocidos no se afirma que todo esté apagado/cerrado: se muestra «Sin datos completos» o el recuento conocido con `?`. Un contacto `on` se interpreta como abierto. No mezcles luces individuales con grupos de una integración que no expongan sus miembros: podrían contarse como dispositivos distintos.

Pulsar un resumen solo abre Más información del contador. No enciende ni apaga el grupo. Prueba dos dispositivos encendidos, apaga uno mientras el grupo sigue `on` y comprueba que el contador baja; prueba contactos abiertos, todos cerrados y uno no disponible. Comprueba también los textos a ancho móvil y los dos modos del tema. Validación local de plantillas y YAML; pendiente de prueba real en Home Assistant.

Referencia: [sensores Template de Home Assistant](https://www.home-assistant.io/integrations/template/).
