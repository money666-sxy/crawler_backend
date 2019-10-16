
from crawler.parser.jianshu_parser import JianshuParser
from crawler.parser.zhihu_parser import ZhihuParser

jianshu_parser = JianshuParser()

def searchCrawlerKeywords(keywords):
    jianshu_parser.searchKeyWord(keywords)
    search_result = list(jianshu_parser.search_result)
    jianshu_parser.start_urls.clear()
    jianshu_parser.search_result.clear()
    if len(search_result) == 0:
        search_result = None
    return search_result