import time
import json

from flask import Flask, request, make_response, jsonify, send_from_directory
from flask_cors import CORS

from crawler.parser.jianshu_parser import JianshuParser
from crawler.db_handle.redis_handler import RedisHandler
from crawler.seacher.crawler_searcher import search_crawler_keywords
from crawler.seacher.redis_searcher import search_redis_keywords

redis_handler = RedisHandler()

app = Flask(__name__)
CORS(app, supports_credentials=True)

jianshu_parser = JianshuParser()

@app.route('/', methods=['GET'])
def get_articles():
    if request.method == 'GET':
        keywords = request.args.get("key_words")
        search_result = search_redis_keywords(keywords)
        if not search_result:
            search_result = search_crawler_keywords(keywords)
    return json.dumps(search_result, ensure_ascii=False)


if __name__ == "__main__":
    app.run()
