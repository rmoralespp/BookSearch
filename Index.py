from PyQt4 import QtGui
import sys
from App.Controller import Controller

if __name__ == "__main__":
    qt_app = QtGui.QApplication(sys.argv)
    book_search_app = Controller()
    book_search_app.show()
    sys.exit(qt_app.exec_())


