import requests
import time
import json
import asyncio
import aiohttp

from threading import Thread
from queue import Queue

headers = {
            'accept': 'application/json',
            'user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
            'Referrer Policy': 'no-referrer-when-downgrade',
            'cookie': '__yadk_uid=w0mb9fgl9kpuFiJ3Rs6RRUElvmrSsUDB; read_mode=day; default_font=font2; locale=zh-CN; remember_user_token=W1s4OTc1Mjc5XSwiJDJhJDExJDJRU3NIdUZueDBPMTEwcElnRGo5eE8iLCIxNTY5OTUyNjE4LjYyOTgzNiJd--d2d4c1c8b4022b821e76c07caff162e1dadf315b; _m7e_session_core=404d263298364c349b3888daa07b8c51; Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1568774957,1569250659,1569565480,1569952621; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%228975279%22%2C%22%24device_id%22%3A%2216c76867f88368-0263c03cd3d34b-38607701-1296000-16c76867f8954e%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22desktop%22%2C%22%24latest_utm_medium%22%3A%22search-trending%22%7D%2C%22first_id%22%3A%2216c76867f88368-0263c03cd3d34b-38607701-1296000-16c76867f8954e%22%7D; Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068=156995262'
           }


def get_url(keywords):
    '''根据关键字获取url'''
    url = []
    for keyword in keywords:
        for i in range(10):
            url.append("https://www.jianshu.com/search/do?q=" + keyword + "&type=note&page=" + str(i) + "&order_by=default")
    return url

async def crawler_start(urls):
    tasks = (asy_get_info(url) for url in urls)
    await asyncio.gather(*tasks)


async def asy_get_info(url):
    async with aiohttp.ClientSession() as client:
        r = await client.post(url=url, headers=headers, ssl=False)
        response = await r.text(encoding='utf-8')
        try:
            text = json.loads(response)['entries']
            for item in text:
                title = text_fix(item['title'])
                print(title)
        except:
            print(response)

def text_fix(text):
    '''去除json信息中的html标签'''
    text = text.replace(
        r"<em class='search-result-highlight'>", "").replace(r"</em>", "")
    return text




