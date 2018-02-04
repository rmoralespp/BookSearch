from PyQt4 import QtGui, QtCore
from PyQt4.QtTest import QTest
import sys
import unittest
import sqlite3
from App.Services.BookService import BookService
from App.Services.PagerService import PagerService
from App.Services.ObservableService import ObservableService
from App.Controller import Controller
from App.ControllerBA import ControllerBA


class TestsBookDataSource(unittest.TestCase):
    book_sotore = BookService()
    book_sotore1 = BookService()

    def testConnect(self):
        self.book_sotore._BookService__connect()
        self.assertNotEqual(self.book_sotore.cursor, None)
        self.assertIsInstance(self.book_sotore.cursor, sqlite3.Cursor)

    def testSingleton(self):
        self.assertEqual(self.book_sotore, self.book_sotore1)


class TestObservableService(unittest.TestCase):
    observable1 = ObservableService()
    observable2 = ObservableService()

    def testSingleton(self):
        self.assertEqual(self.observable2, self.observable1)

    def testSubscribe(self):
        ObservableService.subscribeBook(self)
        self.assertIn(self, ObservableService._observers['book'])


class TestsPagerService(unittest.TestCase):
       pager_service = PagerService()

       def testSetPagerEmpty(self):
           start_index, end_index, control = self.pager_service.setPage(10000)
           self.assertEqual(control, False)
           self.assertEqual(start_index, 0) and  self.assertEqual(end_index, 0)

       def testSetPagerTotal23(self):
           self.pager_service.setTotalItems(23)  # Current Page Size = 27
           start_index, end_index, control = self.pager_service.setPage('2')
           self.assertEqual(control, False)
           self.assertEqual(start_index, 0) and self.assertEqual(end_index, 0)

       def testSetPagerTotal80(self):
           self.pager_service.setTotalItems(80)  # Current Page Size = 27
           start_index, end_index, control = self.pager_service.setPage(2)
           self.assertEqual(control, True)
           self.assertEqual(start_index, 27) and self.assertEqual(end_index, 53)



class TestController(unittest.TestCase):
        test_app = QtGui.QApplication(sys.argv)
        c = Controller()
        c.setupUi(c)

        def testInputBuscar(self):
            QTest.keyClicks(self.c.input_buscar, "Titulo a bucar")

        def testBtns(self):
            QTest.mouseClick(self.c.btn_busqueda_avanzada, QtCore.Qt.LeftButton)
            QTest.mouseClick(self.c.btn_anterior, QtCore.Qt.LeftButton)
            QTest.mouseClick(self.c.btn_siguiente, QtCore.Qt.LeftButton)

        def testUpdateListBooks(self):
            book_sotore = BookService()
            book_sotore._BookService__connect()
            book_sotore.cursor.execute("SELECT * from BXBooks limit 10")
            books = book_sotore.cursor.fetchall()
            book_sotore.conexion.close()
            self.c.updateSearch(books)
            self.assertEqual(self.c.list_libros.count(), len(books))






if __name__ == "__main__":
    unittest.main()