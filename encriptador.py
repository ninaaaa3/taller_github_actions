import sys
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64


def generar_llave_con_hash(llave):
    # Usamos SHA-256 para generar una llave de 32 bytes a partir de la llave proporcionada
    return hashlib.sha256(llave.encode('utf-8')).digest()


def encriptar(texto, llave):
    # Generar la llave a partir del hash SHA-256
    llave = generar_llave_con_hash(llave)

    # Crear el objeto AES en modo ECB
    cipher = AES.new(llave, AES.MODE_ECB)

    # Convertir el texto en bytes y realizar el padding
    texto_bytes = texto.encode('utf-8')
    texto_pad = pad(texto_bytes, AES.block_size)

    # Encriptar el texto
    texto_encriptado = cipher.encrypt(texto_pad)

    # Convertir el resultado a una cadena representable (en base64 para visualización)
    return base64.b64encode(texto_encriptado)


def main():
    if len(sys.argv) != 3:
        print("Uso: python encriptador.py <texto> <llave>")
        sys.exit(1)

    texto = sys.argv[1]
    llave = sys.argv[2]

    texto_encriptado = encriptar(texto, llave)
    print(f"Texto Encriptado: {texto_encriptado}")


if __name__ == "__main__":
    main()
