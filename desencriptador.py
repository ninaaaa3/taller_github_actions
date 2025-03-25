import sys
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

def generar_llave_con_hash(llave):
    # Usamos SHA-256 para generar una llave de 32 bytes a partir de la llave proporcionada
    return hashlib.sha256(llave.encode('utf-8')).digest()

def desencriptar(texto_encriptado, llave):
    # Generar la llave a partir del hash SHA-256
    llave = generar_llave_con_hash(llave)
    
    # Crear el objeto AES en modo ECB
    cipher = AES.new(llave, AES.MODE_ECB)
    
    # Decodificar el texto encriptado desde base64
    texto_encriptado_bytes = base64.b64decode(texto_encriptado)
    
    # Desencriptar el texto
    texto_desencriptado = unpad(cipher.decrypt(texto_encriptado_bytes), AES.block_size)
    
    # Convertir los bytes a texto plano
    return texto_desencriptado.decode('utf-8')

def main():
    if len(sys.argv) != 3:
        print("Uso: python desencriptador.py <texto_encriptado> <llave>")
        sys.exit(1)
    
    texto_encriptado = sys.argv[1]
    llave = sys.argv[2]
    
    texto_desencriptado = desencriptar(texto_encriptado, llave)
    print(f"Texto Desencriptado: {texto_desencriptado}")

if __name__ == "__main__":
    main()
