# Historial de cambios

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
