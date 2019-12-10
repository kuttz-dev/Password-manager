from PySide2.QtWidgets import QFileDialog, QStyledItemDelegate, QStyle
from PySide2.QtGui import QPixmap, QPalette
from PySide2.QtCore import QByteArray, QSize, Qt

class ImageDelegate(QStyledItemDelegate):
    """Books delegate to rate the books"""

    def __init__(self, parent=None):
        QStyledItemDelegate.__init__(self, parent)


    def paint(self, painter, option, index):
        """ Paint the items in the table.

            If the item referred to by <index> is a StarRating, we
            handle the painting ourselves. For the other items, we
            let the base class handle the painting as usual.

            In a polished application, we'd use a better check than
            the column number to find out if we needed to paint the
            stars, but it works for the purposes of this example.
        """
        if option.state & QStyle.State_Enabled:
            if option.state & QStyle.State_Active:
                color_group = QPalette.Normal
            else:
                color_group = QPalette.Inactive
        else:
            color_group = QPalette.Disabled

        if option.state & QStyle.State_Selected:
            painter.fillRect(option.rect,
                             option.palette.color(color_group, QPalette.Highlight)
                             )
        imagen = QPixmap()
        try:
            imagen.loadFromData(index.data())  # , Qt.DisplayRole
        except TypeError:
            return QStyledItemDelegate.paint(self, painter, option, index)
        imagen = imagen.scaled(QSize(16, 16), Qt.KeepAspectRatio)
        width = imagen.width()
        height = imagen.height()
        """Para calcular el lugar donde se tiene que dibujar
        1. option.rect te da: (0, 0, width() , height() ) of the image
        2. Del punto en el que hay que empezar a dibujar, le sumamos
           la mitad del ancho de la celda
        3. Y luego le restamos el ancho del objeto para que quede en la mitad
        """
        x = option.rect.x() + (option.rect.width() / 2) - (width / 2) 
        y = option.rect.y() + (option.rect.height() / 2) - (height / 2)
        # x,y cordenadas - 32,32 ancho y alto de la imagen - la imagen
        painter.drawPixmap(x, y, imagen)

        pen = painter.pen()
        painter.setPen(option.palette.color(QPalette.Mid))

    def sizeHint(self, option, index):
        """ Returns the size needed to display the item in a QSize object. """
        imagen = QPixmap()
        try:
            imagen.loadFromData(index.data())  # , Qt.DisplayRole
        except TypeError:
            return QStyledItemDelegate.sizeHint(self, option, index) + QSize(1, 1)

        size_hint = QSize(5 * imagen.width(), imagen.height()) + QSize(1, 1)
        return size_hint

    def createEditor(self, parent, option, index):
        editor = QFileDialog()
        editor.setFileMode(QFileDialog.ExistingFile)
        editor.setNameFilter("Imagenes (*.png *.xpm *.jpg *.ico)")
        editor.resize(437, 200)
        return editor

    def setModelData(self, editor, model, index):
        if index.isValid():
            try:
                selected_file = editor.selectedFiles()[0]
            except IndexError:
                return False  # Le dio a cancelar
            with open(selected_file, "rb") as ico:
                array = QByteArray(ico.read())
            model.setData(index, array)
            model.dataChanged.emit(index, index, (Qt.DisplayRole, ))
            return True

        return False
