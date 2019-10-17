from crawler.db_handle.sql_handler import SQLHandler

sql_handler = SQLHandler()

def searchSQLKeywords(keywords):
    article_list = sql_handler.queryArticle(keywords)
    search_result = []

    if article_list:
        for article in article_list:
            article_info = {}
            article_info['title'] = article[1]
            article_info['content'] = article[2]
            article_info['likes_count'] = article[3]
            article_info['public_comments_count'] = article[4]
            # title_info['author_nick_name'] = article[1].decode()
            # title_info['notebook_id'] = article[1].decode()
            # title_info['notebook_name'] = article[1].decode()
            article_info['slug'] = article[5]
            article_info['views_count'] = article[6]
            article_info['total_rewards_count'] = article[7]
            article_info['first_shared_at'] = article[8]
            article_info['like_rate'] = article[9]
            search_result.append(article_info)

        if len(search_result) == 0:
            search_result = None

        return search_result