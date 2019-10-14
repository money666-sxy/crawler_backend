from crawler.db_handle.redis_handler import RedisHandler

redis_handler = RedisHandler()

def search_redis_keywords(keywords):
    title_list = redis_handler.query_keywords_title(keywords)

    search_result = []
    for title in title_list:
        try:
            title_info = {}
            title_info['title'] = title
            title_info['content'] = redis_handler.hget_(title, "content").decode()
            title_info['slug'] = redis_handler.hget_(title, "slug").decode()
            title_info['author_id'] = redis_handler.hget_(title, "author_id").decode()
            title_info['author_nick_name'] = redis_handler.hget_(title, "author_nick_name").decode()
            title_info['notebook_id'] = redis_handler.hget_(title, "notebook_id").decode()
            title_info['notebook_name'] = redis_handler.hget_(title, "notebook_name").decode()
            title_info['commentable'] = redis_handler.hget_(title, "commentable").decode()
            title_info['public_comments_count'] = redis_handler.hget_(title, "public_comments_count").decode()
            title_info['like_count'] = redis_handler.hget_(title, "like_count").decode()
            title_info['total_rewards_count'] = redis_handler.hget_(title, "total_rewards_count").decode()
            title_info['first_shared_at'] = redis_handler.hget_(title, "first_shared_at").decode()
            search_result.append(title_info)
        except:
            print("redis error!")
    if len(search_result) == 0:
        search_result = None

    return search_result