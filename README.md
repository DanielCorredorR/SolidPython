# SolidPython

Ejemplos de los principios SOLID en Python.

El proyecto conserva las carpetas originales como referencia y agrega nuevas
carpetas con el sufijo `_solid` para mostrar versiones refactorizadas que
aplican cada principio.

## Principios refactorizados

### SRP - Principio de responsabilidad unica

Carpeta original: `srp/`

Carpeta refactorizada: `srp_solid/`

La clase original `FileManager` mezclaba operaciones de lectura, escritura,
compresion y descompresion de archivos. En la version refactorizada se separan
las responsabilidades:

- `FileManager`: se encarga solo de leer y escribir archivos.
- `ZipFileManager`: se encarga solo de comprimir y descomprimir archivos.

De esta forma, cada clase tiene una unica razon para cambiar.

### OCP - Principio de abierto/cerrado

Carpeta original: `ocp/`

Carpeta refactorizada: `ocp_solid/`

La clase original `Shape` dependia de condicionales para calcular el area de
cada figura. Si se necesitaba agregar una nueva figura, habia que modificar la
clase existente.

En la version refactorizada se define una abstraccion `Shape` y cada figura
implementa su propio calculo de area:

- `Rectangle`: calcula el area de un rectangulo.
- `Circle`: calcula el area de un circulo.
- `AreaCalculator`: trabaja con cualquier objeto que cumpla el contrato de
  `Shape`.

Asi se pueden agregar nuevas figuras creando nuevas clases, sin modificar las
clases ya existentes.
