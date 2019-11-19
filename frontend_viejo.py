# Standard library imports
from tkinter import *
from tkinter import ttk 
from tkinter import Menu
# Related third party imports - No hay
# Local application/library specific imports.
import backend
from os.path import isfile

# ---------- MULTIPLE COMPONENTS  ----------
# Some of the different Widgets : Button, Label,
# Canvas, Menu, Text, Scale, OptionMenu, Frame,
# CheckButton, LabelFrame, MenuButton, PanedWindow,
# Entry, ListBox, Message, RadioButton, ScrollBar,
# Bitmap, SpinBox, Image

# Variables compartidas con backend
db = ""
conexion = ""
cursor = ""
lista_mails = []
lista_nombres_de_usuario = []
lista_categorias = []

window = Tk()
window.resizable(False, False)

# Ventana
window.title("Psw tool")
menu = Menu(window)
ventana_menu = Menu(menu)
menu.add_cascade(label='Opciones', menu=ventana_menu)
window.config(menu=menu)
# Tabs de generar y base de datos
tab_control = ttk.Notebook(window)
principal = ttk.Frame(tab_control)
sqlite_base_de_datos = ttk.Frame(tab_control)
tab_control.add(principal, text='Generador')
tab_control.add(sqlite_base_de_datos, text='Base de datos')
tab_control.pack(expand=1, fill='both')
# Iconos
icono_clipboard = PhotoImage(file="iconos/intento.gif")


# Tab generar
# row = 0 | Generar contraseña
def set_texto_contrseña():
	contraseña = backend.generar_contraseña()
	contraseña_generada.delete(0, END)
	contraseña_generada.insert(0, contraseña)
	backend.copiar(contraseña)


boton_generar = Button(principal, text="GENERAR", command=set_texto_contrseña, width=8).grid(column=0, row=0, sticky=W)
contraseña_generada = Entry(principal, width=25)
contraseña_generada.grid(column=1, row=0)

boton_copiar_contraseña = Button(
	principal, width=15, image=icono_clipboard, command=lambda: backend.copiar(contraseña_generada.get())
)
boton_copiar_contraseña.image = icono_clipboard
boton_copiar_contraseña.grid(column=3, row=0)

# row = 1 | website
etiqueta_url = Label(principal, text="Pagina web:").grid(column=0, row=1, sticky=W)
url = Entry(principal, width=25)
url.grid(column=1, row=1)

# row = 2 | categorias
etiqueta_categoria = Label(principal, text="Categoria:").grid(column=0, row=2, sticky=W)

dropdown_categoria = ttk.Combobox(principal, width=25)
dropdown_categoria["values"] = lista_categorias
dropdown_categoria.grid(column=1, row=2)

# row = 3 | mail
etiqueta_mail = Label(principal, text="Mail:").grid(column=0, row=3, sticky=W)

dropdown_direccion_email = ttk.Combobox(principal, width=25)
dropdown_direccion_email["values"] = lista_mails
dropdown_direccion_email.grid(column=1, row=3)

boton_copiar_mail = Button(
	principal, width=15, image=icono_clipboard, command=lambda: backend.copiar(dropdown_direccion_email.get())
)
boton_copiar_mail.image = icono_clipboard
boton_copiar_mail.grid(column=3, row=3)
# row = 4 | nombre de usuario
etiqueta_username = Label(principal, text="Username:").grid(column=0, row=4, sticky=W)

dropdown_nombre_de_usuario = ttk.Combobox(principal, width=25)
dropdown_nombre_de_usuario["values"] = lista_nombres_de_usuario
dropdown_nombre_de_usuario.grid(column=1, row=4)

boton_copiar_usuario = Button(
	principal, width=15, image=icono_clipboard, command=lambda: backend.copiar(dropdown_nombre_de_usuario.get())
)
boton_copiar_usuario.image = icono_clipboard
boton_copiar_usuario.grid(column=3, row=4)


# row = 4 | guardar
def guardar_info():
	backend.crear_tabla_contraseñas(conexion, cursor)
	favicon = backend.descargar_favico(url.get())
	backend.guardar(
		conexion, cursor, dropdown_categoria.get(), favicon, url.get(), dropdown_direccion_email.get(),
		dropdown_nombre_de_usuario.get(), contraseña_generada.get()
	)

	url.delete('0', END)
	contraseña_generada.delete('0', END)


boton_guardar = Button(principal, text="SAVE", width=36, command=guardar_info)
boton_guardar.grid(row=5, columnspan=4)


def main():
	global db
	global conexion, cursor, lista_mails, lista_nombres_de_usuario, lista_categorias
	conexion, cursor = backend.conectar_db("contraseñas.db")
	
	if not isfile("./opciones.ini"):
		# preguntar_nombre_db()
		backend.generar_cfg()

	nombre_db, largo, mayus, minus, special, favicon = backend.obtener_cfg()

	# Sacamos las variables para la combo box
	lista_mails = backend.obtener_columna(cursor, "mail")
	lista_nombres_de_usuario = backend.obtener_columna(cursor, "username")
	lista_categorias = backend.obtener_columna(cursor, "categoria")
	
	# Seteamos los valores para la combo box
	dropdown_direccion_email["values"] = lista_mails
	dropdown_nombre_de_usuario["values"] = lista_nombres_de_usuario
	dropdown_categoria["values"] = lista_categorias
	
	window.grid_columnconfigure(1, weight=1)

	window.mainloop()


main()
