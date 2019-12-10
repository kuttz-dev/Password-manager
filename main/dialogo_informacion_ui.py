# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogo_informacion.ui',
# licensing of 'dialogo_informacion.ui' applies.
#
# Created: Tue Dec 10 11:16:14 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_dialogo_info(object):
    def setupUi(self, dialogo_info):
        dialogo_info.setObjectName("dialogo_info")
        dialogo_info.resize(437, 218)
        dialogo_info.setMinimumSize(QtCore.QSize(437, 0))
        dialogo_info.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/media/imagenes/main_frame.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dialogo_info.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(dialogo_info)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hlayout_principal = QtWidgets.QHBoxLayout()
        self.hlayout_principal.setSpacing(5)
        self.hlayout_principal.setObjectName("hlayout_principal")
        self.vlayout_perfil = QtWidgets.QVBoxLayout()
        self.vlayout_perfil.setObjectName("vlayout_perfil")
        self.etiqueta_imagen_perfil = QtWidgets.QLabel(dialogo_info)
        self.etiqueta_imagen_perfil.setMaximumSize(QtCore.QSize(96, 96))
        self.etiqueta_imagen_perfil.setText("")
        self.etiqueta_imagen_perfil.setPixmap(QtGui.QPixmap(":/media/imagenes/me.png"))
        self.etiqueta_imagen_perfil.setScaledContents(True)
        self.etiqueta_imagen_perfil.setObjectName("etiqueta_imagen_perfil")
        self.vlayout_perfil.addWidget(self.etiqueta_imagen_perfil)
        self.hlayout_botones = QtWidgets.QHBoxLayout()
        self.hlayout_botones.setObjectName("hlayout_botones")
        self.boton_steam = QtWidgets.QPushButton(dialogo_info)
        self.boton_steam.setMaximumSize(QtCore.QSize(30, 30))
        self.boton_steam.setCursor(QtCore.Qt.PointingHandCursor)
        self.boton_steam.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/media/branding/steam.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boton_steam.setIcon(icon1)
        self.boton_steam.setIconSize(QtCore.QSize(24, 24))
        self.boton_steam.setObjectName("boton_steam")
        self.hlayout_botones.addWidget(self.boton_steam)
        self.boton_discord = QtWidgets.QPushButton(dialogo_info)
        self.boton_discord.setMaximumSize(QtCore.QSize(30, 30))
        self.boton_discord.setCursor(QtCore.Qt.PointingHandCursor)
        self.boton_discord.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/media/branding/Discord-Logo-Black.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boton_discord.setIcon(icon2)
        self.boton_discord.setIconSize(QtCore.QSize(24, 24))
        self.boton_discord.setObjectName("boton_discord")
        self.hlayout_botones.addWidget(self.boton_discord)
        self.boton_github = QtWidgets.QPushButton(dialogo_info)
        self.boton_github.setMaximumSize(QtCore.QSize(30, 30))
        self.boton_github.setCursor(QtCore.Qt.PointingHandCursor)
        self.boton_github.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/media/branding/GitHub-Mark-64px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boton_github.setIcon(icon3)
        self.boton_github.setIconSize(QtCore.QSize(24, 24))
        self.boton_github.setObjectName("boton_github")
        self.hlayout_botones.addWidget(self.boton_github)
        self.vlayout_perfil.addLayout(self.hlayout_botones)
        self.hlayout_principal.addLayout(self.vlayout_perfil)
        self.vlayout_info = QtWidgets.QVBoxLayout()
        self.vlayout_info.setSpacing(5)
        self.vlayout_info.setObjectName("vlayout_info")
        self.etiqueta_titulo = QtWidgets.QLabel(dialogo_info)
        self.etiqueta_titulo.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.etiqueta_titulo.setFont(font)
        self.etiqueta_titulo.setObjectName("etiqueta_titulo")
        self.vlayout_info.addWidget(self.etiqueta_titulo)
        self.etiqueta_descripccion = QtWidgets.QLabel(dialogo_info)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.etiqueta_descripccion.sizePolicy().hasHeightForWidth())
        self.etiqueta_descripccion.setSizePolicy(sizePolicy)
        self.etiqueta_descripccion.setMaximumSize(QtCore.QSize(16777215, 150))
        self.etiqueta_descripccion.setWordWrap(True)
        self.etiqueta_descripccion.setObjectName("etiqueta_descripccion")
        self.vlayout_info.addWidget(self.etiqueta_descripccion)
        self.vlayout_info.setStretch(0, 10)
        self.vlayout_info.setStretch(1, 90)
        self.hlayout_principal.addLayout(self.vlayout_info)
        self.hlayout_principal.setStretch(0, 20)
        self.hlayout_principal.setStretch(1, 80)
        self.verticalLayout.addLayout(self.hlayout_principal)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(dialogo_info)
        self.buttonBox.setCursor(QtCore.Qt.PointingHandCursor)
        self.buttonBox.setAccessibleName("")
        self.buttonBox.setAccessibleDescription("")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.horizontalLayout.setStretch(0, 90)
        self.horizontalLayout.setStretch(1, 10)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 30)

        self.retranslateUi(dialogo_info)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), dialogo_info.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), dialogo_info.reject)
        QtCore.QMetaObject.connectSlotsByName(dialogo_info)

    def retranslateUi(self, dialogo_info):
        dialogo_info.setWindowTitle(QtWidgets.QApplication.translate("dialogo_info", "Información", None, -1))
        self.etiqueta_titulo.setText(QtWidgets.QApplication.translate("dialogo_info", "<html><head/><body><p>Psw-manager by Küttz</p></body></html>", None, -1))
        self.etiqueta_descripccion.setText(QtWidgets.QApplication.translate("dialogo_info", "<html><head/><body><p>Este proyecto es un trabajo en curso desarrollado únicamente por mi utilizando python. Seria genial si podes aportar a este proyecto revisando el código en github, comentando, encontrando errores, etc. Podes encontrarme en mi servidor de discord o a través de mi cuenta de steam dejando un comentario.</p><p>Los iconos pertenecen a Smashicons, Vignesh Oviyan, Those icons,  Iconnice y Freepik a traves de flaticon.com</p><p>Agradecimientos especiales a Roja</p></body></html>", None, -1))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialogo_info = QtWidgets.QDialog()
    ui = Ui_dialogo_info()
    ui.setupUi(dialogo_info)
    dialogo_info.show()
    sys.exit(app.exec_())

