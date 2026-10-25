# Arrel · Prototipo para Home Assistant

Tema en grafito y porcelana, con acento azul pizarra, bordes finos y modos claro/oscuro. Diseñado principalmente para `custom:bubble-card`, con `custom:navbar-card` para navegación general. Mushroom Template Card muestra los resúmenes. El tema funciona por sí solo; el dashboard requiere las tres colecciones y usa entidades simuladas.

## Instalar solo el tema

### Instalación manual (GitHub o Forgejo)

1. Descarga el código de una release y copia `themes/arrel.yaml` a `/config/themes/arrel/arrel.yaml`, creando la carpeta si hace falta.
2. Habilita los temas en `configuration.yaml` con el bloque siguiente. Si ya tienes `frontend`, añade únicamente `themes` dentro de él; conserva tu inclusión si ya existe.

```yaml
frontend:
  themes: !include_dir_merge_named themes
```

3. Si acabas de añadir la configuración, compruébala y reinicia Home Assistant. Si los temas ya estaban habilitados, ejecuta `frontend.reload_themes` desde Herramientas de desarrollador → Acciones.
4. Selecciona **Arrel** en tu perfil y elige claro, oscuro o el modo del sistema.

Para actualizar manualmente, descarga una nueva release, reemplaza ese mismo archivo y ejecuta `frontend.reload_themes`. No hay actualizaciones automáticas configuradas para la instalación manual.

### Desde HACS (GitHub)

Repositorio: https://github.com/t3rr0rz0n3/arreltheme-ha

1. Habilita los temas con el bloque anterior y reinicia si has cambiado `configuration.yaml`.
2. En HACS → ⋮ → Repositorios personalizados, añade `https://github.com/t3rr0rz0n3/arreltheme-ha`, selecciona **Theme** y añádelo.
3. Busca **Arrel**, descárgalo y selecciónalo en tu perfil. Si no aparece, ejecuta `frontend.reload_themes` y recarga la página.
4. Instala las siguientes actualizaciones desde HACS; recarga los temas si el cambio no se refleja.

HACS gestiona únicamente el tema. No instala los archivos de `dashboards/` ni de `packages/`. Evita editar el archivo gestionado por HACS: las actualizaciones pueden sustituirlo.

Si instalaste antes el tema en `/config/themes/arrel.yaml`, elimina esa copia al pasar a `/config/themes/arrel/arrel.yaml` o a HACS para evitar dos definiciones de `Arrel`.

## Instalar el dashboard con Bubble Card, Navbar Card y Mushroom

Antes de copiar el dashboard, instala **Bubble Card 3.2.0 o posterior**, **Navbar Card** y **Mushroom 5 o posterior** desde HACS. Mushroom está en `https://github.com/piitaya/lovelace-mushroom` (tipo Dashboard). Bubble Card usa el repositorio `https://github.com/Clooos/Bubble-Card`, de tipo **Dashboard**. Esta versión mínima es necesaria para los pop-ups independientes con contenido en `cards`.

Instala también **Navbar Card** desde HACS. Si no aparece, añade `https://github.com/joseluis9595/lovelace-navbar-card` como repositorio personalizado de tipo **Dashboard** (Arrel se instala como **Theme**). Sigue las instrucciones de instalación de la tarjeta y recarga el navegador.

Comprueba en Ajustes → Paneles de control → Recursos (con modo avanzado activado) que están registrados los módulos `/hacsfiles/lovelace-navbar-card/navbar-card.js` , `/hacsfiles/Bubble-Card/bubble-card.js` y `/hacsfiles/lovelace-mushroom/mushroom.js`. Si gestionas los recursos por YAML, añade las tres URLs con `type: module` a tu lista `lovelace.resources` existente. No registres un recurso dos veces. Si aparece «Custom element doesn't exist: navbar-card», revisa instalación, recurso y caché del navegador.


