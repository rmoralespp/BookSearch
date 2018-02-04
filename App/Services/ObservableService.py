from SingletonService import Singleton

class ObservableService:
    __metaclass__ = Singleton

    _observers = {'book': []}

    @staticmethod
    def subscribeBook(observer):
        observer_books = ObservableService._observers['book']
        if observer not in observer_books:
            observer_books.append(observer)


    def updateBooks(self, books):
        observer_books = self._observers['book']
        for observer in observer_books:
            try:
                observer.updateSearch(books)
            except Exception:
                continue

    def startLoadingBooks(self):
        observer_books = self._observers['book']
        for observer in observer_books:
            try:
                observer.startLoading()
            except Exception:
                continue

    def stopLoadingBooks(self):
        observer_books = self._observers['book']
        for observer in observer_books:
            try:
                observer.stopLoading()
            except Exception:
                continue
