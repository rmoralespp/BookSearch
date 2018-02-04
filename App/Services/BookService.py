# -*- coding: utf-8 -*-
import sqlite3
from PyQt4.QtCore import QObject, SIGNAL
from threading import Thread
from ObservableService import ObservableService
from SingletonService import Singleton


class BookService:
    __metaclass__ = Singleton

    def __init__(self):
        self.observable_service = ObservableService()
        self.__initSignals()

    def __initSignals(self):
        self.signal_loading = SIGNAL("loading")
        self.worker = QObject()
        QObject.connect(self.worker, self.signal_loading, self.__onQueryEnd)

    def __connect(self):
        try:
            self.conexion = sqlite3.connect('db.db')
            self.conexion.text_factory = bytes
            self.cursor = self.conexion.cursor()
        except Exception as e:
            print(e)
            self.cursor = None
            self.conexion = None


    def filterBooks(self, *args, **kwargs):
        conditions = ""
        params = []
        if 'isbn' in kwargs.keys():
            conditions, params = self.__addCondition(conditions, params, 'ISBN', kwargs.get('isbn', ""))
        if 'titulo' in kwargs.keys():
            conditions, params = self.__addCondition(conditions, params, 'BookTitle', kwargs.get('titulo', ""))
        if 'autor' in kwargs.keys():
            conditions, params = self.__addCondition(conditions, params, 'BookAuthor', kwargs.get('autor', ""))
        if 'editorial' in kwargs.keys():
            conditions, params = self.__addCondition(conditions, params, 'Publisher', kwargs.get('editorial', ""))
        if 'anno_pub' in kwargs.keys():
            conditions, params = self.__addCondition(conditions, params, 'YearOfPublication', kwargs.get('anno_pub', ""))
        subproceso = Thread(target=self.__executeQuery, args=("BXBooks", conditions, params, "BookTitle"))
        self.observable_service.startLoadingBooks()
        subproceso.start()



    def __addCondition(self, conditions, params, indicator, valor_indicator):
           if unicode(valor_indicator).strip() != "":
               if len(params) == 0:
                    conditions = " where %s like ? "%"LOWER(%s)"%unicode(indicator)
               else:
                    conditions += "and %s like ? "%"LOWER(%s)"%unicode(indicator)
               params.append(valor_indicator)
           return (conditions, params)


    def __executeQuery(self, table, conditions, params, order_field, order_dir = 'asc'):
            self.__connect()
            books = []
            if isinstance(self.cursor, sqlite3.Cursor):
                query = "SELECT * from %s"%table
                query += conditions
                query += " order by %s %s"%(order_field, order_dir)
                try:
                    self.cursor.execute(query, tuple(map(lambda param: '%' + unicode(param).lower() + '%', params)))
                    books = self.cursor.fetchall()
                except Exception:
                    pass
                self.conexion.close()
            self.worker.emit(self.signal_loading, books)


    def __onQueryEnd(self, books):
        self.observable_service.stopLoadingBooks()
        self.observable_service.updateBooks(books)


