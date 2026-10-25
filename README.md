# Arrel · Prototipo para Home Assistant

Tema en grafito y porcelana, con acento azul pizarra, bordes finos y modos claro/oscuro. Diseñado para `custom:navbar-card`. El tema funciona por sí solo; el dashboard de ejemplo requiere Navbar Card y usa controles nativos con entidades simuladas.

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

## Instalar el dashboard con Navbar Card

Antes de copiar el dashboard, instala **Navbar Card** desde HACS. Si no aparece, añade `https://github.com/joseluis9595/lovelace-navbar-card` como repositorio personalizado de tipo **Dashboard** (Arrel se instala como **Theme**). Sigue las instrucciones de instalación de la tarjeta y recarga el navegador.

Comprueba en Ajustes → Paneles de control → Recursos (con modo avanzado activado) que está registrado el módulo `/hacsfiles/lovelace-navbar-card/navbar-card.js`. Si gestionas los recursos por YAML, añade esa URL con `type: module` a tu lista `lovelace.resources` existente. No lo registres dos veces. Si aparece «Custom element doesn't exist: navbar-card», revisa instalación, recurso y caché del navegador.


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

- Casa: resumen reactivo, aviso de ventana abierta y acceso rápido a la luz del salón.
- Luces: controles por estancia.
- Confort: consigna y apertura de persiana simuladas.
- Pulsa el icono de una luz para alternarla; pulsa la tarjeta para abrir sus detalles.
- Pruebas: modifica la temperatura y activa Ventana abierta para mostrar el aviso en Casa.
- Los ayudantes no están conectados a dispositivos. La temperatura no evoluciona al cambiar la consigna; el modo de casa no activa escenas. Sus valores iniciales se restablecen al reiniciar.
- Sections distribuye las secciones según el ancho disponible, hasta dos columnas. La cantidad real depende del viewport y de la barra lateral.

## Ajustar la navegación

La configuración común está en `navbar-templates.arrel_navigation` al inicio de `dashboards/arrel-demo.yaml`; cada vista incluye una única tarjeta que referencia esa plantilla.

- PC y tablet ancha, desde 1024 px: barra flotante a la izquierda.
- Móvil y tablet estrecha, por debajo de 1024 px: barra inferior con etiquetas y área segura para gestos.
- `layout.auto_padding` reserva espacio para evitar que la barra tape controles.
- Las cuatro rutas comienzan por `/arrel-pruebas/`. Si tu dashboard tiene otra URL, cambia ese prefijo en la plantilla. Conserva los sufijos `casa`, `luces`, `confort` y `laboratorio` o ajústalos junto a los `path` de las vistas.
- Los colores, radios y sombras de navbar se definen en `themes/arrel.yaml`. Los estilos de botones y etiquetas se comparten en la plantilla; no hace falta card-mod.
- Se conserva la cabecera nativa de Home Assistant para mantener sus menús accesibles.

Usa una versión de Navbar Card que incluya plantillas y `layout.auto_padding`; las opciones se han contrastado con la documentación actual. La integración visual sigue pendiente de prueba en una instancia real.

## Actualizar desde el prototipo anterior

Actualiza el tema desde HACS (o reemplaza su archivo manualmente), ejecuta `frontend.reload_themes` e instala Navbar Card. Reemplaza también `/config/dashboards/arrel-demo.yaml` con este ejemplo y recarga el dashboard. **HACS no actualiza el dashboard de ejemplo.** Si ya lo has personalizado, integra la plantilla y la tarjeta de navegación en tus vistas en lugar de sobrescribir tus cambios. El paquete de ayudantes no ha cambiado.

## Validación en tus pantallas

Prueba 360–390 px en móvil, 768–1024 px en tablet y 1440 px en PC; también tablet vertical/horizontal y zoom al 200 %. Revisa desbordamientos, legibilidad, acceso táctil y ambos modos. Comprueba que el contador cambia con las tres luces y que el aviso desaparece al cerrar la ventana simulada. Prueba también 1023/1024 px, las cuatro rutas, el indicador de ruta activa, la barra lateral de Home Assistant abierta/cerrada y el último control de cada vista: debe quedar accesible por encima de la navbar. Verifica el área de gestos en la app móvil y la navegación con teclado.

## Iteración y HACS

El tema está separado del dashboard. Podemos sustituir una tarjeta cada vez por una tarjeta personalizada y comparar comportamiento, colores y rendimiento. La compatibilidad con tarjetas personalizadas de HACS todavía no está verificada: anota nombre y versión de cada tarjeta antes de integrarla.

Para conectar dispositivos reales, sustituye los ayudantes por tus entidades. Los controles de `input_number` son simuladores: para `cover` o `climate` hay que cambiar también la tarjeta y sus controles. Usa una tarjeta Tile de luz para brillo y una tarjeta adecuada para climatización. El resumen contiene una lista explícita de las tres luces de prueba que también deberás actualizar.

Las variables de apariencia como radios, fondos y bordes pueden cambiar entre versiones de Home Assistant. Después de actualizar, revisa el tema y las tarjetas HACS.

Para modificar colores, edita `themes/arrel.yaml` y ejecuta `frontend.reload_themes`. Tras editar el dashboard YAML, recarga su vista. No es necesario reiniciar para cada ajuste visual.

## Publicar y versionar

Consulta [PUBLISHING.md](PUBLISHING.md) para publicar versiones. La siguiente versión propuesta es `v0.2.0`; no se ha creado el tag ni la release. Los cambios se registran en [CHANGELOG.md](CHANGELOG.md).

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