Si ya instalaste el tema manualmente o mediante HACS, copia solo el dashboard y el paquete en el paso 1 y conserva la configuración de temas existente.


1. Instala el tema siguiendo uno de los métodos anteriores. Copia `packages/arrel_demo.yaml` y `dashboards/arrel-demo.yaml` a esas mismas carpetas dentro de `/config` en Home Assistant. Crea las carpetas si no existen.
2. Integra lo siguiente en `/config/configuration.yaml`. Si ya tienes bloques `frontend`, `homeassistant` o `lovelace`, añade las claves dentro de ellos: no dupliques los bloques ni sustituyas la configuración existente. Si ya incluyes temas o paquetes desde otra carpeta, copia los archivos allí y conserva tus inclusiones.

```yaml
frontend:
  themes: !include_dir_merge_named themes

homeassistant:
  packages: !include_dir_named packages

lovelace:
  dashboards:
    arrel-pruebas:
      mode: yaml
      title: Arrel · Pruebas
      icon: mdi:palette-outline
      show_in_sidebar: true
      filename: dashboards/arrel-demo.yaml
```

3. Comprueba la configuración desde Herramientas de desarrollador → YAML y reinicia Home Assistant para cargar los ayudantes y registrar el dashboard.
4. Abre **Arrel · Pruebas** en la barra lateral. El dashboard solicita el tema Arrel; selecciona también Arrel en tu perfil para tematizar toda la interfaz. Alterna los modos claro y oscuro desde el perfil.

Usa una versión actual de Home Assistant con vistas Sections y tarjetas Heading. No se ha ejecutado este prototipo en una instancia real de Home Assistant; la validación local comprueba la estructura de los archivos y sus referencias.

## Qué puedes probar

- Casa: resumen reactivo y tarjetas de Salón, Cocina y Dormitorio. Un toque en el nombre o icono de la habitación abre su pop-up; el subbotón Luz permite alternar la luz sin abrirlo.
- Cada habitación agrupa sus controles en un pop-up Bubble Card. El salón incluye luz, temperatura, consigna, persiana y ventana; cocina y dormitorio incluyen su luz.
- Luces: controles por estancia.
- Confort: consigna y apertura de persiana simuladas.
- Las tarjetas de luz alternan su estado al pulsarlas. Los controles numéricos usan sliders Bubble Card: mantén pulsado y arrastra para ajustar; no envían cambios continuamente mientras deslizas.
- Pruebas: modifica la temperatura y activa Ventana abierta para mostrar el aviso en Casa.
- Los ayudantes no están conectados a dispositivos. La temperatura no evoluciona al cambiar la consigna; el modo de casa no activa escenas. Sus valores iniciales se restablecen al reiniciar.
- Sections distribuye las secciones según el ancho disponible, hasta dos columnas. La cantidad real depende del viewport y de la barra lateral.

## Mushroom Template Card

En Casa, `custom:mushroom-template-card` se utiliza para el resumen de luces/modo/temperatura y el estado de la ventana. El resumen abre Luces; la ventana abre el pop-up del salón y una pulsación larga muestra los detalles. La ventana distingue abierta, cerrada y sin datos. El resumen indica luces sin datos cuando están `unknown` o `unavailable`.

Se usa la Template Card moderna de Mushroom 5+, basada en Tile. Hereda fondos, bordes, radios y textos del tema Home Assistant; `color: primary` aplica el acento de Arrel en ambos modos y la alerta usa `var(--warning-color)`. No necesita Mushroom Themes ni card-mod. Las variables antiguas `mush-*` no afectan a esta tarjeta. Esta configuración usa `color` e `icon_tap_action`, no las opciones legacy `icon_color` y `layout`.

Para añadir una tarjeta similar:

