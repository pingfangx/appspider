# -*- coding: utf-8 -*-
# @Time    : 2018/5/28 22:03
# @Author  : ddvv
# @Site    : http://ddvv.life
# @File    : xiaomistorespider.py
# @Software: PyCharm

"""
第三方依赖库: Crypto
功能:
    1. 获取小米商店应用评论
消息说明:
    1. "AppSpider-0010-001" : 应用评论
"""

import scrapy
from appspider.commonapis import *

CONST_INFO = {
    'app_name': 'com.xiaomi.market',
    'app_version': 'R.1.4.5',
    'spider_author': 'ddvv'
}


class xiaomistorecommentsspider(scrapy.Spider):
    """
    爬取中国裁判文书APP
    """
    # 爬虫名称
    name = 'xiaomistorecommentsspider'

    def __init__(self, appid, **kwargs):
        super().__init__(**kwargs)
        self.header = {
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 7.0; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10)",
            "Host": "app.market.xiaomi.com",
            "Accept-Encoding": "gzip, deflate"
        }
        self.appid = appid

    # 爬虫入口，发起请求
    def start_requests(self):
        """

        """
        appid = self.appid
        header = self.header
        burl = "https://app.market.xiaomi.com/apm/comment/list/{" \
               "appid}?channel=market_100_1_android&clientId=70a40c54102b9be2da4664cd819bbc32&co=CN" \
               "&densityScaleFactor=3.0&imei=6066eb90c6d80f6e8eaa7afd48256483&la=zh&marketVersion=147&model=HUAWEI" \
               "+NXT-AL10&os=C00B577&page={page}&resolution=1080*1812&sdk=24&session=2jmj7l5rSw0yVb_v"
        for page in range(0, 10):
            url = burl.format(appid=appid, page=page)
            yield scrapy.Request(url=url,
                                 headers=header,
                                 method='GET',
                                 callback=self.parse)

    # 解析返回值，推送至pipeline
    def parse(self, response):
        """

        :param response: 爬取的数据返回值。
        """
        try:
            js = json.loads(response.body.decode())
            js['appid'] = self.appid
            item = setappspideritem('AppSpider-0009-001', 'json', js, **CONST_INFO)
            yield item
        except Exception as e:
            logger.error(str(e))
