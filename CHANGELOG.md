# Historial de cambios

## 0.6.4 — Sin publicar

- Pop-up de salón con parejas de botones en horizontal-stack y entidades centralizadas.
- Tres luces regulables, ambiente, enchufes, termostato y purificador; acciones anidadas y feature fan-speed corregidas.

## 0.6.3 — Sin publicar

- Ejemplo Better Thermostat normal con entidades editables, ventana, humedad y calefacción morada.
- Superficie integrada mediante las variables nativas de Arrel, sin CSS adicional ni card-mod.
- Guía de instalación y pruebas en el dashboard.

## 0.6.2 — Sin publicar

- Luz del pop-up regulable mediante slider con porcentaje y envío al soltar.
- Recorrido visible con fondo diferenciado y sombra interior suave, sin bordes, en claro y oscuro.
- Acabado compartido con sliders de la demo y recorrido del reproductor Navbar.

## 0.6.1 — Sin publicar

- Navbar con el diseño de habitaciones: superficie, iconos, estados activos y menú desplegable; sin sombras en móvil ni escritorio.
- Ejemplo autónomo de navbar para pegar o copiar solo sus estilos conservando las rutas existentes.
- Criterio de mantenimiento visual conjunto para tarjetas nativas, Bubble Card y Navbar Card.


## 0.6.0 — Sin publicar

- Una plantilla de pop-up con nombre, icono, ID de apertura y entidades agrupados en variables; requiere Config Template Card.
- Superficies compartidas con habitaciones: radios de 24 px, sin bordes y fondos de iconos de 16 px, en claro y oscuro.
- Guía para copiar, duplicar y probar las tarjetas directamente en el dashboard.


## 0.5.1 — Sin publicar

- Tarjeta autónoma `cards/arrel-rooms-paste.yaml` para pegar en el editor Manual.
- Entidades agrupadas al principio de cada habitación y leídas por el JavaScript.
- Pop-ups independientes; edición directa desde el dashboard, sin generador ni archivos de variables externos.
- Retiradas las plantillas y el dashboard de prueba del flujo anterior de habitaciones.
- Guía simplificada para evitar confundir configuración de dashboard y de tarjeta.
- Sin cambios visuales en el tema; actualizar HACS por sí solo no añade esta tarjeta.

## 0.5.0 — Sin publicar

- Panel reutilizable de habitaciones en dos columnas con Bubble Card y pop-ups.
- Entidades y área configurables una sola vez por habitación mediante Decluttering Card.
- Tema de superficies e iconos claro/oscuro, humedad, temperatura, presencia y ventana.
- Dashboard independiente y guía de instalación; requiere card-mod para el contenedor.

Validación local de estructura y plantillas; pendiente de prueba visual en Home Assistant.

## 0.4.0 — Sin publicar

- Mushroom Template Card moderna en la portada: resumen reactivo y estado de ventana.
- Accesos directos a Luces y al pop-up del salón, con estados sin datos explícitos.
- Colores del tema HA para Mushroom, incluyendo texto deshabilitado; sin dependencia de card-mod ni Mushroom Themes.
- El dashboard requiere ahora Mushroom >= 5 además de Bubble Card y Navbar Card.
- Sin cambios en los ayudantes. Actualizar también el YAML del dashboard.

Validación estática y de plantillas local; pendiente de prueba visual en Home Assistant.

## 0.3.0 — Sin publicar

- Dashboard centrado en Bubble Card: Salón, Cocina y Dormitorio con pop-ups independientes.
- Subbotones de luz en portada para actuar sin abrir cada habitación.
- Selectores, estados, interruptores y sliders Bubble Card en las vistas generales.
- Variables de tema Bubble Card para fondos, bordes, iconos y pop-ups en claro/oscuro.
- Requiere Bubble Card >= 3.2.0 y Navbar Card; mantiene los ocho ayudantes y las URLs existentes.
- HACS solo actualiza el tema; copiar también el nuevo dashboard.

Validación estática local; pendiente de prueba funcional y visual en Home Assistant.

## 0.2.0 — Sin publicar

- Nueva paleta grafito/porcelana y acento azul pizarra en ambos modos.
- Variables de tema específicas para Navbar Card.
- Plantilla común de navegación: lateral desde 1024 px e inferior en móvil, con etiquetas y área segura.
- Cuatro vistas: Casa, Luces, Confort y Pruebas; espacio automático para la navbar.
- El dashboard ahora requiere Navbar Card; el tema sigue funcionando por separado.
- Los ayudantes existentes se conservan. HACS actualiza el tema; el dashboard debe actualizarse aparte.

Validación estática local; pendiente de prueba visual en Home Assistant.

## 0.1.0 — Preparada para publicar

- Tema Arrel con modos claro y oscuro, tonos piedra y acento verde.
- Dashboard de pruebas con vistas Casa y Laboratorio.
- Ocho ayudantes simulados sin conexión a dispositivos reales.
- Manifiesto para distribuir el tema con HACS desde GitHub.
- Instrucciones de instalación manual desde Forgejo y publicación de versiones.

Validación local de YAML y referencias de entidades. Pendiente de prueba visual en Home Assistant y de instalación real mediante HACS.