```yaml
type: custom:mushroom-template-card
entity: input_boolean.arrel_demo_luz_salon
primary: Luz del salón
secondary: "{{ 'Encendida' if is_state(entity, 'on') else 'Apagada' if is_state(entity, 'off') else 'Sin datos' }}"
icon: mdi:lightbulb-outline
color: "{{ 'primary' if is_state(entity, 'on') else 'disabled' }}"
tap_action:
  action: more-info
icon_tap_action:
  action: toggle
```

Si cambias las entidades del resumen, actualiza también su lista `entity_id`, que controla qué cambios disparan las plantillas. Si cambias la URL del dashboard, ajusta las acciones de navegación del resumen además de las rutas de Navbar Card. Los hashes de habitación deben corresponder a un pop-up de la misma vista.

## Añadir habitaciones y entidades

La vista Casa contiene un botón de acceso y un `card_type: pop-up` por habitación. Cada pop-up tiene un `hash` único (`#salon`, `#cocina`, `#dormitorio`) y sus entidades están agrupadas dentro de `cards`. Se cierran con la X; prueba también Atrás en el móvil y Escape en escritorio.

Para añadir una habitación, duplica un botón de acceso y un pop-up dentro de la misma vista, cambia nombre/icono y asigna el mismo hash nuevo a `navigation_path` y `hash`. Después añade sus controles a `cards`. El botón configura por separado la acción del cuerpo (`button_action.tap_action`) y la del icono (`tap_action`) para que ambos abran la habitación.

Para pasar a dispositivos reales, sustituye las entidades de ejemplo tanto en los pop-ups como en los subbotones, accesos globales y contador de luces. Usa un botón Bubble de tipo `switch` para luces sin regulación, `slider` para luces regulables, y tarjetas `cover`/`climate` para dispositivos reales de persiana/climatización. La persiana y consigna actuales son `input_number`, no dispositivos de esos dominios. Los sensores de temperatura y ventana se muestran con botones de tipo `state`.

Los ayudantes del paquete no han cambiado. El prototipo solo tiene sensores de ambiente en el salón: añade los de cada habitación cuando conozcamos tus entidades, sin reutilizar el mismo sensor como si midiera varias habitaciones.

## Ajustar la navegación

Navbar Card mantiene Casa, Luces, Confort y Pruebas como accesos generales; los detalles por habitación se abren con Bubble Card desde Casa.

La configuración común está en `navbar-templates.arrel_navigation` al inicio de `dashboards/arrel-demo.yaml`; cada vista incluye una única tarjeta que referencia esa plantilla.

- PC y tablet ancha, desde 1024 px: barra flotante a la izquierda.
- Móvil y tablet estrecha, por debajo de 1024 px: barra inferior con etiquetas y área segura para gestos.
- `layout.auto_padding` reserva espacio para evitar que la barra tape controles.
- Las cuatro rutas comienzan por `/arrel-pruebas/`. Si tu dashboard tiene otra URL, cambia ese prefijo en la plantilla. Conserva los sufijos `casa`, `luces`, `confort` y `laboratorio` o ajústalos junto a los `path` de las vistas.
- Los colores, radios y sombras de navbar se definen en `themes/arrel.yaml`. Los estilos de botones y etiquetas se comparten en la plantilla; no hace falta card-mod.
- Se conserva la cabecera nativa de Home Assistant para mantener sus menús accesibles.

Usa una versión de Navbar Card que incluya plantillas y `layout.auto_padding`; las opciones se han contrastado con la documentación actual. La integración visual sigue pendiente de prueba en una instancia real.

## Actualizar desde el prototipo anterior

Actualiza el tema desde HACS (o reemplaza su archivo manualmente), ejecuta `frontend.reload_themes` e instala Bubble Card, Navbar Card y Mushroom. Reemplaza también `/config/dashboards/arrel-demo.yaml` con este ejemplo y recarga el dashboard. **HACS no actualiza el dashboard de ejemplo.** Si ya lo has personalizado, integra la plantilla y la tarjeta de navegación en tus vistas en lugar de sobrescribir tus cambios. El paquete de ayudantes no ha cambiado.

