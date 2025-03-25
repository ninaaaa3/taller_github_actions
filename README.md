# Instrucciones para Ejecutar el Sistema de Encriptación AES

## Contenido del archivo ZIP

El archivo ZIP contiene los siguientes componentes:
- `encriptador.py`: Programa para encriptar texto
- `desencriptador.py`: Programa para desencriptar texto
- `test_encriptacion.py`: Pruebas automatizadas del sistema
- `README.md`: Este archivo de instrucciones

## Requisitos Previos

Antes de ejecutar los programas, asegúrese de tener instalado:

1. Python 3.x
2. Las siguientes bibliotecas:
   ```bash
   pip install pycryptodome pytest
   ```

## Instrucciones de Ejecución

### 1. Extraer el archivo ZIP
Extraiga todos los archivos del ZIP en una carpeta de su elección.

### 2. Encriptar un texto
Para encriptar un texto, ejecute el siguiente comando desde la terminal:
```bash
python encriptador.py Mensaje a encriptar clave_secreta
```
Ejemplo:
```bash
python encriptador.py Este es un mensaje confidencial mi_clave_2024
```
El programa mostrará el texto encriptado en formato Base64.

### 3. Desencriptar un texto
Para desencriptar un texto previamente encriptado, ejecute:
```bash
python desencriptador.py texto_encriptado_en_base64 clave_secreta
```
Ejemplo:
```bash
python desencriptador.py VGhpcyBpcyBqdXN0IGFuIGV4YW1wbGU= mi_clave_2024
```
El programa mostrará el texto original.

### 4. Ejecutar las pruebas
Para verificar que el sistema funciona correctamente, ejecute:
```bash
pytest test_encriptacion.py -v
```
Debería ver un resultado indicando que todas las pruebas han pasado exitosamente.

## Notas Importantes

- Asegúrese de recordar la clave secreta utilizada para encriptar, ya que será necesaria para desencriptar.
- El texto encriptado en Base64 puede contener caracteres especiales. Para evitar problemas al usar el desencriptador, se recomienda copiar y pegar el texto exactamente como se muestra.
- Si va a encriptar texto con caracteres especiales o acentos, asegúrese de que su terminal esté configurada para usar UTF-8.
