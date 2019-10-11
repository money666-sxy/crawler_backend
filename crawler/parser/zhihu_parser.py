from crawler.parser.parser import Parser

class ZhihuParser(Parser):

    def __init__(self):
        Parser.__init__(self, self.__get_page_num, self.__get_cookie, self.__add_url)

    def __get_page_num(self):
        pass

    def __get_cookie(self):
        pass

    def __add_url(self):
        pass