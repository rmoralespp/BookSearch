from PyQt4 import QtGui
from PyQt4.QtCore import QRegExp
from Views.UiBA import Ui_DialogBA
from Services.CommonService import CommonService

class ControllerBA(QtGui.QDialog, Ui_DialogBA):

    def __init__(self):
        super(ControllerBA, self).__init__()
        self.setupUi(self)
        self.services = CommonService()
        self.addEventsListener()
        self.addValidations()

    def addEventsListener(self):
        self.btn_cancelar.clicked.connect(self.onCancel)
        self.btn_aceptar.clicked.connect(self.onAceptar)


    def addValidations(self):
        year_pub_validator = QtGui.QRegExpValidator(QRegExp("[0-9]{4}"), self.input_fecha_pub)
        self.input_fecha_pub.setValidator(year_pub_validator)


    def onCancel(self):
        self.hide()

    def onAceptar(self):
        autor = self.input_autor.text()
        editorial = self.input_editorial.text()
        isbn = self.input_isbn.text()
        anno_pub = self.input_fecha_pub.text()
        title = self.input_title.text()

        if isbn!= "" or autor!="" or editorial!="" or anno_pub!="" or title!="":
            self.services.filterBooks(titulo=title, autor=autor, editorial=editorial, isbn=isbn, anno_pub=anno_pub)
            self.hide()
