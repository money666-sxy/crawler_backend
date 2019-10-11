import requests
import json


from crawler.parser.parser import Parser


class JianshuParser(Parser):
    def __init__(self):
        Parser.__init__(self, self.__get_page_num,
                        self.__get_cookie, self.__add_url)
        self.headers = {'accept': 'application/json',
                        'user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
                        'content-type': 'application/json; charset=utf-8',
                        'Referrer Policy': 'no - referrer - when - downgrade',
                        }

    def __get_page_num(self, keyword):
        '''获取页数'''
        url = 'https://www.jianshu.com/search/do?q=' + \
            keyword + '&type=note&page=1&order_by=default'
        page_info = requests.post(url=url, headers=self.headers).text
        total_pages = json.loads(page_info)['total_pages']
        return total_pages

    def __get_cookie(self):
        self.headers.update({'cookie': '__yadk_uid=w0mb9fgl9kpuFiJ3Rs6RRUElvmrSsUDB; Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1568141141,1568141179,1568220556,1568307421; Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1568307421; locale=zh-CN; read_mode=day; default_font=font2; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216c76867f88368-0263c03cd3d34b-38607701-1296000-16c76867f8954e%22%2C%22%24device_id%22%3A%2216c76867f88368-0263c03cd3d34b-38607701-1296000-16c76867f8954e%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22desktop%22%2C%22%24latest_utm_medium%22%3A%22search-recent%22%7D%2C%22first_id%22%3A%22%22%7D; _m7e_session_core=d8a453b6b4c0b788b19f37d5b3119fbe; signin_redirect=https%3A%2F%2Fwww.jianshu.com%2Fsearch%3Fq%3Dpython%26page%3D1%26type%3Dnote'})

    def __add_url(self, keyword):
        '''添加待处理的url'''
        page_num = self.getPageNum(keyword)
        for i in range(page_num):
            url = 'https://www.jianshu.com/search/do?q=' + keyword + '&type=note&page=' + str(
                i) + '&order_by=default'
            # print(url)
            self.start_urls.append(url)


if __name__ == "__main__":
    jianshu_parser = JianshuParser()
    jianshu_parser.searchKeyWord("Java")
