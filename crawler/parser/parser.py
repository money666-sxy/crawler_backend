# coding: utf-8

import time
import json
import asyncio
import requests
from threading import Thread

import aiohttp

from crawler.info_queues.raw_info_queue import RawInfoQueue
from crawler.info_queues.db_queue import DBQueue
from crawler.items.articles import Article
from crawler.tools import textFix, getLikeRate, isHot
from crawler.db_handle.redis_handler import RedisHandler
from crawler.db_handle.sql_handler import SQLHandler

redis_handler = RedisHandler()
sql_handler = SQLHandler()


class Parser(object):

    def __init__(self, get_page_num, get_cookie, add_url):
        self.headers = None
        self.raw_info_queue = RawInfoQueue(maxsize=10)
        self.db_queue = DBQueue(maxsize=10)
        self.start_urls = []

        self.getPageNum = get_page_num
        self.getCookie = get_cookie
        self.addUrl = add_url
        self.search_result = []

        thread_parse_info = Thread(target=self.parseInfo)
        thread_save2db = Thread(target=self.save2db)
        thread_parse_info.start()
        thread_save2db.start()

    def searchKeyWord(self, keywords):
        print("start searching")

        if type(keywords) == str:
            keyword = keywords
            self.getCookie()
            self.addUrl(keyword)
        else:
            for keyword in keywords:
                self.getCookie()
                self.addUrl(keyword)

        asyncio.run(self.crawlerStart())
        print("end............................................................")

    async def crawlerStart(self):
        tasks = (self.getInfo(url, 'POST') for url in self.start_urls)
        await asyncio.gather(*tasks)

    async def getInfo(self, url, method):
        try:
            '''请求数据'''
            if method == 'GET':
                pass
            elif method == 'POST':
                try:
                    async with aiohttp.ClientSession() as client:
                        r = await client.post(url=url, headers=self.headers, ssl=False)
                        response = await r.text(encoding='utf-8')
                        self.raw_info_queue.put(response)
                except:
                    raise Exception("requests " + url + " error")
        except Exception as e:
            print(e)

    def parseInfo(self):
        # try:
        while True:
            info = self.raw_info_queue.get()
            # try:
            text = json.loads(info)['entries']
            for item in text:
                article = Article()

                article.likes_count = item['likes_count']
                article.first_shared_at = item['first_shared_at']
                article.like_rate = getLikeRate(article)

                if article.like_rate > 0.1:
                    # print(article.like_rate)
                    pass
                else:
                    continue


                article.id = item['id']
                article.title = textFix(item['title'])
                article.content = textFix(item['content'])
                article.author.id = item['user']['id']
                article.author.nickname = textFix(
                    item['user']['nickname'])
                article.slug = item ['slug']
                article.author.author_avatar_url = item['user']['avatar_url']
                article.notebook.id = item['notebook']['id']
                article.notebook.name = item['notebook']['name']
                article.commentable = item['commentable']
                article.public_comments_count = item['public_comments_count']
                article.views_count = item['views_count']
                article.total_rewards_count = item['total_rewards_count']
                print(article.title)

                result_dict = {'id': article.id, 'title': article.title, 'content': article.content, 'slug': article.slug, 'author_id': article.author.id, 'author_nick_name': article.author.nickname, 'notebook_id': article.notebook.id, 'notebook_name': article.notebook.name,
                               'commentable': article.commentable, 'public_comments_count': article.public_comments_count, 'like_count': article.views_count, 'total_rewards_count': article.total_rewards_count, 'first_shared_at': article.first_shared_at}
                self.search_result.append(result_dict)
                self.db_queue.put(article)
        #         except:
        #             raise Exception("赋值出错")
        # except Exception as e:
        #     print(e)

    def save2db(self):
        '''筛选 like_rate > 3 存入redis'''
        while True:
            try:
                article = self.db_queue.get()
                if isHot(article):
                    redis_handler.hset(article)
                sql_handler.insertArticle(article)
            except Exception as e:
                print(e)

