from ObservableService import ObservableService
from PagerService import PagerService
from BookService import BookService

class CommonService:
    def __init__(self):
        self.pager = PagerService()
        self.book_store = BookService()
        self.observable = ObservableService()

    def filterBooks(self, *args, **kwargs):
        self.book_store.filterBooks(*args, **kwargs)

    def setPage(self, *args, **kwargs):
        return self.pager.setPage(*args, **kwargs)

    def getNoPages(self):
        return self.pager.getNoPages()

    def setTotalBooks(self, *args, **kwargs):
        return self.pager.setTotalItems(*args, **kwargs)

    def subscribeToBook(self, *args, **kwargs):
        self.observable.subscribeBook(*args, **kwargs)

