# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'psw_tool.ui',
# licensing of 'psw_tool.ui' applies.
#
# Created: Mon Dec  9 00:52:52 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        TabWidget.setObjectName("TabWidget")
        TabWidget.setWindowModality(QtCore.Qt.NonModal)
        TabWidget.setEnabled(True)
        TabWidget.resize(437, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TabWidget.sizePolicy().hasHeightForWidth())
        TabWidget.setSizePolicy(sizePolicy)
        TabWidget.setMinimumSize(QtCore.QSize(437, 200))
        TabWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        TabWidget.setCursor(QtCore.Qt.ArrowCursor)
        TabWidget.setFocusPolicy(QtCore.Qt.WheelFocus)
        TabWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/media/imagenes/main_frame.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TabWidget.setWindowIcon(icon)
        TabWidget.setToolTip("")
        TabWidget.setToolTipDuration(1)
        TabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        TabWidget.setAutoFillBackground(False)
        TabWidget.setStyleSheet("")
        TabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        TabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        TabWidget.setUsesScrollButtons(True)
        TabWidget.setDocumentMode(False)
        TabWidget.setTabsClosable(False)
        TabWidget.setMovable(False)
        TabWidget.setTabBarAutoHide(False)
        self.tab_1 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_1.sizePolicy().hasHeightForWidth())
        self.tab_1.setSizePolicy(sizePolicy)
        self.tab_1.setMaximumSize(QtCore.QSize(16777215, 171))
        self.tab_1.setCursor(QtCore.Qt.ArrowCursor)
        self.tab_1.setToolTip("")
        self.tab_1.setStatusTip("")
        self.tab_1.setWhatsThis("")
        self.tab_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tab_1.setAutoFillBackground(False)
        self.tab_1.setObjectName("tab_1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.hlayout_psw = QtWidgets.QHBoxLayout()
        self.hlayout_psw.setSpacing(4)
        self.hlayout_psw.setObjectName("hlayout_psw")
        self.boton_generar = QtWidgets.QPushButton(self.tab_1)
        self.boton_generar.setMinimumSize(QtCore.QSize(0, 30))
        self.boton_generar.setCursor(QtCore.Qt.PointingHandCursor)
        self.boton_generar.setObjectName("boton_generar")
        self.hlayout_psw.addWidget(self.boton_generar)
        self.input_psw = QtWidgets.QLineEdit(self.tab_1)
        self.input_psw.setMinimumSize(QtCore.QSize(230, 22))
        self.input_psw.setMaximumSize(QtCore.QSize(16777215, 22))
        self.input_psw.setMouseTracking(False)
        self.input_psw.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_psw.setObjectName("input_psw")
        self.hlayout_psw.addWidget(self.input_psw)
        self.reveal_psw = QtWidgets.QPushButton(self.tab_1)
        self.reveal_psw.setMinimumSize(QtCore.QSize(30, 25))
        self.reveal_psw.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.reveal_psw.setCursor(QtCore.Qt.PointingHandCursor)
        self.reveal_psw.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/media/iconografia/view.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reveal_psw.setIcon(icon1)
        self.reveal_psw.setObjectName("reveal_psw")
        self.hlayout_psw.addWidget(self.reveal_psw)
        self.cp1 = QtWidgets.QPushButton(self.tab_1)
        self.cp1.setMinimumSize(QtCore.QSize(30, 25))
        self.cp1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cp1.setCursor(QtCore.Qt.PointingHandCursor)
        self.cp1.setMouseTracking(False)
        self.cp1.setAcceptDrops(False)
        self.cp1.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/media/iconografia/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cp1.setIcon(icon2)
        self.cp1.setObjectName("cp1")
        self.hlayout_psw.addWidget(self.cp1)
        self.hlayout_psw.setStretch(0, 10)
        self.hlayout_psw.setStretch(1, 80)
        self.hlayout_psw.setStretch(2, 5)
        self.hlayout_psw.setStretch(3, 5)
        self.verticalLayout_2.addLayout(self.hlayout_psw)
        self.hlayout_usuario_mail = QtWidgets.QHBoxLayout()
        self.hlayout_usuario_mail.setContentsMargins(-1, -1, 0, -1)
        self.hlayout_usuario_mail.setObjectName("hlayout_usuario_mail")
        self.vlayout_usuario = QtWidgets.QVBoxLayout()
        self.vlayout_usuario.setSpacing(1)
        self.vlayout_usuario.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.vlayout_usuario.setObjectName("vlayout_usuario")
        self.etiqueta_usuario = QtWidgets.QLabel(self.tab_1)
        self.etiqueta_usuario.setMinimumSize(QtCore.QSize(60, 0))
        self.etiqueta_usuario.setMaximumSize(QtCore.QSize(16777215, 20))
        self.etiqueta_usuario.setObjectName("etiqueta_usuario")
        self.vlayout_usuario.addWidget(self.etiqueta_usuario)
        self.hlayout_usuario = QtWidgets.QHBoxLayout()
        self.hlayout_usuario.setObjectName("hlayout_usuario")
        self.comboBox_usuario = QtWidgets.QComboBox(self.tab_1)
        self.comboBox_usuario.setMaximumSize(QtCore.QSize(16777215, 20))
        self.comboBox_usuario.setCursor(QtCore.Qt.PointingHandCursor)
        self.comboBox_usuario.setEditable(True)
        self.comboBox_usuario.setObjectName("comboBox_usuario")
        self.hlayout_usuario.addWidget(self.comboBox_usuario)
        self.cp2 = QtWidgets.QPushButton(self.tab_1)
        self.cp2.setMinimumSize(QtCore.QSize(30, 20))
        self.cp2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cp2.setCursor(QtCore.Qt.PointingHandCursor)
        self.cp2.setMouseTracking(False)
        self.cp2.setAcceptDrops(False)
        self.cp2.setText("")
        self.cp2.setIcon(icon2)
        self.cp2.setObjectName("cp2")
        self.hlayout_usuario.addWidget(self.cp2)
        self.hlayout_usuario.setStretch(0, 90)
        self.hlayout_usuario.setStretch(1, 10)
        self.vlayout_usuario.addLayout(self.hlayout_usuario)
        self.hlayout_usuario_mail.addLayout(self.vlayout_usuario)
        self.vlayout_mail = QtWidgets.QVBoxLayout()
        self.vlayout_mail.setSpacing(1)
        self.vlayout_mail.setObjectName("vlayout_mail")
        self.etiqueta_mail = QtWidgets.QLabel(self.tab_1)
        self.etiqueta_mail.setMinimumSize(QtCore.QSize(60, 0))
        self.etiqueta_mail.setMaximumSize(QtCore.QSize(16777215, 20))
        self.etiqueta_mail.setObjectName("etiqueta_mail")
        self.vlayout_mail.addWidget(self.etiqueta_mail)
        self.hlayout_mail = QtWidgets.QHBoxLayout()
        self.hlayout_mail.setObjectName("hlayout_mail")
        self.comboBox_mail = QtWidgets.QComboBox(self.tab_1)
        self.comboBox_mail.setMinimumSize(QtCore.QSize(0, 20))
        self.comboBox_mail.setMaximumSize(QtCore.QSize(16777215, 20))
        self.comboBox_mail.setCursor(QtCore.Qt.PointingHandCursor)
        self.comboBox_mail.setEditable(True)
        self.comboBox_mail.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.comboBox_mail.setObjectName("comboBox_mail")
        self.hlayout_mail.addWidget(self.comboBox_mail)
        self.cp3 = QtWidgets.QPushButton(self.tab_1)
        self.cp3.setMinimumSize(QtCore.QSize(30, 20))
        self.cp3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cp3.setCursor(QtCore.Qt.PointingHandCursor)
        self.cp3.setMouseTracking(False)
        self.cp3.setAcceptDrops(False)
        self.cp3.setText("")
        self.cp3.setIcon(icon2)
        self.cp3.setObjectName("cp3")
        self.hlayout_mail.addWidget(self.cp3)
        self.hlayout_mail.setStretch(0, 90)
        self.hlayout_mail.setStretch(1, 10)
        self.vlayout_mail.addLayout(self.hlayout_mail)
        self.hlayout_usuario_mail.addLayout(self.vlayout_mail)
        self.verticalLayout_2.addLayout(self.hlayout_usuario_mail)
        self.hlayout_categoria_url = QtWidgets.QHBoxLayout()
        self.hlayout_categoria_url.setContentsMargins(-1, -1, 0, -1)
        self.hlayout_categoria_url.setObjectName("hlayout_categoria_url")
        self.vlayout_categoria = QtWidgets.QVBoxLayout()
        self.vlayout_categoria.setSpacing(1)
        self.vlayout_categoria.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.vlayout_categoria.setObjectName("vlayout_categoria")
        self.etiqueta_categoria = QtWidgets.QLabel(self.tab_1)
        self.etiqueta_categoria.setMinimumSize(QtCore.QSize(60, 0))
        self.etiqueta_categoria.setMaximumSize(QtCore.QSize(16777215, 20))
        self.etiqueta_categoria.setObjectName("etiqueta_categoria")
        self.vlayout_categoria.addWidget(self.etiqueta_categoria)
        self.comboBox_categoria = QtWidgets.QComboBox(self.tab_1)
        self.comboBox_categoria.setMinimumSize(QtCore.QSize(0, 20))
        self.comboBox_categoria.setMaximumSize(QtCore.QSize(16777215, 20))
        self.comboBox_categoria.setCursor(QtCore.Qt.PointingHandCursor)
        self.comboBox_categoria.setEditable(True)
        self.comboBox_categoria.setCurrentText("")
        self.comboBox_categoria.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.comboBox_categoria.setDuplicatesEnabled(False)
        self.comboBox_categoria.setObjectName("comboBox_categoria")
        self.vlayout_categoria.addWidget(self.comboBox_categoria)
        self.vlayout_categoria.setStretch(0, 50)
        self.vlayout_categoria.setStretch(1, 50)
        self.hlayout_categoria_url.addLayout(self.vlayout_categoria)
        self.vlayout_url = QtWidgets.QVBoxLayout()
        self.vlayout_url.setSpacing(1)
        self.vlayout_url.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.vlayout_url.setObjectName("vlayout_url")
        self.etiqueta_url = QtWidgets.QLabel(self.tab_1)
        self.etiqueta_url.setMinimumSize(QtCore.QSize(60, 0))
        self.etiqueta_url.setMaximumSize(QtCore.QSize(16777215, 20))
        self.etiqueta_url.setObjectName("etiqueta_url")
        self.vlayout_url.addWidget(self.etiqueta_url)
        self.input_url = QtWidgets.QLineEdit(self.tab_1)
        self.input_url.setMinimumSize(QtCore.QSize(0, 20))
        self.input_url.setMaximumSize(QtCore.QSize(16777215, 20))
        self.input_url.setMouseTracking(False)
        self.input_url.setInputMethodHints(QtCore.Qt.ImhNone)
        self.input_url.setObjectName("input_url")
        self.vlayout_url.addWidget(self.input_url)
        self.vlayout_url.setStretch(0, 50)
        self.hlayout_categoria_url.addLayout(self.vlayout_url)
        self.hlayout_categoria_url.setStretch(0, 50)
        self.hlayout_categoria_url.setStretch(1, 50)
        self.verticalLayout_2.addLayout(self.hlayout_categoria_url)
        self.boton_guardar = QtWidgets.QPushButton(self.tab_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boton_guardar.sizePolicy().hasHeightForWidth())
        self.boton_guardar.setSizePolicy(sizePolicy)
        self.boton_guardar.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.boton_guardar.setFont(font)
        self.boton_guardar.setCursor(QtCore.Qt.PointingHandCursor)
        self.boton_guardar.setAutoDefault(False)
        self.boton_guardar.setDefault(False)
        self.boton_guardar.setObjectName("boton_guardar")
        self.verticalLayout_2.addWidget(self.boton_guardar)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/media/iconografia/authorization.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TabWidget.addTab(self.tab_1, icon3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setEnabled(True)
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.boton_seguridad = QtWidgets.QPushButton(self.tab_2)
        self.boton_seguridad.setCursor(QtCore.Qt.PointingHandCursor)
        self.boton_seguridad.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/media/iconografia/locked.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boton_seguridad.setIcon(icon4)
        self.boton_seguridad.setObjectName("boton_seguridad")
        self.horizontalLayout.addWidget(self.boton_seguridad)
        self.combobox_filtro = QtWidgets.QComboBox(self.tab_2)
        self.combobox_filtro.setCursor(QtCore.Qt.PointingHandCursor)
        self.combobox_filtro.setObjectName("combobox_filtro")
        self.combobox_filtro.addItem("")
        self.combobox_filtro.addItem("")
        self.combobox_filtro.addItem("")
        self.combobox_filtro.addItem("")
        self.horizontalLayout.addWidget(self.combobox_filtro)
        self.input_filtro = QtWidgets.QLineEdit(self.tab_2)
        self.input_filtro.setObjectName("input_filtro")
        self.horizontalLayout.addWidget(self.input_filtro)
        self.boton_filtro = QtWidgets.QPushButton(self.tab_2)
        self.boton_filtro.setCursor(QtCore.Qt.PointingHandCursor)
        self.boton_filtro.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/media/iconografia/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boton_filtro.setIcon(icon5)
        self.boton_filtro.setAutoDefault(False)
        self.boton_filtro.setDefault(False)
        self.boton_filtro.setFlat(False)
        self.boton_filtro.setObjectName("boton_filtro")
        self.horizontalLayout.addWidget(self.boton_filtro)
        self.boton_editar = QtWidgets.QPushButton(self.tab_2)
        self.boton_editar.setCursor(QtCore.Qt.PointingHandCursor)
        self.boton_editar.setStatusTip("")
        self.boton_editar.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/media/iconografia/document.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boton_editar.setIcon(icon6)
        self.boton_editar.setObjectName("boton_editar")
        self.horizontalLayout.addWidget(self.boton_editar)
        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(1, 30)
        self.horizontalLayout.setStretch(2, 60)
        self.horizontalLayout.setStretch(3, 5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tabla_db = QtWidgets.QTableView(self.tab_2)
        self.tabla_db.setObjectName("tabla_db")
        self.verticalLayout.addWidget(self.tabla_db)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/media/iconografia/database.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TabWidget.addTab(self.tab_2, icon7, "")
        self.tab_3 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_3.sizePolicy().hasHeightForWidth())
        self.tab_3.setSizePolicy(sizePolicy)
        self.tab_3.setMaximumSize(QtCore.QSize(16777215, 171))
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.grupo_opciones_psw = QtWidgets.QGroupBox(self.tab_3)
        self.grupo_opciones_psw.setObjectName("grupo_opciones_psw")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.grupo_opciones_psw)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.check_caracteres = QtWidgets.QCheckBox(self.grupo_opciones_psw)
        self.check_caracteres.setCursor(QtCore.Qt.PointingHandCursor)
        self.check_caracteres.setChecked(True)
        self.check_caracteres.setObjectName("check_caracteres")
        self.gridLayout_2.addWidget(self.check_caracteres, 3, 0, 1, 3)
        self.boton_guardar_config = QtWidgets.QPushButton(self.grupo_opciones_psw)
        self.boton_guardar_config.setMinimumSize(QtCore.QSize(80, 0))
        self.boton_guardar_config.setCursor(QtCore.Qt.PointingHandCursor)
        self.boton_guardar_config.setObjectName("boton_guardar_config")
        self.gridLayout_2.addWidget(self.boton_guardar_config, 4, 4, 1, 1)
        self.check_min = QtWidgets.QCheckBox(self.grupo_opciones_psw)
        self.check_min.setMinimumSize(QtCore.QSize(0, 0))
        self.check_min.setMaximumSize(QtCore.QSize(75, 16777215))
        self.check_min.setCursor(QtCore.Qt.PointingHandCursor)
        self.check_min.setToolTip("")
        self.check_min.setChecked(True)
        self.check_min.setObjectName("check_min")
        self.gridLayout_2.addWidget(self.check_min, 2, 0, 1, 1)
        self.etiqueta_largo = QtWidgets.QLabel(self.grupo_opciones_psw)
        self.etiqueta_largo.setMinimumSize(QtCore.QSize(120, 20))
        self.etiqueta_largo.setMaximumSize(QtCore.QSize(120, 20))
        self.etiqueta_largo.setScaledContents(False)
        self.etiqueta_largo.setObjectName("etiqueta_largo")
        self.gridLayout_2.addWidget(self.etiqueta_largo, 4, 0, 1, 1)
        self.check_amor = QtWidgets.QCheckBox(self.grupo_opciones_psw)
        self.check_amor.setCursor(QtCore.Qt.PointingHandCursor)
        self.check_amor.setChecked(True)
        self.check_amor.setObjectName("check_amor")
        self.gridLayout_2.addWidget(self.check_amor, 1, 2, 1, 1)
        self.check_mayus = QtWidgets.QCheckBox(self.grupo_opciones_psw)
        self.check_mayus.setMinimumSize(QtCore.QSize(0, 0))
        self.check_mayus.setMaximumSize(QtCore.QSize(75, 16777215))
        self.check_mayus.setCursor(QtCore.Qt.PointingHandCursor)
        self.check_mayus.setChecked(True)
        self.check_mayus.setObjectName("check_mayus")
        self.gridLayout_2.addWidget(self.check_mayus, 2, 2, 1, 1)
        self.spinBox_largo = QtWidgets.QSpinBox(self.grupo_opciones_psw)
        self.spinBox_largo.setMaximumSize(QtCore.QSize(35, 16777215))
        self.spinBox_largo.setCursor(QtCore.Qt.PointingHandCursor)
        self.spinBox_largo.setAutoFillBackground(False)
        self.spinBox_largo.setWrapping(False)
        self.spinBox_largo.setFrame(False)
        self.spinBox_largo.setAccelerated(False)
        self.spinBox_largo.setProperty("showGroupSeparator", True)
        self.spinBox_largo.setMinimum(4)
        self.spinBox_largo.setMaximum(16)
        self.spinBox_largo.setProperty("value", 13)
        self.spinBox_largo.setObjectName("spinBox_largo")
        self.gridLayout_2.addWidget(self.spinBox_largo, 4, 1, 1, 1)
        self.check_numeros = QtWidgets.QCheckBox(self.grupo_opciones_psw)
        self.check_numeros.setMinimumSize(QtCore.QSize(30, 0))
        self.check_numeros.setCursor(QtCore.Qt.PointingHandCursor)
        self.check_numeros.setToolTip("")
        self.check_numeros.setChecked(True)
        self.check_numeros.setAutoRepeat(False)
        self.check_numeros.setObjectName("check_numeros")
        self.gridLayout_2.addWidget(self.check_numeros, 1, 0, 1, 1)
        self.boton_info = QtWidgets.QPushButton(self.grupo_opciones_psw)
        self.boton_info.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/media/iconografia/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boton_info.setIcon(icon8)
        self.boton_info.setObjectName("boton_info")
        self.gridLayout_2.addWidget(self.boton_info, 4, 5, 1, 1)
        self.horizontalLayout_5.addWidget(self.grupo_opciones_psw)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/media/iconografia/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TabWidget.addTab(self.tab_3, icon9, "")

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        TabWidget.setWindowTitle(QtWidgets.QApplication.translate("TabWidget", "Psw Tool", None, -1))
        self.boton_generar.setText(QtWidgets.QApplication.translate("TabWidget", "Generar contraseña:", None, -1))
        self.input_psw.setToolTip(QtWidgets.QApplication.translate("TabWidget", "Puedes introducir tu poropia contraseña", None, -1))
        self.reveal_psw.setToolTip(QtWidgets.QApplication.translate("TabWidget", "Revelar u esconder contraseña", None, -1))
        self.cp1.setToolTip(QtWidgets.QApplication.translate("TabWidget", "Copiar la contraseña", None, -1))
        self.etiqueta_usuario.setText(QtWidgets.QApplication.translate("TabWidget", "Usuario:", None, -1))
        self.cp2.setToolTip(QtWidgets.QApplication.translate("TabWidget", "Copiar el nombre de usuario", None, -1))
        self.etiqueta_mail.setText(QtWidgets.QApplication.translate("TabWidget", "Mail:", None, -1))
        self.cp3.setToolTip(QtWidgets.QApplication.translate("TabWidget", "Copiar el mail", None, -1))
        self.etiqueta_categoria.setText(QtWidgets.QApplication.translate("TabWidget", "Categoria:", None, -1))
        self.etiqueta_url.setText(QtWidgets.QApplication.translate("TabWidget", "Servicio:", None, -1))
        self.input_url.setToolTip(QtWidgets.QApplication.translate("TabWidget", "Ingrese una pagina web, aplicacion, o juego.", None, -1))
        self.boton_guardar.setToolTip(QtWidgets.QApplication.translate("TabWidget", "Guardar en la base de datos la informacion encriptada con la contraseña maestra", None, -1))
        self.boton_guardar.setText(QtWidgets.QApplication.translate("TabWidget", "GUARDAR", None, -1))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_1), QtWidgets.QApplication.translate("TabWidget", "Panel principal", None, -1))
        self.boton_seguridad.setToolTip(QtWidgets.QApplication.translate("TabWidget", "Presione para revelar u ocultar las contraseñas", None, -1))
        self.combobox_filtro.setToolTip(QtWidgets.QApplication.translate("TabWidget", "Selecione la categoria por la cual desea filtrar", None, -1))
        self.combobox_filtro.setItemText(0, QtWidgets.QApplication.translate("TabWidget", "Categoria", None, -1))
        self.combobox_filtro.setItemText(1, QtWidgets.QApplication.translate("TabWidget", "Usuario", None, -1))
        self.combobox_filtro.setItemText(2, QtWidgets.QApplication.translate("TabWidget", "Mail", None, -1))
        self.combobox_filtro.setItemText(3, QtWidgets.QApplication.translate("TabWidget", "Servicio", None, -1))
        self.input_filtro.setToolTip(QtWidgets.QApplication.translate("TabWidget", "<html><head/><body><p>Introduzca el texto para buscar exactamente</p></body></html>", None, -1))
        self.boton_filtro.setToolTip(QtWidgets.QApplication.translate("TabWidget", "Establezca un filtro", None, -1))
        self.boton_editar.setToolTip(QtWidgets.QApplication.translate("TabWidget", "Pulse este boton para alternar entre el modo de edicion de datos.", None, -1))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_2), QtWidgets.QApplication.translate("TabWidget", "Base de datos", None, -1))
        self.grupo_opciones_psw.setTitle(QtWidgets.QApplication.translate("TabWidget", "Opciones para la formacion de la contraseña:", None, -1))
        self.check_caracteres.setText(QtWidgets.QApplication.translate("TabWidget", "Caracteres especiales: !%_-@#", None, -1))
        self.boton_guardar_config.setToolTip(QtWidgets.QApplication.translate("TabWidget", "Presione para guardar esta configuración", None, -1))
        self.boton_guardar_config.setText(QtWidgets.QApplication.translate("TabWidget", "Guardar", None, -1))
        self.check_min.setText(QtWidgets.QApplication.translate("TabWidget", "Minúsculas", None, -1))
        self.etiqueta_largo.setText(QtWidgets.QApplication.translate("TabWidget", "Cantidad de caracteres:", None, -1))
        self.check_amor.setToolTip(QtWidgets.QApplication.translate("TabWidget", "Descarga el icono de la pagina", None, -1))
        self.check_amor.setText(QtWidgets.QApplication.translate("TabWidget", "Fabricada con amor :3", None, -1))
        self.check_mayus.setText(QtWidgets.QApplication.translate("TabWidget", "Mayúsculas", None, -1))
        self.check_numeros.setText(QtWidgets.QApplication.translate("TabWidget", "Números", None, -1))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_3), QtWidgets.QApplication.translate("TabWidget", "Configuración", None, -1))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TabWidget = QtWidgets.QTabWidget()
    ui = Ui_TabWidget()
    ui.setupUi(TabWidget)
    TabWidget.show()
    sys.exit(app.exec_())

