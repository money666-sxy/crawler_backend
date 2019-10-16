import pymysql


class SQLHandler(object):
    def __init__(self, username, password):
        self.port = "127.0.0.1"
        self.database = "crawler"
        self.__conn = pymysql.connect(host='localhost', port=3306, user='root',
                                      password='root', db='crawler', charset='utf8')
        self.cursor = self.__conn.cursor()

    def query(self):
        pass

    def execute(self, sql):
        self.cursor.execute(sql)

    def insertArticle(self, article):
        sql = "insert into tbl_article values('%s' '%s' '%s' '%s' '%s' '%s' '%s' '%s' '%s')" % (
            article.title, article.content, article.public_comments_count, article.likes_count, article.slug,
            article.views_count, article.total_rewards_count, article.first_shared_at, article.like_rate)
        self.execute(sql)
