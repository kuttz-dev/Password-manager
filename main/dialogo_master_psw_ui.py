# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogo_master_psw.ui',
# licensing of 'dialogo_master_psw.ui' applies.
#
# Created: Sat Nov 30 04:15:25 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_dialogo_master_psw(object):
    def setupUi(self, dialogo_master_psw):
        dialogo_master_psw.setObjectName("dialogo_master_psw")
        dialogo_master_psw.resize(350, 157)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dialogo_master_psw.sizePolicy().hasHeightForWidth())
        dialogo_master_psw.setSizePolicy(sizePolicy)
        dialogo_master_psw.setMinimumSize(QtCore.QSize(350, 0))
        dialogo_master_psw.setMaximumSize(QtCore.QSize(350, 157))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/media/imagenes/main_frame.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dialogo_master_psw.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(dialogo_master_psw)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setContentsMargins(10, 5, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(dialogo_master_psw)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 80))
        self.label.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setScaledContents(False)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.hlayout_psw = QtWidgets.QHBoxLayout()
        self.hlayout_psw.setSpacing(4)
        self.hlayout_psw.setObjectName("hlayout_psw")
        self.input_master_psw = QtWidgets.QLineEdit(dialogo_master_psw)
        self.input_master_psw.setMinimumSize(QtCore.QSize(200, 22))
        self.input_master_psw.setMaximumSize(QtCore.QSize(16777215, 22))
        self.input_master_psw.setMouseTracking(False)
        self.input_master_psw.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_master_psw.setObjectName("input_master_psw")
        self.hlayout_psw.addWidget(self.input_master_psw)
        self.reveal_master_psw = QtWidgets.QPushButton(dialogo_master_psw)
        self.reveal_master_psw.setMinimumSize(QtCore.QSize(30, 25))
        self.reveal_master_psw.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.reveal_master_psw.setCursor(QtCore.Qt.PointingHandCursor)
        self.reveal_master_psw.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/media/iconografia/view.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reveal_master_psw.setIcon(icon1)
        self.reveal_master_psw.setObjectName("reveal_master_psw")
        self.hlayout_psw.addWidget(self.reveal_master_psw)
        self.hlayout_psw.setStretch(0, 90)
        self.hlayout_psw.setStretch(1, 5)
        self.verticalLayout.addLayout(self.hlayout_psw)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(dialogo_master_psw)
        self.buttonBox.setToolTip("")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 40)
        self.verticalLayout.setStretch(1, 40)
        self.verticalLayout.setStretch(2, 10)

        self.retranslateUi(dialogo_master_psw)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), dialogo_master_psw.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), dialogo_master_psw.reject)
        QtCore.QMetaObject.connectSlotsByName(dialogo_master_psw)

    def retranslateUi(self, dialogo_master_psw):
        dialogo_master_psw.setWindowTitle(QtWidgets.QApplication.translate("dialogo_master_psw", "Contraseña maestra", None, -1))
        self.label.setWhatsThis(QtWidgets.QApplication.translate("dialogo_master_psw", "Una vez que ingrese la contraseña maestra, la contraseña que completo será encriptada con esta y guardad en la base de datos. Se usará una única contraseña encriptada por base de datos.", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("dialogo_master_psw", "<html><head/><body><p><a name=\"docs-internal-guid-18a17bac-7fff-5834-6fea-9c7cb4c38644\"/><span style=\"color:#000000; background-color:transparent;\">E</span><span style=\"color:#000000; background-color:transparent;\">sta contraseña le dará acceso al resto, por favor considere severamente cual usará y recuerde no perderla, sino sus contraseñas serán irrecuperables.</span></p><p><span style=\" color:#000000; background-color:transparent;\">Contraseña maestra:</span></p></body></html>", None, -1))
        self.input_master_psw.setToolTip(QtWidgets.QApplication.translate("dialogo_master_psw", "(6 -16 caracteres)", None, -1))
        self.reveal_master_psw.setToolTip(QtWidgets.QApplication.translate("dialogo_master_psw", "Revelar u esconder contraseña", None, -1))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialogo_master_psw = QtWidgets.QDialog()
    ui = Ui_dialogo_master_psw()
    ui.setupUi(dialogo_master_psw)
    dialogo_master_psw.show()
    sys.exit(app.exec_())

