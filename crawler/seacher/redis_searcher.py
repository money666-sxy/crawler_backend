from crawler.db_handle.redis_handler import RedisHandler

redis_handler = RedisHandler()

def searchRedisKeywords(keywords):
    title_list = redis_handler.queryKeywordsTitle(keywords)

    search_result = []
    for title in title_list:
        try:
            title_info = {}
            title_info['title'] = title
            title_info['content'] = redis_handler.hget(title, "content").decode()
            title_info['slug'] = redis_handler.hget(title, "slug").decode()
            title_info['author_id'] = redis_handler.hget(title, "author_id").decode()
            title_info['author_nick_name'] = redis_handler.hget(title, "author_nick_name").decode()
            title_info['notebook_id'] = redis_handler.hget(title, "notebook_id").decode()
            title_info['notebook_name'] = redis_handler.hget(title, "notebook_name").decode()
            title_info['commentable'] = redis_handler.hget(title, "commentable").decode()
            title_info['public_comments_count'] = redis_handler.hget(title, "public_comments_count").decode()
            title_info['like_count'] = redis_handler.hget(title, "like_count").decode()
            title_info['total_rewards_count'] = redis_handler.hget(title, "total_rewards_count").decode()
            title_info['first_shared_at'] = redis_handler.hget(title, "first_shared_at").decode()
            search_result.append(title_info)
        except:
            print("redis error!")
    if len(search_result) == 0:
        search_result = None

    return search_result