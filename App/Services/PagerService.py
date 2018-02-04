class PagerService:

    def __init__(self, total_items=0, current_page=1, page_size=27):
        self.__start_page = 1
        self.__current_page = current_page
        self.__page_size = page_size
        self.setTotalItems(total_items)

    def getCurrentPage(self):
        return self.__current_page

    def getNoPages(self):
        return self.__total_pages

    def setTotalItems(self, total_items):
        if isinstance(total_items, int):
            self.__total_items = total_items
            self.__total_pages = max(int(total_items / self.__page_size), 1)
            self.__end_page = self.__total_pages

    def setPage(self, no_page):
        control = False
        if isinstance(no_page, int):
            if no_page >= self.__start_page and no_page <= self.__end_page:
                self.__current_page = no_page
                control = True
        start_index = int((self.__current_page - 1) * self.__page_size)
        end_index = min(start_index + self.__page_size - 1, self.__total_items - 1)
        end_index = max(end_index, 0) # Si el total de items es 0 el indice final tambien es 0
        return (start_index, end_index, control)