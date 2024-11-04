# Automatización de renovación de libros de la biblioteca de la UNS

Este proyecto automatiza la renovación de libros de la biblioteca de la Universidad Nacional del Sur mediante _Python_ utilizando _GitHub Actions_. Inicia sesión en el sistema de la biblioteca y renueva automáticamente los libros prestados.

## Configuración

### Variables de entorno

Para que el script funcione correctamente, es necesario configurar las siguientes variables de entorno:

- `USERNAME`: Nombre de usuario de la biblioteca (del tipo: `DNIXXXXXXXX`).
- `PASSWORD`: Contraseña de la biblioteca (en el caso de no tener se puede obtener de [Activación de cuenta](http://catalogo.uns.edu.ar/vufind/MyResearch/Activar?auth_method=ILS)).

### GitHub Actions

El script esta configurado para ejecutarse diariamente a las 00:00 hs, aunque esto es configurable en el archivo `.github/workflows/renovar-libro.yml`.
