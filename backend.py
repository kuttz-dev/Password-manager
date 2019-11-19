from pswCrypto import generar_key, encriptar, descifrar
from urllib import request
from random import choice
from os import remove
from os.path import isfile
import re
import string
import sqlite3
import configparser
from pyperclip import copy

# Base de datos
# ~~~~~~~~~~~~~
def conectar_db(db):
    try:
        conexion = sqlite3.connect(db)
        cursor = conexion.cursor()
        return conexion, cursor
    except Error as e:
        print(e)


def crear_tabla_contraseñas(conexion, cursor):
    # if favicon is True:
    try:
        cursor.execute('CREATE TABLE IF NOT EXISTS passwords (id INTEGER PRIMARY KEY, categoria TEXT, favicon TEXT, website TEXT, mail TEXT, username TEXT, contraseña BLOB);')
        conexion.commit()

    except sqlite3.OperationalError as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
    '''
    elif favicon is False:
        try:
            cursor.execute('CREATE TABLE passwords (id INTEGER PRIMARY KEY, categoria TEXT, website TEXT, mail TEXT, username TEXT, contraseña BLOB);')
            conexion.commit()

        except sqlite3.OperationalError as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
    '''


def checkear_tabla(cursor, db):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='{}';".format(db))


def guardar(conexion, cursor, categoria, favicon, url, mail, usuario, contraseña):
    try:
        cursor.execute('INSERT INTO passwords(categoria, favicon, website, mail, username, contraseña) VALUES(?, ?, ?, ?, ?)', (categoria, favicon, url, mail, usuario, contraseña))
        conexion.commit()
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)

def obtener_columna(cursor, columna):
    cursor.execute("SELECT {} FROM passwords".format(columna))
    entradas = cursor.fetchall()
    resultados = [x[0] for x in entradas]
    resultados = list(filter(None, resultados))

    return resultados

# Otra seccion
# ~~~~~~~~~~~~~
class BackEnd:
    def __init__(self, nombre_db):
        self.conexion = sqlite3.connect(self.nombre_db)
        self.cursor = self.conexion.cursor()


class BaseDeDatos(BackEnd):
    # Nombre, conexion y cursor, y opciones


    def crear_tabla_contraseñas(self, conexion, cursor):
        # if favicon is True:
        try:
            self.cursor.execute(
                'CREATE TABLE IF NOT EXISTS passwords (id INTEGER PRIMARY KEY, categoria TEXT, favicon TEXT, website TEXT, mail TEXT, username TEXT, contraseña BLOB);')
            self.conexion.commit()

        except sqlite3.OperationalError as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
        '''
        elif favicon is False:
            try:
                cursor.execute('CREATE TABLE passwords (id INTEGER PRIMARY KEY, categoria TEXT, website TEXT, mail TEXT, username TEXT, contraseña BLOB);')
                conexion.commit()

            except sqlite3.OperationalError as ex:
                template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                message = template.format(type(ex).__name__, ex.args)
                print(message)
        '''


def string2bool(s):
    return s == "True"


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
        
    nombre = re.search(r"(www\.)?(?P<nombre_pagina>[\w\d\-@:%\._\+~#=]{2,256})(?P<terminacion>\.\w{2,6})", url)
    link = nombre.group("nombre_pagina") + nombre.group("terminacion")
    nombre = nombre.group("nombre_pagina")
    # Para poder guardarlo
    if "." in nombre:
        nombre = nombre.replace(".", "-")
    # Lugar donde se guarda el archivo    
    favicon = "imagenes/{}.ico".format(nombre)
    # Conseguimos el ico con la API    
    try:
        favicon_a_descargar = request.urlopen("http://favicongrabber.com/api/grab/{}".format(link)).read()
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
        return None

    favicon_a_descargar = re.search(r'("src":)?."(?P<fav_icon>[\w\-@:%\._\+~#=\/]+\.ico)"', str(favicon_a_descargar))
   
    if favicon_a_descargar is None:
        try:
            raise SyntaxError("El siguiente url no tuvo resultados regex, url: {}".format(url))
        except Exception as e:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(e).__name__, e.args)
            print(message)
            return None
            # Hacer un archivo de registro

    favicon_a_descargar = favicon_a_descargar.group("fav_icon")
    # Lo descargamos y guardamos
    with open(favicon, "wb") as imagen:
        try:
            imagen.write(request.urlopen(favicon_a_descargar).read())
            # Devolvemos el directorio donde se guarda la imagen
            print(url)
            return favicon

        except Exception as e:
            print("Error guardando el favcion de url: {} | Error: {}".format(url, e))
            try:
                imagen.close()
                borrar_favico(favicon)
                return None
            except:
                print("Algo salio demasaido mal")
    print(url)

# Si no se pudo descargar la imagen, hay que borrar el archivo vacio
def borrar_favico(archivo):
    try:
        return remove(archivo)
    except Exception as e:
        print(e)


def generar_cfg(largo: int =13, mayus=True, minus=True, numeros=True, special=True, favicon=True):
    cfg = configparser.ConfigParser()
    cfg['OPCIONES'] = {'largo': largo,
                      'mayus': mayus,
                      'minus': minus,
                      'numeros': numeros,
                      'special': special,
                      'favicon': favicon}

    with open("opciones.ini", "w") as configfile:
        cfg.write(configfile)


def obtener_cfg():
    if not isfile("./opciones.ini"):
        generar_cfg()
    if not isfile("./cuentas.db"):
        conectar_db("cuentas.db")
    try:
        cfg = configparser.ConfigParser()
        cfg.read('opciones.ini')
        largo = cfg['OPCIONES']['largo']
        mayus = cfg['OPCIONES']['mayus']
        minus = cfg['OPCIONES']['minus']
        numeros = cfg['OPCIONES']['numeros']
        special = cfg['OPCIONES']['special']
        favicon = cfg['OPCIONES']['favicon']
        return largo, mayus, minus, numeros, special, favicon

    except Exception as e:
        print(e)


def editar_cfg(categoria, argumento, valor):
    cfg = configparser.ConfigParser()
    valor = cfg[categoria][argumento] 
    with open("opciones.ini", "w") as configfile:
        cfg.write(configfile)

def copiar(text):
    copy(text)

# Encripatdo
# ~~~~~~~~~~
def generar_muestra(key):
    muestra = encriptar("muestra para probar las key", key)
    return muestra


def verificar_key(muestra, key):
    muestra = descifrar(muestra, key)
    if muestra == "An exception of type InvalidToken occurred.":
        return False
    elif muestra is not None:
        return True

