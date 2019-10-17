import pymysql


class SQLHandler(object):

    def __init__(self):
        self.__conn = pymysql.connect(host='127.0.0.1', user='root',
                                      password='0000', db='crawler', charset='utf8', autocommit=True)
        self.cursor = self.__conn.cursor()

    def __contains__(self, article):
        title = article.title
        content = article.content
        query_result = self.queryArticleTitle(title)
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
        if article not in self:
            try:
                sql = "insert into tbl_article(title, content, public_comments_count, likes_count, slug, views_count, total_rewards_count, first_shared_at, like_rate)  " \
                      "values ('%s', '%s', '%d', '%d', '%s', '%d', '%d', null, '%f');" % (
                          article.title, article.content, article.public_comments_count, article.likes_count,
                          article.slug,
                          article.views_count, article.total_rewards_count, article.like_rate)
                self.execute(sql)
                self.__conn.close()
            except Exception as e:
                raise (e)

    def queryArticleTitle(self, title):
        sql = "select * from tbl_article where title = '%s'" % title
        return self.query(sql)

    def queryArticle(self, keyword):
        result = []
        sql_title = "select * from tbl_article where title like '%{}%'".format(keyword)
        title_result = self.query(sql_title)
        for item in title_result:
            result.append(item)

        sql_content = "select * from tbl_article where content like  '%{}%'".format(keyword)
        content_result = self.query(sql_content)
        for item in content_result:
            result.append(item)

        # sql_author = "select * from tbl_article where author like '%{}%'".format(keyword)
        # author_result = self.query(sql_author)
        # for item in author_result:
        #     result.append(item)

        print(list(set(result)))

if __name__ == "__main__":
    sql_handler = SQLHandler()
sql_handler.queryArticle("go")
