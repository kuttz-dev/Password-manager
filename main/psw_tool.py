import sys

from PySide2.QtWidgets import QApplication, QTabWidget, QLineEdit, QMessageBox, QDialog, QHeaderView, QComboBox
from PySide2.QtCore import QFile, QByteArray, Qt
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlField

from psw_tool_ui import Ui_TabWidget
from dialogo_informacion_ui import Ui_dialogo_info
from dialogo_master_psw_ui import Ui_dialogo_master_psw

import backend
import pswCrypto
import pswItemDelegate


class VentanaPrincipal(QTabWidget):

	def __init__(self):
		super(VentanaPrincipal, self).__init__()
		self.ui = Ui_TabWidget()
		self.ui.setupUi(self)

		# DB
		self.db = QSqlDatabase.addDatabase("QSQLITE")
		self.db.setDatabaseName("cuentas.db")
		self.conector = QSqlDatabase.database()
		self.general_query = QSqlQuery()
		self.organizar_db()
		# Querys para psw_tool
		self.master_query = QSqlQuery()
		self.save_query = QSqlQuery()
		self.passwords_query_retrieve = QSqlQuery()
		self.passwords_query_write = QSqlQuery()
		self.popular = QSqlQuery()
		self.comboBoxes_query_categoria = QSqlQuery()
		self.comboBoxes_query_mail = QSqlQuery()
		self.comboBoxes_query_usuario = QSqlQuery()
		self.verificar_columna_contrasenas = QSqlQuery()
		self.filtro = QSqlQuery()
		# Querys para pswItemDelegate
		self.all_data = QSqlQuery()
		#  BASE DE DATOS en UI
		self.model = QSqlTableModel()  # pswItemDelegate.CustomSqlModel()
		self.organizar_tabla_ui()
		self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)  # Va aca abajo por self.model.setTable('passwords')
		# Para cuando se cambian datos
		self.model.dataChanged.connect(self.celdas_cambiadas)

		# Filtro DB
		# .connect(lambda: self.
		self.tabBarClicked.connect(self.actualizar_tabs)
		# Iconos DB en UI
		self.icon_seguridad = QIcon()
		self.icon_seguridad.addPixmap(QPixmap(":/media/iconografia/locked.png"), QIcon.Normal, QIcon.Off)
		self.icon_desbloqueado = QIcon()
		self.icon_desbloqueado.addPixmap(QPixmap(":/media/iconografia/unlocked.png"), QIcon.Normal, QIcon.Off)
		self.icon_editar = QIcon()
		self.icon_editar.addPixmap(QPixmap(":/media/iconografia/pencil.png"), QIcon.Normal, QIcon.Off)
		self.icon_guardar = QIcon()
		self.icon_guardar.addPixmap(QPixmap(":/media/iconografia/broken-pencil.png"), QIcon.Normal, QIcon.Off)

		# Procesos iniciales
		self.cargar_config()
		self.master_key = None
		self.seguridad_alterada = False
		self.candado = "cerrado"
		self.modo_boton_editar_guardar = "editar"
		self.contrasenas_nuevas = {}
		self.edits = {}
		self.revisar_columna_contrasenas()
		self.cargar_opciones_combo_boxes()
		# Alertas
		# Iconos para las alertas sin UI
		self.icon_ventana = QIcon()
		self.icon_ventana.addPixmap(QPixmap(":/media/imagenes/main_frame.png"), QIcon.Normal, QIcon.Off)
		self.alerta_config = QMessageBox(QMessageBox.Warning,
										"Problema con la configuración actual",
										"Existen dos posibilidades para este error:\n\n1. El archivo de configuración está dañando\n2. Usted tiene todas las opciones desmarcadas (el amor no cuenta)\n\nPara solucionarlo, borre el archivo de configuración ('opciones.ini'),\no marque alguna opción en la pestaña de configuración y guarde su selección\n"
										)
		self.alerta_master_psw_mala = QMessageBox(QMessageBox.Warning,
												"Problema con la contraseña ingresada",
												"Por favor tome precauciones con la elección de la contraseña maestra.\nPara poder proseguir debe ingresar una contraseña con más de 5 y menos de 17 caracteres, o sino presione cancelar."
												)
		self.alerta_master_psw_incorrecta = QMessageBox(QMessageBox.Warning,
														"Problema con la contraseña ingresada",
														"La contraseña que ingresaste es incorrecta"
														)
		self.alerta_guardado_exitoso = QMessageBox(QMessageBox.Information, "Información guardada",
													"Toda la información que ingresaste se guardó con exito."
												)
		self.alerta_config.setWindowIcon(self.icon_ventana)
		self.alerta_master_psw_mala.setWindowIcon(self.icon_ventana)
		self.alerta_master_psw_incorrecta.setWindowIcon(self.icon_ventana)
		self.alerta_guardado_exitoso.setWindowIcon(self.icon_ventana)
		# Alertas con su propia UI
		# Dialog info
		self.dialogo_info = QDialog()
		self.info_app = Ui_dialogo_info()
		self.info_app.setupUi(self.dialogo_info)
		# Alerta master psw
		self.dialogo_master_psw = QDialog()
		self.alerta_master_psw = Ui_dialogo_master_psw()
		self.alerta_master_psw.setupUi(self.dialogo_master_psw)

		# Botones
		self.ui.boton_guardar_config.clicked.connect(self.guardar_config)
		self.ui.boton_info.clicked.connect(self.cargar_info)
		self.ui.boton_generar.clicked.connect(self.llamar_generar_contrasena)  # Boton generar contrasñea
		self.ui.boton_guardar.clicked.connect(self.guardar_contrasena)  # boton guardar data
		# Si presionan el boton revelar contraseña
		self.ui.reveal_psw.clicked.connect(self.mostrar_contrasena)
		self.alerta_master_psw.reveal_master_psw.clicked.connect(self.mostrar_contrasena_maestra)
		# Icono del boton revelar contraseña
		self.icon_not_view = QIcon()
		self.icon_not_view.addPixmap(QPixmap(":/media/iconografia/not_view.png"), QIcon.Normal, QIcon.Off)
		self.icon_view = QIcon()
		self.icon_view.addPixmap(QPixmap(":/media/iconografia/view.png"), QIcon.Normal, QIcon.Off)
		# Click en botones copiar # Otra manera de hacerlo: partial(self.llamar_copiar(n)) using functools.partial
		self.ui.cp1.clicked.connect(lambda: self.llamar_copiar(1))
		self.ui.cp2.clicked.connect(lambda: self.llamar_copiar(2))
		self.ui.cp3.clicked.connect(lambda: self.llamar_copiar(3))
		# Botones DB
		self.ui.boton_filtro.clicked.connect(lambda: self.filtrar())
		self.ui.boton_editar.clicked.connect(lambda: self.gestor_boton_editar_guardar())
		self.ui.boton_seguridad.clicked.connect(lambda: self.mostrar_contrasenas())
		# Botones Info
		self.info_app.boton_steam.clicked.connect(lambda: backend.abrir_link("https://steamcommunity.com/id/JosephKm"))
		self.info_app.boton_discord.clicked.connect(lambda: backend.abrir_link("https://discord.gg/wYuXPQS"))
		self.info_app.boton_github.clicked.connect(
			lambda: backend.abrir_link("https://github.com/kuttz-dev/Password-manager"))
		# Si se presiona la pestaña de configuracion
		# self.ui.tab_3.connect(self.cargar_config)
		# SETEAR COMBOBOXES
		self.ui.comboBox_usuario.setInsertPolicy(QComboBox.InsertAlphabetically)
		self.ui.comboBox_mail.setInsertPolicy(QComboBox.InsertAlphabetically)
		self.ui.comboBox_categoria.setInsertPolicy(QComboBox.InsertAlphabetically)
		self.ui.comboBox_usuario.setDuplicatesEnabled(False)
		self.ui.comboBox_mail.setDuplicatesEnabled(False)
		self.ui.comboBox_categoria.setDuplicatesEnabled(False)
		self.ui.comboBox_usuario.clearEditText()
		self.ui.comboBox_mail.clearEditText()
		self.ui.comboBox_categoria.clearEditText()

	# print(self.model.flags(self.model.index(0,2)))

	def organizar_db(self):
		self.general_query.exec_(
			'CREATE TABLE IF NOT EXISTS passwords (id INTEGER PRIMARY KEY ASC, categoria TEXT, icono BLOB, servicio TEXT, mail TEXT, usuario TEXT, contraseña_encriptada BLOB);'
		)
		self.general_query.exec_(
			'CREATE TABLE IF NOT EXISTS maestra (id INTEGER PRIMARY KEY, muestra BLOB);'
		)
		self.general_query.exec_(
			'DELETE FROM passwords WHERE usuario = "" AND mail = "" AND contraseña_encriptada = ""'
		)
		self.db.commit()

	def borrar_columna_contrasenas(self):
		self.general_query.exec_(
			'DROP TABLE IF EXISTS temporal'
		)
		self.general_query.exec_(
			'CREATE TABLE temporal (id INTEGER PRIMARY KEY ASC, categoria TEXT, icono BLOB, servicio TEXT, mail TEXT, usuario TEXT, contraseña_encriptada BLOB);'
		)
		self.popular.exec_(
			'INSERT INTO temporal(id, categoria, icono, servicio, mail, usuario, contraseña_encriptada) SELECT id, categoria, icono, servicio, mail, usuario, contraseña_encriptada FROM passwords'
		)
		self.db.commit()
		self.general_query.exec_(
			'DROP TABLE IF EXISTS passwords'
		)
		self.popular.exec_(
			'ALTER TABLE temporal RENAME TO passwords'
		)
		self.general_query.exec_(
			'DROP TABLE IF EXISTS temporal'
		)
		self.db.commit()

	def cargar_config(self):
		largo, mayus, minus, numeros, special, icono = backend.obtener_cfg()
		self.ui.spinBox_largo.setProperty("value", int(largo))
		self.ui.check_mayus.setChecked(backend.string2bool(mayus))
		self.ui.check_min.setChecked(backend.string2bool(minus))
		self.ui.check_numeros.setChecked(backend.string2bool(numeros))
		self.ui.check_caracteres.setChecked(backend.string2bool(special))
		self.ui.check_amor.setChecked(backend.string2bool(icono))

	def guardar_config(self):
		hay_opcion_verdadera = False
		largo = self.ui.spinBox_largo.value()
		mayus = self.ui.check_mayus.checkState()
		minus = self.ui.check_min.checkState()
		numeros = self.ui.check_numeros.checkState()
		special = self.ui.check_caracteres.checkState()
		icono = self.ui.check_amor.checkState()

		estado_checkeado = [mayus, minus, numeros, special, icono]
		for i in range(len(estado_checkeado)):
			if str(estado_checkeado[i]) == "PySide2.QtCore.Qt.CheckState.Checked":
				if i != 4:  # len de estado_checkeado - 1
					hay_opcion_verdadera = True
				estado_checkeado[i] = True
			else:
				estado_checkeado[i] = False

		if hay_opcion_verdadera is False:
			return self.alerta_config.exec()

		backend.generar_cfg(largo,
							estado_checkeado[0],
							estado_checkeado[1],
							estado_checkeado[2],
							estado_checkeado[3],
							estado_checkeado[4]
							)

		self.cargar_config()

	def cargar_info(self):
		return self.dialogo_info.exec()

	def llamar_generar_contrasena(self):
		#  Primero obtenemos que tipo de contraseña quiere el usuario
		largo, mayus, minus, numeros, special, icono = backend.obtener_cfg()
		mayus = backend.string2bool(mayus)
		minus = backend.string2bool(minus)
		numeros = backend.string2bool(numeros)
		special = backend.string2bool(special)

		if mayus is False and minus is False and numeros is False and special is False:
			self.alerta_config.exec()

		texto_contrasena = backend.generar_contraseña(int(largo), mayus, minus, numeros, special)
		self.ui.input_psw.setText(str(texto_contrasena))  # Ponemos la contraseña en la aplicacion

	def mostrar_contrasena(self):
		# Si esta en password a normal y viceversa
		if self.ui.input_psw.echoMode() == QLineEdit.EchoMode.Password:
			self.ui.reveal_psw.setIcon(self.icon_not_view)
			self.ui.input_psw.setEchoMode(QLineEdit.Normal)
		else:
			self.ui.reveal_psw.setIcon(self.icon_view)
			self.ui.input_psw.setEchoMode(QLineEdit.Password)

	def mostrar_contrasena_maestra(self, modo_echo=False):
		# Si no se cambio el estado va a estar en False y se va a usar el echoMode del input
		if modo_echo is False:
			modo_echo = self.alerta_master_psw.input_master_psw.echoMode()
		# Si esta en password a normal y viceversa
		if modo_echo == QLineEdit.EchoMode.Password:
			self.alerta_master_psw.reveal_master_psw.setIcon(self.icon_not_view)
			self.alerta_master_psw.input_master_psw.setEchoMode(QLineEdit.Normal)
		else:
			self.alerta_master_psw.reveal_master_psw.setIcon(self.icon_view)
			self.alerta_master_psw.input_master_psw.setEchoMode(QLineEdit.Password)

	def llamar_copiar(self, numero_boton):
		if numero_boton == 1:
			backend.copiar(str(self.ui.input_psw.text()))
		if numero_boton == 2:
			backend.copiar(str(self.ui.comboBox_usuario.currentText()))
		if numero_boton == 3:
			backend.copiar(str(self.ui.comboBox_mail.currentText()))

	def preparar_favicon(self, url):
		try:
			archivo_ico = backend.descargar_favico(url)
		except Exception:  # Si lo que se ingreso era un link pero no se consigui favicon
			with open("media/favicons/domain.ico") as ico:
				return QByteArray(ico.read())
		# Si no se consiguio la imagen
		if archivo_ico is None:
			return None
		with open(archivo_ico, "rb") as ico:
			return QByteArray(ico.read())

	def guardar_contrasena(self):
		# self.ui.comboBox_usuario.currentText() / self.ui.comboBox_mail.currentText()
		# self.ui.comboBox_categoria.currentText() / self.ui.input_url.text()
		# self.ui.input_psw.text()

		if self.master_key is None:
			try:
				self.master_key = self.pedir_contrasena_maestra()
			except Exception:
				return
		if self.ui.input_psw.text() != "":
			contrasena_ingresada_encriptada = QByteArray(pswCrypto.encriptar(self.ui.input_psw.text(), self.master_key))
		else:
			contrasena_ingresada_encriptada = ""

		try:
			fav_icon = self.preparar_favicon(self.ui.input_url.text())

			self.save_query.prepare(
				'INSERT INTO passwords (categoria, icono, servicio, mail, usuario, contraseña_encriptada) VALUES(?,?,?,?,?,?)'
			)
			self.save_query.addBindValue(self.ui.comboBox_categoria.currentText())
			self.save_query.addBindValue(fav_icon)
			self.save_query.addBindValue(self.ui.input_url.text())
			self.save_query.addBindValue(self.ui.comboBox_mail.currentText())
			self.save_query.addBindValue(self.ui.comboBox_usuario.currentText())
			self.save_query.addBindValue(contrasena_ingresada_encriptada)
			self.save_query.exec_()
			self.db.commit()
			self.model.select()
			self.ui.tabla_db.resizeColumnsToContents()
			self.cargar_opciones_combo_boxes()
			return self.alerta_guardado_exitoso.exec()

		except Exception as ex:
			template = "An exception of type {0} occurred. Arguments:\n{1!r}"
			message = template.format(type(ex).__name__, ex.args)
			print(message)

	def pedir_contrasena_maestra(self):
		self.dialogo_master_psw.exec()

		contrasena_maestra = self.alerta_master_psw.input_master_psw.text()
		# Borrarmos el texto porque no se borra solo, y lo volvemos secreto de nuevo
		self.alerta_master_psw.input_master_psw.setText("")
		self.mostrar_contrasena_maestra(QLineEdit.EchoMode.Normal)

		# Si le dio a cancelar
		if bool(self.dialogo_master_psw.result()) is False:
			raise Exception("Accion canelada")

		# Comprobamos que cumpla requisitos
		if contrasena_maestra == "" or len(contrasena_maestra) < 6 or len(contrasena_maestra) > 16:
			self.alerta_master_psw_mala.exec()
			return self.pedir_contraseña_maestra()

		# Encriptacion
		key_contrasena_maestra = pswCrypto.generar_key(contrasena_maestra)  # La convertimos en una key
		# Verificacion
		# Obtenemos la muestra guardada en la db
		muestra_db = backend.obtener_muestra_db()
		# Si no habia guardamos una nueva con esta contraseña maestra
		if muestra_db is None:
			array = QByteArray(backend.generar_muestra(key_contrasena_maestra))
			self.master_query.prepare("INSERT INTO maestra (id, muestra) VALUES(1, ?)")
			self.master_query.addBindValue(array)
			self.master_query.exec_()

			return key_contrasena_maestra

		else:
			# Ahora si verificamos
			psw_correcta = backend.verificar_key(muestra_db, key_contrasena_maestra)
			if psw_correcta is True:
				return key_contrasena_maestra
			else:
				self.alerta_master_psw_incorrecta.exec_()
				raise Exception("Contraseña maestra incorrecta")
		# return self.master_key = contrasena_maestra

	def filtrar(self):
		if self.ui.input_filtro.text() == "":
			self.model.setFilter("")
			return self.model.select()
		else:
			self.model.setFilter(
				"{} LIKE '{}%'".format(self.ui.combobox_filtro.currentText().lower(), self.ui.input_filtro.text())
			)
			return self.model.select()

	def mostrar_contrasenas(self):
		if self.master_key is None:
			try:
				self.master_key = self.pedir_contrasena_maestra()
			except Exception:
				return

		if self.candado == "abierto":  # Si esta abierto
			self.borrar_columna_contrasenas()
			self.ui.combobox_filtro.removeItem(4)
			self.organizar_tabla_ui()
			self.ui.boton_seguridad.setIcon(self.icon_seguridad)
			self.candado = "cerrado"  # lo cerramos
			return

		else:  # Si estaba cerrado
			self.candado = "abierto"  # lo abrimos
		# y se abre asi:
		self.ui.boton_seguridad.setIcon(self.icon_desbloqueado)
		# Conseguimos las contraseñas encriptadas
		self.passwords_query_retrieve.exec_('SELECT id, contraseña_encriptada FROM passwords')
		# Creamos una columna para las contraseñas descifradas
		self.general_query.exec_('ALTER TABLE passwords ADD contraseña TEXT')
		self.db.commit()
		# Para cada contraseña
		while self.passwords_query_retrieve.next():
			# Si se guardo un texto vacio
			contrasena_descifrada = self.passwords_query_retrieve.value(1)
			if type(contrasena_descifrada) != str:
				contrasena_descifrada = pswCrypto.descifrar(contrasena_descifrada.data(), self.master_key)

			self.passwords_query_write.prepare('UPDATE passwords SET contraseña = ? WHERE id= ?')
			self.passwords_query_write.addBindValue(contrasena_descifrada)
			self.passwords_query_write.addBindValue(self.passwords_query_retrieve.value(0))
			self.passwords_query_write.exec_()
		self.ui.combobox_filtro.addItem("Contraseña")
		self.organizar_tabla_ui()  # Las hacemos visibles el la tabla

	def actualizar_tabs(self, index):
		if index == 0:
			self.cargar_opciones_combo_boxes()
		if index == 1 and self.ui.boton_seguridad.isEnabled() is True:
			self.organizar_tabla_ui()
		elif index == 2:
			self.cargar_config()

	def organizar_tabla_ui(self):
		self.model.setTable('passwords')
		self.model.setSort(1, Qt.AscendingOrder)
		self.model.select()
		self.ui.tabla_db.setModel(self.model)
		self.ui.tabla_db.setItemDelegateForColumn(2, pswItemDelegate.ImageDelegate(self.ui.tabla_db))
		self.ui.tabla_db.hideColumn(0)  # Escondemos id
		self.ui.tabla_db.hideColumn(6)  # Escondemos las contraseñas encriptadas
		self.ui.tabla_db.setWindowTitle("Lista de cuentas")
		# Tamaño columnas
		self.ui.tabla_db.resizeColumnsToContents()
		self.ui.tabla_db.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
		# self.ui.tabla_db.horizontalHeader().setSectionsClickable(False)
		self.ui.tabla_db.verticalHeader().setVisible(False)
		# self.ui.tabla_db.horizontalHeader().setSortIndicator(2, Qt.AscendingOrder)
		self.ui.tabla_db.setSortingEnabled(True)

	def cargar_opciones_combo_boxes(self):
		a = self.ui.comboBox_categoria.currentText()
		b = self.ui.comboBox_mail.currentText()
		c = self.ui.comboBox_usuario.currentText()

		self.comboBoxes_query_categoria.exec_(
			'SELECT DISTINCT categoria FROM passwords'
		)
		self.comboBoxes_query_mail.exec_(
			'SELECT DISTINCT mail FROM passwords'
		)
		self.comboBoxes_query_usuario.exec_(
			'SELECT DISTINCT usuario FROM passwords'
		)
		# Borramos las anteriores
		self.ui.comboBox_usuario.clear()
		self.ui.comboBox_mail.clear()
		self.ui.comboBox_categoria.clear()
		# Cargamos las nuevas
		while self.comboBoxes_query_categoria.next():
			if self.comboBoxes_query_categoria.value(0) == "" or self.comboBoxes_query_categoria.value(0) is None:
				continue
			self.ui.comboBox_categoria.addItem(self.comboBoxes_query_categoria.value(0))

		while self.comboBoxes_query_mail.next():
			if self.comboBoxes_query_mail.value(0) == "" or self.comboBoxes_query_mail.value(0) is None:
				continue
			self.ui.comboBox_mail.addItem(self.comboBoxes_query_mail.value(0))

		while self.comboBoxes_query_usuario.next():
			if self.comboBoxes_query_usuario.value(0) == "" or self.comboBoxes_query_usuario.value(0) is None:
				continue
			self.ui.comboBox_usuario.addItem(self.comboBoxes_query_usuario.value(0))
		self.ui.comboBox_categoria.setCurrentText(a)
		self.ui.comboBox_mail.setCurrentText(b)
		self.ui.comboBox_usuario.setCurrentText(c)

	def revisar_columna_contrasenas(self, borrar=True):
		existe = self.verificar_columna_contrasenas.exec_('SELECT contraseña FROM passwords LIMIT 1')
		if existe is True and borrar is True:
			self.verificar_columna_contrasenas.finish()
			self.borrar_columna_contrasenas()
			return self.organizar_tabla_ui()

		elif existe is True:
			return "Existe"

	def gestor_boton_editar_guardar(self):
		if self.modo_boton_editar_guardar == "editar":
			try:
				self.editar_tabla_ui()
			except Exception:
				return
			self.modo_boton_editar_guardar = "guardar"  # Cambiamos al proximo modo
			return self.ui.boton_editar.setIcon(self.icon_guardar)

		elif self.modo_boton_editar_guardar == "guardar":
			self.borrar_columna_contrasenas()
			self.organizar_tabla_ui()
			self.candado = "cerrado"
			self.ui.boton_seguridad.setDisabled(False)
			self.ui.boton_seguridad.setIcon(self.icon_seguridad)
			self.ui.boton_editar.setIcon(self.icon_editar)
			self.modo_boton_editar_guardar = "editar"  # Cambiamos al proximo modo
			return

	def editar_tabla_ui(self):
		if self.master_key is None:
			try:
				self.master_key = self.pedir_contrasena_maestra()
			except Exception:
				raise Exception("No se pudo conseguir master key")

		self.ui.boton_seguridad.setDisabled(True)
		if self.candado == "cerrado":
			self.mostrar_contrasenas()

	def celdas_cambiadas(self, top_left, bottom_right):
		if self.modo_boton_editar_guardar == "editar":
			return
		else:
			if top_left.column() == 7:

				contrasena_editada_encriptada = ""
				if self.model.record(top_left.row()).value('contraseña') != "":
					contrasena_editada_encriptada = QByteArray(
						pswCrypto.encriptar(self.model.record(top_left.row()).value('contraseña'), self.master_key))

				casilla_editada = QSqlField("contraseña_encriptada")
				casilla_editada.setValue(contrasena_editada_encriptada)
				valores_fila = self.model.record(top_left.row())
				valores_fila.replace(6, casilla_editada)
				return self.model.updateRowInTable(top_left.row(), valores_fila)
			else:
				self.model.updateRowInTable(top_left.row(), self.model.record(top_left.row()))
				return self.db.commit()


if __name__ == "__main__":
	app = QApplication(sys.argv)

	window = VentanaPrincipal()
	window.show()

	sys.exit(app.exec_())
