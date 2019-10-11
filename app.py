import time
import json

from flask import Flask, request, make_response, jsonify, send_from_directory
from flask_cors import CORS

from crawler.parser.jianshu_parser import JianshuParser


app = Flask(__name__)
CORS(app, supports_credentials=True)

jianshu_parser = JianshuParser()


@app.route('/', methods=['GET'])
def get_articles():
    if request.method == 'GET':
        keywords = request.args.get("key_words")
        print(keywords)
        start = time.time()
        jianshu_parser.searchKeyWord(keywords)
        print("spend: %s" % (time.time() - start))
        search_result = list(jianshu_parser.search_result)
        jianshu_parser.start_urls.clear()
        jianshu_parser.search_result.clear()
        print("list = ", jianshu_parser.search_result)
    return json.dumps(search_result, ensure_ascii=False)


# @app.route('/', methods=['GET'])
# def get_articles():
#     return json.dumps({'a': {'title': 1, 'content': 'this is content'}, 'b': {'title': 2, 'content': 'this is content'}}, ensure_ascii=False)


if __name__ == "__main__":
    app.run()
