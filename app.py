import time
import json

from flask import Flask, request, make_response, jsonify, send_from_directory
from flask_cors import CORS

from crawler.parser.jianshu_parser import JianshuParser
from crawler.db_handle.redis_handler import RedisHandler
from crawler.seacher.crawler_searcher import searchCrawlerKeywords
from crawler.seacher.redis_searcher import searchRedisKeywords
from crawler.seacher.sql_searcher import searchSQLKeywords

redis_handler = RedisHandler()

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/', methods=['GET'])
def getArticles():
    if request.method == 'GET':
        start = time.time()
        keywords = request.args.get("key_words")
        # search_result = searchRedisKeywords(keywords)
        search_result = None
        if not search_result:
            print("redis empty!")
            print("search from sql")
            search_result = searchSQLKeywords(keywords)
        if not search_result:
            print("sql empty!")
            print("search from crawler")
            search_result = searchCrawlerKeywords(keywords)
        print("spend: ", time.time() - start)
    return json.dumps(search_result, ensure_ascii=False)


if __name__ == "__main__":
    app.run()
