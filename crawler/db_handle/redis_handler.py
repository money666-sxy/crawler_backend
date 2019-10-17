import time
import sys

import redis
from threading import Thread

from crawler.items.articles import Article


class RedisHandler(object):
    def __init__(self):
        self.__conn = redis.Redis(host="localhost", port=6379)
        self.chan_sub = "crawler" # 订阅频道

    def publish(self, msg):
        '''发布'''
        self.__conn.publish(self.chan_sub, msg)
        return True

    def subscribe(self):
        '''订阅'''
        pub = self.__conn.pubsub()
        pub.subscribe(self.chan_sub)
        for item in pub.listen():
            if item['type'] == 'pmessage' or item['type'] == 'message':
                print(item['data'])

    def hset(self, article):
        article_info = {'id': str(article.id), 'title': article.title, 'content': article.content, 'slug': article.slug,
                       'author_id': article.author.id, 'author_nick_name': article.author.nickname,
                       'notebook_id': article.notebook.id, 'notebook_name': article.notebook.name,
                       'commentable': article.commentable, 'public_comments_count': article.public_comments_count,
                       'like_count': article.views_count, 'total_rewards_count': article.total_rewards_count,
                       'first_shared_at': article.first_shared_at}
        for key, value in article_info.items():
            self.__conn.hset(article_info['title'], "%s" % key, "%s" % str(value))
            # print(self.__conn.hget(article_info['title'], "slug"))
            # print(article.title)

    def hget(self, title, key):
        return self.__conn.hget(title, key)

    def set(self, key, val):
        self.__conn.set(key, val)

    def get(self, key):
        return self.__conn.get(key)

    def queryKeywordsTitle(self, keyword):
        '''根据key查询文章'''
        title_list = []
        search_list = [keyword, keyword.lower(), keyword.upper(), keyword.capitalize()]
        for item in search_list:
            raw_title_list = self.__conn.keys("*%s*" % item)
            for each in raw_title_list:
                title_list.append(each.decode())
        return set(title_list)


    # def hget(self, list_name):
        # print(self.__conn.hget(list_name, 0, -1))

if __name__ == "__main__":
    rd = RedisHandler()

