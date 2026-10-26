# Diseño de Arrel

Cuando se modifique el CSS o el tema, aplicar y comprobar la coherencia del cambio en las tarjetas nativas de Home Assistant, Bubble Card y Navbar Card. Estos son los componentes visuales que el usuario utiliza actualmente. Revisar claro/oscuro y móvil/escritorio; conservar los colores de estado que comunican información.

Mantener sincronizados los estilos de Navbar del dashboard de ejemplo y de `cards/arrel-navbar-paste.yaml`. Los ejemplos deben poder pegarse y editarse directamente en el dashboard, sin build. Documentar cuándo hay que actualizar el tema y cuándo copiar estilos a tarjetas existentes; no afirmar que actualizar HACS modifica su YAML.

Al entregar una versión, facilitar comandos de Git y pasos de prueba directa en Home Assistant. No ejecutar publicación salvo petición explícita. No afirmar validación visual sin probar en una instancia real.
