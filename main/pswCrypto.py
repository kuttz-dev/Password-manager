import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet, InvalidToken
import timeit
from PySide2.QtCore import QByteArray

def generar_key(contraseña):
	contraseña = contraseña.encode()  # Convert to type bytes

	salt = b"\xb8M\xce\x94\xbd\xfa\x0f\x1e\x04\r\x83\xea\xa1\xbbD'"  # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
	kdf = PBKDF2HMAC(
	    algorithm=hashes.SHA256(),
	    length=32,
	    salt=salt,
	    iterations=100000,
	    backend=default_backend()
	)

	key = base64.urlsafe_b64encode(kdf.derive(contraseña))  # Can only use kdf once
	return key


def encriptar(mensaje, key):
	mensaje = mensaje.encode()

	f = Fernet(key)
	mensaje_encriptado = f.encrypt(mensaje)

	return mensaje_encriptado


def descifrar(mensaje_encriptado, key):
	f = Fernet(key)
	mensaje_descifrado = f.decrypt(mensaje_encriptado)
	mensaje_descifrado = mensaje_descifrado.decode("utf-8")
	return mensaje_descifrado
	
#	except InvalidToken as ex:
#		template = "An exception of type {0} occurred. Arguments:\n{1!r}"
#		message = template.format(type(ex).__name__, ex.args)
#		print(message)
		