## Validación en tus pantallas

Prueba 360–390 px en móvil, 768–1024 px en tablet y 1440 px en PC; también tablet vertical/horizontal y zoom al 200 %. Revisa desbordamientos, legibilidad, acceso táctil y ambos modos. Comprueba que el contador cambia con las tres luces y que el aviso desaparece al cerrar la ventana simulada. Prueba también 1023/1024 px, las cuatro rutas, el indicador de ruta activa, la barra lateral de Home Assistant abierta/cerrada y el último control de cada vista: debe quedar accesible por encima de la navbar. Verifica el área de gestos en la app móvil y la navegación con teclado. Abre y cierra cada habitación, prueba sliders y subbotones, y comprueba que el pop-up recibe las pulsaciones por encima de la navbar. Prueba también entidades no disponibles y textos largos.

## Iteración y HACS

El tema está separado del dashboard. Podemos sustituir una tarjeta cada vez por una tarjeta personalizada y comparar comportamiento, colores y rendimiento. La compatibilidad con tarjetas personalizadas de HACS todavía no está verificada: anota nombre y versión de cada tarjeta antes de integrarla.

Para conectar dispositivos reales, sustituye los ayudantes por tus entidades. Los controles de `input_number` son simuladores: para `cover` o `climate` hay que cambiar también la tarjeta y sus controles. Usa una tarjeta Tile de luz para brillo y una tarjeta adecuada para climatización. El resumen contiene una lista explícita de las tres luces de prueba que también deberás actualizar.

Las variables de apariencia como radios, fondos y bordes pueden cambiar entre versiones de Home Assistant. Después de actualizar, revisa el tema y las tarjetas HACS.

Para modificar colores, edita `themes/arrel.yaml` y ejecuta `frontend.reload_themes`. Tras editar el dashboard YAML, recarga su vista. No es necesario reiniciar para cada ajuste visual.

## Publicar y versionar

Consulta [PUBLISHING.md](PUBLISHING.md) para publicar versiones. La siguiente versión propuesta es `v0.5.0`; no se ha creado el tag ni la release. Los cambios se registran en [CHANGELOG.md](CHANGELOG.md).

## Retirada

Si instalaste el tema con HACS, retíralo desde HACS. Para la instalación manual elimina el archivo del tema de la ruta que utilizaste. Si instalaste la demo, elimina la entrada `arrel-pruebas` de tus dashboards y los tres archivos instalados. Selecciona otro tema y reinicia para retirar los ayudantes. Conserva las inclusiones de temas/paquetes si las usan otros archivos.

## Referencias

- [Temas](https://www.home-assistant.io/integrations/frontend/)
- [Sections](https://www.home-assistant.io/dashboards/sections/)
- [Packages](https://www.home-assistant.io/docs/configuration/packages/)
- [Dashboards YAML](https://www.home-assistant.io/dashboards/dashboards/)

- [Navbar Card: instalación](https://joseluis9595.github.io/lovelace-navbar-card/docs/getting-started/installation/)
- [Navbar Card: estilos](https://joseluis9595.github.io/lovelace-navbar-card/docs/configuration/styles/)
- [Navbar Card: espacio para la navegación](https://joseluis9595.github.io/lovelace-navbar-card/docs/configuration/layout/)

- [Bubble Card: configuración oficial](https://github.com/Clooos/Bubble-Card#readme)

- [Mushroom Template Card: configuración y temas](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/template.md)

## Panel de habitaciones de dos columnas

La tarjeta completa inspirada en la referencia está en [cards/arrel-rooms.yaml](cards/arrel-rooms.yaml). Edita los bloques de área y entidades; la plantilla compartida genera cada tarjeta con su pop-up. Consulta [instalación y configuración](cards/README.md). Requiere Bubble Card, Decluttering Card y card-mod. Incluye un dashboard independiente para probarlo.
