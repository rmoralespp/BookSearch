# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UiBA.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DialogBA(object):
    def setupUi(self, DialogBA):
        DialogBA.setObjectName(_fromUtf8("DialogBA"))
        DialogBA.resize(415, 185)
        self.verticalLayout_4 = QtGui.QVBoxLayout(DialogBA)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_5 = QtGui.QLabel(DialogBA)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.label = QtGui.QLabel(DialogBA)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(DialogBA)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(DialogBA)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtGui.QLabel(DialogBA)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.input_title = QtGui.QLineEdit(DialogBA)
        self.input_title.setObjectName(_fromUtf8("input_title"))
        self.verticalLayout_2.addWidget(self.input_title)
        self.input_isbn = QtGui.QLineEdit(DialogBA)
        self.input_isbn.setObjectName(_fromUtf8("input_isbn"))
        self.verticalLayout_2.addWidget(self.input_isbn)
        self.input_editorial = QtGui.QLineEdit(DialogBA)
        self.input_editorial.setObjectName(_fromUtf8("input_editorial"))
        self.verticalLayout_2.addWidget(self.input_editorial)
        self.input_fecha_pub = QtGui.QLineEdit(DialogBA)
        self.input_fecha_pub.setMaxLength(32766)
        self.input_fecha_pub.setObjectName(_fromUtf8("input_fecha_pub"))
        self.verticalLayout_2.addWidget(self.input_fecha_pub)
        self.input_autor = QtGui.QLineEdit(DialogBA)
        self.input_autor.setObjectName(_fromUtf8("input_autor"))
        self.verticalLayout_2.addWidget(self.input_autor)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btn_aceptar = QtGui.QPushButton(DialogBA)
        self.btn_aceptar.setObjectName(_fromUtf8("btn_aceptar"))
        self.horizontalLayout.addWidget(self.btn_aceptar)
        self.btn_cancelar = QtGui.QPushButton(DialogBA)
        self.btn_cancelar.setObjectName(_fromUtf8("btn_cancelar"))
        self.horizontalLayout.addWidget(self.btn_cancelar)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.retranslateUi(DialogBA)
        QtCore.QMetaObject.connectSlotsByName(DialogBA)

    def retranslateUi(self, DialogBA):
        DialogBA.setWindowTitle(_translate("DialogBA", "Búsqueda Avanzada", None))
        self.label_5.setText(_translate("DialogBA", "Título", None))
        self.label.setText(_translate("DialogBA", "ISBN", None))
        self.label_2.setText(_translate("DialogBA", "Editorial", None))
        self.label_3.setText(_translate("DialogBA", "Año de Publicación", None))
        self.label_4.setText(_translate("DialogBA", "Autor", None))
        self.btn_aceptar.setText(_translate("DialogBA", "Aceptar", None))
        self.btn_cancelar.setText(_translate("DialogBA", "Cancelar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogBA = QtGui.QDialog()
    ui = Ui_DialogBA()
    ui.setupUi(DialogBA)
    DialogBA.show()
    sys.exit(app.exec_())

