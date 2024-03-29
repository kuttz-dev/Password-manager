from os import remove
from os.path import isfile
import re
import string
import sqlite3

import configparser
from urllib import request
from webbrowser import open as web_open
from random import choice
from pyperclip import copy
from cryptography.fernet import InvalidToken

from pswCrypto import generar_key, encriptar, descifrar


# Base de datos
# ~~~~~~~~~~~~~
def obtener_muestra_db():
    conexion = sqlite3.connect("cuentas.db")
    cursor = conexion.cursor()    
    muestra_db = cursor.execute('SELECT muestra FROM maestra WHERE id = 1')
    muestra_db = muestra_db.fetchone()
    # Devolvemos
    if muestra_db is None:
        return None
    else:
        return muestra_db[0]


# Funcionalidad general
# ~~~~~~~~~~~~~
def string2bool(s):
    return s == "True"


def abrir_link(url):
    web_open(url)


def generar_contraseña(largo: int=13, mayus=True, minus=True, numeros=True, special=True):
        caracteres = ""
        contraseña = ""
        expresion = []
        
        if mayus is False and minus is False and numeros is False and special is False:
            return ""

        if mayus is True:
            expresion.append("[ABCDFGHIJKLMNÑOPQRSTUVWXYZ]")
            caracteres += string.ascii_uppercase
        if minus is True:
            expresion.append("[abcdfghijklmnñopqrstuvwxyz]")
            caracteres += string.ascii_lowercase
        if numeros is True:
            expresion.append("[0123456789]")
            caracteres += string.digits
        if special is True:
            expresion.append("[!%@#_-]")
            caracteres += "!%@#_-"  # string.digits = !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

        for i in range(largo):
            contraseña += choice(caracteres)
        extender_iteracion = [0]
        for iteracion in extender_iteracion:
            for i in expresion:
                hay_caracter = bool(re.search(i, contraseña))

                if hay_caracter is False:
                    extender_iteracion.append(1)
                    # Caracter a cambiar
                    elegido = choice(contraseña)

                    # Asi no se eligen los corchetes
                    i = i.replace("[", "")
                    i = i.replace("]", "")

                    # Elegimos el caracter del grupo por el que hay que cambiarlo
                    remplazo = choice(i)
                    contraseña = contraseña.replace(elegido, remplazo, 1)
        
        return contraseña


def descargar_favico(url):
    if url == "":
        return None
        
    nombre = re.search(r"(www\.)?(?P<nombre_pagina>[\w\d\-@:%._+~#=]{2,256})(?P<terminacion>\.\w{2,6})", url)
    if nombre is None:
        return None

    link = nombre.group("nombre_pagina") + nombre.group("terminacion")
    nombre = nombre.group("nombre_pagina")
    # Para poder guardarlo
    if "." in nombre:
        nombre = nombre.replace(".", "-")
    # Lugar donde se guarda el archivo    
    icono = "media/favicons/{}.ico".format(nombre)
    # Conseguimos el ico con la API    
    try:
        favicon_a_descargar = request.urlopen("http://favicongrabber.com/api/grab/{}".format(link)).read()
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
        return None

    favicon_a_descargar = re.search(r'("src":)?."(?P<fav_icon>[\w\-@:%._+~#=/]+\.ico)"', str(favicon_a_descargar))
   
    if favicon_a_descargar is None:
            """ Hacer un archivo de registro
            try:
                raise SyntaxError("El siguiente url no tuvo resultados regex, url: {}".format(url))
            except Exception as e:
                template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                message = template.format(type(e).__name__, e.args)
                print(message)
            """
            return None

    favicon_a_descargar = favicon_a_descargar.group("fav_icon")
    # Lo descargamos y guardamos
    with open(icono, "wb") as imagen:
        try:
            imagen.write(request.urlopen(favicon_a_descargar).read())
            # Devolvemos el directorio donde se guarda la imagen
            # print(url)
            return icono

        except Exception as e:
            print("Error guardando el favcion de url: {} | Error: {}".format(url, e))
            try:
                imagen.close()
                borrar_favico(icono)
                raise Exception("El url si era valido, pero no se consiguio icono")
            except:
                print("Algo salio demasaido mal")
    print(url)


# Si no se pudo descargar la imagen, hay que borrar el archivo vacio
def borrar_favico(archivo):
    try:
        return remove(archivo)
    except Exception as e:
        print(e)


def generar_cfg(largo: int = 13, mayus=True, minus=True, numeros=True, special=True, icono=True):
    cfg = configparser.ConfigParser()
    cfg['OPCIONES'] = {'largo': largo,
                       'mayus': mayus,
                       'minus': minus,
                       'numeros': numeros,
                       'special': special,
                       'icono': icono
                       }

    with open("opciones.ini", "w") as configfile:
        cfg.write(configfile)


def obtener_cfg():
    if not isfile("./opciones.ini"):
        generar_cfg()
    if not isfile("./cuentas.db"):
        pass  # crear_tabla_contraseñas(conectar_db("cuentas.db"))
    try:
        cfg = configparser.ConfigParser()
        cfg.read('opciones.ini')
        largo = cfg['OPCIONES']['largo']
        mayus = cfg['OPCIONES']['mayus']
        minus = cfg['OPCIONES']['minus']
        numeros = cfg['OPCIONES']['numeros']
        special = cfg['OPCIONES']['special']
        icono = cfg['OPCIONES']['icono']

    except configparser.MissingSectionHeaderError:
        generar_cfg()
        return obtener_cfg()
    except KeyError:
        generar_cfg()
        return obtener_cfg()
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        return print(message)

    try:
        largo = int(largo)

    except ValueError:
        generar_cfg(13, mayus, minus, numeros, special, icono)
        return obtener_cfg()

    if int(largo) < 4 or int(largo) > 16:
        generar_cfg(13, mayus, minus, numeros, special, icono)
        return obtener_cfg()    

    return largo, mayus, minus, numeros, special, icono


def copiar(text):
    copy(text)


# Encripatdo
# ~~~~~~~~~~
def generar_muestra(key):
    muestra = encriptar("muestra para probar las key", key)
    return muestra


def verificar_key(muestra, key):
    """
    muestra = descifrar(muestra, key)
    print(type(muestra))
    if muestra == "An exception of type InvalidToken occurred.":
        return False
    elif muestra is not None:
        return True"""
    try:
        descifrar(muestra, key)  # muestra = descifrar(muestra, key)
        return True
    except InvalidToken:
        return False
