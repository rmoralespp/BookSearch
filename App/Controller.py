# -*- coding: utf-8 -*-
from PyQt4.QtGui import QMainWindow, QPixmap, QLabel, QMovie
from PyQt4.QtCore import SIGNAL, QObject
import urllib
from threading import Thread
from Views.UiMain import Ui_MainWindow
from ControllerBA import ControllerBA
from Services.CommonService import CommonService


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Controller, self).__init__()
        self.setupUi(self)
        self.books = []
        self.current_page = 1
        self.box_detalles.hide()
        self.addEventsListener()
        self.builLoadingIco()
        self.initSignals()
        self.initServices()

    def initServices(self):
        self.services = CommonService()
        self.services.subscribeToBook(self)

    def initSignals(self):
        self.signal_loading = SIGNAL("loading")
        QObject.connect(self, self.signal_loading, self.setPreviewBookDetail)

    def builLoadingIco(self):
        self.loading_label = QLabel(self.centralwidget)
        self.loading_label.move(350, 250)
        self.loading_label.setFixedSize(145, 145)
        self.movie_loading_gif = QMovie(":/newPrefix/Users/Lia/PycharmProjects/BookSearch/Design/loading.gif")
        self.loading_label.setMovie(self.movie_loading_gif)
        self.loading_label.hide()

    def startLoading(self):
        self.movie_loading_gif.start()
        self.loading_label.show()
        self.setDisabled(True)

    def stopLoading(self):
        self.movie_loading_gif.stop()
        self.loading_label.hide()
        self.setDisabled(False)

    def addEventsListener(self):
        self.btn_buscar.clicked.connect(self.onSearchTitle)
        self.btn_busqueda_avanzada.clicked.connect(self.onShowViewBA)
        self.btn_siguiente.clicked.connect(self.onNextPage)
        self.btn_anterior.clicked.connect(self.onPreviousPage)
        self.list_libros.itemClicked.connect(self.onDetailsBook)

    def onDetailsBook(self):
        self.box_detalles.show()
        pos = self.list_libros.currentRow()
        i = (((self.current_page - 1) * 27) + pos) # Calcular Pos Real a partir del page size
        self.titulo_value.setText(self.books[i][1].decode('latin-1')[0:50]+"...")
        self.isbn_value.setText(self.books[i][0])
        self.autor_value.setText(self.books[i][2].decode('latin-1'))
        self.fecha_pub_value.setText(unicode(self.books[i][3]))
        self.editorial_value.setText(self.books[i][4].decode('latin-1'))
        subproceso = Thread(target=self.loadImageData, args=(self.books[i][7].decode('latin-1'),))
        self.startLoading()
        subproceso.start()

    def loadImageData(self, url):
        data = None
        try: data = urllib.urlopen(url).read()
        except Exception: pass
        self.emit(self.signal_loading, data)


    def setPreviewBookDetail(self, data):
        if data != None:
            pixmap = QPixmap()
            pixmap.loadFromData(data)
            self.label_img.setScaledContents(True)
            self.label_img.setPixmap(pixmap)
        self.stopLoading()

    def onSearchTitle(self):
        text = self.input_buscar.text()
        if text != '':
            self.box_detalles.hide()
            self.services.filterBooks(titulo=text)

    def updateSearch(self, books):
        self.books = books
        self.services.setTotalBooks(len(books))  # Set Pager Total Items
        self.updateBookList(1)

    def updateBookList(self, no_page):
        start_index, end_index, control = self.services.setPage(no_page)  # Pager
        if control == True:
            self.current_page = no_page
            if len(self.books) > 0:
                self.pagina_value.setText(unicode(no_page)+"-"+unicode(self.services.getNoPages()))
            else:
                self.pagina_value.setText("1 *No se encontraron resultados*")
            titulos = map(lambda libro: libro[1], self.books[start_index:end_index + 1])
            self.list_libros.clear()
            self.list_libros.addItems(titulos)

    def onNextPage(self):
        self.updateBookList(self.current_page + 1)

    def onPreviousPage(self):
        self.updateBookList(self.current_page - 1)

    def onShowViewBA(self):
        self.box_detalles.hide()
        self.view_ba = ControllerBA()
        self.view_ba.show()
