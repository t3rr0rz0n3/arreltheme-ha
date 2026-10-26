# Publicar arreltheme-ha

## Próxima versión: v0.6.5

Los tags locales llegan a v0.6.4. Tras probar y revisar los cambios, ejecuta desde la raíz del repositorio (no se ejecutan automáticamente):

```sh
git status --short
git diff --check
git add AGENTS.md cards/ dashboards/ themes/ README.md CHANGELOG.md PUBLISHING.md
git commit -m "Simplify room popup to basic controls"
git push origin HEAD
git tag -a v0.6.5 -m "Arrel 0.6.5"
git push origin v0.6.5
gh release create v0.6.5 --repo t3rr0rz0n3/arreltheme-ha --verify-tag --title "Arrel 0.6.5" --notes "Pop-up básico con luz, temperatura, puerta, ventana y presencia." --latest
```

Comprueba que `v0.6.5` no existe en el remoto antes de publicar; si existe, usa el siguiente número. No muevas tags publicados. Revisa la lista de archivos antes del commit para incluir solo cambios de esta entrega.

Prueba primero siguiendo [la guía de tarjetas](cards/README.md#probar-en-tu-dashboard-sin-publicar). No necesitas publicar una release para comprobar los YAML.

En cada entrega se facilitarán los comandos de `git add`, commit, push, tag y release correspondientes. HACS necesita la release en GitHub para ofrecer esa versión numerada. El tema y el dashboard se actualizan por separado.

Las instrucciones de Forgejo y espejos siguientes son opcionales.

Forgejo puede ser el repositorio principal. HACS solo admite repositorios públicos en GitHub: una URL de Forgejo no sirve como repositorio personalizado de HACS. El manifiesto incluido prepara el tema para un espejo opcional en GitHub; no configura ni publica ningún remoto.

## Primera subida a Forgejo

Crea `arreltheme-ha` vacío, sin README inicial. Desde esta carpeta, si todavía no es un repositorio Git:

```sh
git init -b main
git add README.md PUBLISHING.md CHANGELOG.md hacs.json themes dashboards packages
git commit -m "Prepare Arrel 0.1.0 prototype"
```

Añade la URL de clonación que muestre tu Forgejo (sustituye el ejemplo):

```sh
git remote add origin 'https://TU-FORGEJO/TU-USUARIO/arreltheme-ha.git'
git push -u origin main
```

Si ya tienes repositorio o remoto, utiliza los existentes; no repitas `git init` ni `git remote add`.

## Versión inicial: v0.1.0

Cuando quieras publicar el prototipo, crea una etiqueta anotada y súbela:

```sh
git tag -a v0.1.0 -m "Arrel 0.1.0"
git push origin v0.1.0
```

En Forgejo abre Releases → New Release, selecciona `v0.1.0`, titula la versión `Arrel 0.1.0` y copia sus notas desde CHANGELOG.md. La etiqueta fija el código; la release añade descripción y descargas. El archivo fuente de la release contiene el tema y la demo. Puedes adjuntar `themes/arrel.yaml` para facilitar la descarga del tema por separado; no es obligatorio.

La etiqueta no es obligatoria para instalar manualmente, pero sí recomendable para identificar lo que pruebas. No se ha creado ninguna etiqueta local: debe apuntar al commit final que subas.

## HACS mediante un espejo público en GitHub

1. Crea un repositorio público `arreltheme-ha` en GitHub.
2. Configura un push mirror en Forgejo hacia ese repositorio, o añade un segundo remoto y sube la rama y la etiqueta:

```sh
git remote add github 'https://github.com/TU-USUARIO/arreltheme-ha.git'
git push github main
git push github v0.1.0
```

3. Publica también una **release en GitHub**, asociada a `v0.1.0`, si quieres distribuir versiones numeradas mediante HACS. Un tag por sí solo no basta. No necesitas adjuntar ZIP ni YAML a la release para esta estructura de tema.
4. Añade la URL de **GitHub** en HACS → ⋮ → Repositorios personalizados, como tipo Theme.

El espejo Git sincroniza referencias y código; las releases de Forgejo no se convierten en releases de GitHub. Publica estas últimas por separado. Sin releases, HACS puede descargar desde la rama predeterminada.

## Siguientes versiones

1. Modifica el tema y prueba claro/oscuro en Home Assistant y tus pantallas.
2. Añade las notas a CHANGELOG.md: `0.1.1` para correcciones pequeñas; `0.2.0` para la siguiente iteración funcional.
3. Haz commit y push de los cambios.
4. Crea y sube un nuevo tag, por ejemplo `v0.1.1`, y publica su release. No muevas etiquetas ya publicadas.
5. Si usas HACS, sincroniza GitHub y publica allí también la release. Comprueba la actualización desde Home Assistant.

La versión viene del tag/release; no hay que añadir un campo `version` a hacs.json. HACS actualiza el tema, no el dashboard ni los ayudantes. La instalación automática de actualizaciones no está configurada.

## Referencias

- [Requisitos y versiones de HACS](https://hacs.dev/docs/publish/start/)
- [Estructura de un tema HACS](https://www.hacs.dev/docs/publish/theme/)
- [Guía de Forgejo](https://forgejo.org/docs/latest/user/)
