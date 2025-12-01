# bio-sql

## 📦 Instalación de dependencias

Este proyecto utiliza un entorno virtual (`.venv`) y un archivo `requirements.txt` para asegurar reproducibilidad.

### 1. Activar entorno virtual
En la raíz del proyecto (`bio-sql-clinico`):

```bash
source .venv/bin/activate

## 2. Instalar dependencias desde requirements.txt
Con el entorno activado:

```bash
pip install -r requirements.txt
Esto instalará todas las librerías necesarias con las versiones exactas.

## 3. Agregar nuevas dependencias
Si instalás una librería adicional con `pip install`, recordá actualizar `requirements.txt`:

### Opción manual (recomendada)
Consultar versión instalada:

```bash
pip show nombre_libreria
Agregarla en `requirements.txt` con `==versión`.

### Opción automática (rápida)
Sobrescribir el archivo con todas las dependencias actuales:

```bash
pip freeze > requirements.txt
## 4. Verificación
En un entorno limpio, podés probar que todo funciona ejecutando:

```bash
pip install -r requirements.txt
Si no hay errores, tu archivo está correcto y reproducible.