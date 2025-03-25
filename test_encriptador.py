import hashlib
from encriptador import encriptar
from desencriptador import desencriptar

# Función para realizar las pruebas de encriptación y desencriptación


def test_encriptacion_desencriptacion():
    texto_original = "Este es un mensaje secreto"
    llave = "mi_llave_secreta"

    # Encriptar el texto
    texto_encriptado = encriptar(texto_original, llave)

    # Asegurarse de que el texto encriptado no sea el mismo que el original
    assert texto_encriptado != texto_original.encode('utf-8')

    # Desencriptar el texto
    texto_desencriptado = desencriptar(texto_encriptado, llave)

    # Asegurarse de que el texto desencriptado sea el mismo que el original
    assert texto_desencriptado == texto_original

# Prueba de que el hash genera una clave única y consistente


def test_generar_llave_con_hash():
    llave1 = "mi_llave_secreta"
    llave2 = "otra_llave"

    # Comprobamos que las llaves generadas con el hash sean de 32 bytes
    hash_llave1 = hashlib.sha256(llave1.encode('utf-8')).digest()
    hash_llave2 = hashlib.sha256(llave2.encode('utf-8')).digest()

    assert len(hash_llave1) == 32
    assert len(hash_llave2) == 32
    assert hash_llave1 != hash_llave2  # Las llaves generadas deben ser diferentes
