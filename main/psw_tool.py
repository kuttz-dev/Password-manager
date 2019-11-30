import sys
from time import sleep

from PySide2.QtWidgets import QApplication, QMainWindow, QTabWidget, QLineEdit, QMessageBox, QInputDialog, QDialog  # QLineEdit para input_psw
from PySide2.QtCore import QFile
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel


from psw_tool_ui import Ui_TabWidget
from dialogo_informacion_ui import Ui_dialogo_info
from dialogo_master_psw_ui import Ui_dialogo_master_psw
import backend
import pswCrypto

class VentanaPrincipal(QTabWidget):

    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        self.registro = 0
        self.ui = Ui_TabWidget()
        self.ui.setupUi(self)

        # Procesos iniciales
        self.cargar_config()
        self.master_psw = None

        # Alertas
        self.alerta_config = QMessageBox(QMessageBox.Warning, "Problema con la configuración actual", "Existen dos posibilidades para este error:\n\n1. El archivo de configuración está dañando\n2. Usted tiene todas las opciones desmarcadas (el amor no cuenta)\n\nPara solucionarlo, borre el archivo de configuración ('opciones.ini'),\no marque alguna opción en la pestaña de configuración y guarde su selección\n")
        self.alerta_master_psw_mala = QMessageBox(QMessageBox.Warning, "Problema con la contraseña ingresada", "Por favor tome precauciones con la elección de la contraseña maestra.\nPara poder proseguir debe ingresar una contraseña con más de 5 y menos de 17 caracteres, o sino presione cancelar.")
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
        self.ui.boton_guardar_config.clicked.connect(self.guardar_config)  # connect button clicked with action  # boton guardar config
        self.ui.boton_info.clicked.connect(self.cargar_info)
        self.ui.boton_generar.clicked.connect(self.llamar_generar_contraseña)  # connect button clicked with action # Boton generar contrasñea
        self.ui.boton_guardar.clicked.connect(self.guardar_contraseña) # boton guardar data
        # Si presionan el boton revelar contraseña
        self.ui.reveal_psw.clicked.connect(self.mostrar_contraseña)
        self.alerta_master_psw.reveal_master_psw.clicked.connect(self.mostrar_contraseña_maestra)
            # Icono del boton revelar contraseña
        self.icon_not_view = QIcon()
        self.icon_not_view.addPixmap(QPixmap(":/media/iconografia/not_view.png"), QIcon.Normal, QIcon.Off)
        self.icon_view = QIcon()
        self.icon_view.addPixmap(QPixmap(":/media/iconografia/view.png"), QIcon.Normal, QIcon.Off)

        # Click en botones copiar # Otra manera de hacerlo: partial(self.llamar_copiar(n)) using functools.partial
        self.ui.cp1.clicked.connect(lambda: self.llamar_copiar(1))
        self.ui.cp2.clicked.connect(lambda: self.llamar_copiar(2))
        self.ui.cp3.clicked.connect(lambda: self.llamar_copiar(3))

        # Si se presiona la pestaña de configuracion
        #self.ui.tab_3.connect(self.cargar_config)

        # BASE DE DATOS
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("cuentas.db")
        # db.setPassword(str(self.master_pasw))
        self.conector = QSqlDatabase.database()
        self.query = QSqlQuery()
        self.query.exec_('CREATE TABLE IF NOT EXISTS passwords (id INTEGER PRIMARY KEY ASC, categoria TEXT, favicon BLOB, website TEXT, mail TEXT, username TEXT, contraseña BLOB);')
        self.query.exec_('CREATE TABLE IF NOT EXISTS maestra (id INTEGER PRIMARY KEY, muestra BLOB);')
        self.db.commit()
        self.model = QSqlTableModel()
        self.model.setTable('passwords')
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange) 
        #self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.ui.tabla_db.setModel(self.model)
        self.ui.tabla_db.setWindowTitle("Titulossas")
        #print(self.model.rowCount())


    def cargar_config(self):
        largo, mayus, minus, numeros, special, favicon = backend.obtener_cfg()   
        self.ui.spinBox_largo.setProperty("value", int(largo))
        self.ui.check_mayus.setChecked(backend.string2bool(mayus))
        self.ui.check_min.setChecked(backend.string2bool(minus))
        self.ui.check_numeros.setChecked(backend.string2bool(numeros))
        self.ui.check_caracteres.setChecked(backend.string2bool(special))
        self.ui.check_amor.setChecked(backend.string2bool(favicon))


    def guardar_config(self):
        hay_opcion_verdadera = False
        largo = self.ui.spinBox_largo.value()
        mayus = self.ui.check_mayus.checkState()
        minus = self.ui.check_min.checkState()
        numeros = self.ui.check_numeros.checkState()
        special = self.ui.check_caracteres.checkState()
        favicon = self.ui.check_amor.checkState()

        estado_checkeado = [mayus, minus, numeros, special, favicon]
        for i in range(len(estado_checkeado)):
            if str(estado_checkeado[i]) == "PySide2.QtCore.Qt.CheckState.Checked":
                if i != 4: #len de estado_checkeado - 1
                    hay_opcion_verdadera = True
                estado_checkeado[i] = True
            else:
                estado_checkeado[i] = False

        if hay_opcion_verdadera == False:
            return self.alerta_config.exec()

        backend.generar_cfg(largo, estado_checkeado[0], estado_checkeado[1], estado_checkeado[2], estado_checkeado[3], estado_checkeado[4])
        self.cargar_config()


    def cargar_info(self):
        return self.dialogo_info.exec()        


    def llamar_generar_contraseña(self):
        #  Primero obtenemos que tipo de contraseña quiere el usuario
        largo, mayus, minus, numeros, special, favicon = backend.obtener_cfg()
        mayus = backend.string2bool(mayus)
        minus = backend.string2bool(minus)
        numeros = backend.string2bool(numeros)
        special = backend.string2bool(special)

        if mayus is False and minus is False and numeros is False and special is False:
            self.alerta_config.exec()

        texto_contraseña = backend.generar_contraseña(int(largo), mayus, minus, numeros, special)
        self.ui.input_psw.setText(str(texto_contraseña)) # Ponemos la contraseña en la aplicacion


    def mostrar_contraseña(self):
        # Si esta en password a normal y viceversa
        if self.ui.input_psw.echoMode() == QLineEdit.EchoMode.Password:
            self.ui.reveal_psw.setIcon(self.icon_not_view)
            self.ui.input_psw.setEchoMode(QLineEdit.Normal)
        else:
            self.ui.reveal_psw.setIcon(self.icon_view)
            self.ui.input_psw.setEchoMode(QLineEdit.Password)


    def mostrar_contraseña_maestra(self, modoEcho = False):
        # Si no se cambio el estado va a estar en False y se va a usar el echoMode del input
        if modoEcho is False:
            modoEcho = self.alerta_master_psw.input_master_psw.echoMode()
        # Si esta en password a normal y viceversa
        if modoEcho == QLineEdit.EchoMode.Password:
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


    def guardar_contraseña(self):
        if self.master_psw is None:
            self.master_psw = self.pedir_contraseña_maestra()
        '''
        self.ui.input_psw.text()
        self.ui.comboBox_usuario.currentText()
        self.ui.comboBox_mail.currentText()
        self.ui.comboBox_categoria.currentText()
        self.ui.input_url.toPlainText()
        '''
        try:
            with open("contraseñas.txt") as file:
                file.append("""

                    """)
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)        


    def pedir_contraseña_maestra(self):
        self.dialogo_master_psw.exec()
        
        contraseña_maestra = self.alerta_master_psw.input_master_psw.text()
        # Borrarmos el texto porque no se borra solo, y lo volvemos secreto de nuevo
        self.alerta_master_psw.input_master_psw.setText("")
        self.mostrar_contraseña_maestra(QLineEdit.EchoMode.Normal)

        # Si le dio a cancelar
        if bool(self.dialogo_master_psw.result()) is False:
            return "Accion canelada"

        # Comprobamos que cumpla requisitos
        if contraseña_maestra == "" or len(contraseña_maestra) < 6 or len(contraseña_maestra) >16:
            self.alerta_master_psw_mala.exec()
            return self.pedir_contraseña_maestra()
        
        # Encriptacion
        key_contraseña_maestra = pswCrypto.generar_key(contraseña_maestra) # La convertimos en una key
        contraseña_maestra_encriptada = pswCrypto.encriptar(contraseña_maestra, key_contraseña_maestra) # Encriptamos la contraseña con la key
        # Verificacion
        # Obtenemos la muestra guardada en la db
        muestra_db = backend.obtener_muestra_db()
        # Si no habia guardamos una nueva con esta contraseña maestra
        if muestra_db is None:
            nueva_muestra = backend.generar_muestra(key_contraseña_maestra)
            print(nueva_muestra)
            self.master_query = QSqlQuery()
            self.master_query.exec_("INSERT INTO maestra (id, muestra) VALUES(1, ?)" (nueva_muestra))
            print(self.db.lastError())
            self.db.commit()

            # RETURN QUE?
        else:
            # Ahora si verificamos
            print(type(muestra_db), type(key_contraseña_maestra)) 
            psw_correcta = backend.verificar_key(muestra_db, key_contraseña_maestra)
            print(psw_correcta)
    

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = VentanaPrincipal()
    window.show()

    sys.exit(app.exec_())
