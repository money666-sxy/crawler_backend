import pymysql

from crawler.tools import contentFix


class SQLHandler(object):

    def __init__(self):
        self.__conn = pymysql.connect(host='127.0.0.1', user='root',
                                      password='0000', db='crawler', charset='utf8', autocommit=True)
        self.cursor = self.__conn.cursor()

    def __contains__(self, article):
        title = article.title
        content = article.content
        query_result = self.queryArticleTitle(title)
        if len(query_result) == 0:
            return False
        if query_result[0][2] == content:
            return True
        return False

    def query(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def execute(self, sql):
        self.cursor.execute(sql)

    def insertArticle(self, article):
        '''插入新文章'''
        if article not in self:
            try:
                sql = 'insert into tbl_article(title, content, public_comments_count, likes_count, slug, views_count, total_rewards_count, first_shared_at, like_rate)  ' \
                      'values ("%s", "%s", "%d", "%d", "%s", "%d", "%d", null, "%f");' % (
                          self.__conn.escape_string(article.title), self.__conn.escape_string(article.content), article.public_comments_count, article.likes_count,
                          article.slug,
                          article.views_count, article.total_rewards_count, article.like_rate)
                print("article.title: ", article.title)
                print("article.content: ", article.content)
                print("article.public_comments_count: ", article.public_comments_count)
                print("article.likes_count: ", article.likes_count)
                print("article.slug: ", article.slug)
                print("article.views_count: ", article.views_count)
                print("article.total_rewards_count: ", article.total_rewards_count)
                print("article.first_shared_at: ", article.first_shared_at)
                print("article.like_rate: ", article.like_rate)
                self.execute(sql)
            except Exception as e:
                raise (e)

    def queryArticleTitle(self, title):
        '''根据文章标题查询'''
        sql = "select * from tbl_article where title = '%s'" % title
        return self.query(sql)

    def queryArticle(self, keyword):
        '''模糊查询文章'''
        result = []
        sql_title = "select * from tbl_article where title like '%{}%'".format(keyword)
        title_result = self.query(sql_title)
        for item in title_result:
            result.append(item)

        sql_content = "select * from tbl_article where content like '%{}%'".format(keyword)
        content_result = self.query(sql_content)
        for item in content_result:
            result.append(item)

        # author表待添加
        # sql_author = "select * from tbl_article where author like '%{}%'".format(keyword)
        # author_result = self.query(sql_author)
        # for item in author_result:
        #     result.append(item)
        if len(result) == 0:
            return None

        return list(set(result))
