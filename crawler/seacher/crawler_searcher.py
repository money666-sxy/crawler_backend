
from crawler.parser.jianshu_parser import JianshuParser
from crawler.parser.zhihu_parser import ZhihuParser

jianshu_parser = JianshuParser()

def search_crawler_keywords(keywords):
    jianshu_parser.searchKeyWord(keywords)
    search_result = list(jianshu_parser.search_result)
    jianshu_parser.start_urls.clear()
    jianshu_parser.search_result.clear()
    if len(search_result) == 0:
        search_result = None
    return search_result