# -*- coding: utf-8 -*-
# @Time    : 2018/5/11 00:38
# @Author  : ddvv
# @Site    : http://ddvv.life
# @File    : epornerspider.py
# @Software: PyCharm

"""
第三方依赖库: 无
功能:
    1. 获取视频列表
    2. 获取视频下载价格
消息说明:
    1. "AppSpider-0004-001" : 视频列表
    2. "AppSpider-0004-002" : 视频下载地址
"""

from lxml import etree
import scrapy
from appspider.commonapis import *

CONST_INFO = {
    'app_name': 'https://www.eporner.com',
    'app_version': '0.0.0',
    'spider_author': 'ddvv'
}


class EpornerSpider(scrapy.Spider):
    """
    Eporn爬虫
    """
    name = 'EpornerSpider'
    header = {
        'Host': 'www.eporner.com',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6,zh-TW;q=0.5',
    }

    # 爬虫入口，发起请求
    def start_requests(self):
        """

        """
        burl = 'https://www.eporner.com/search/chinese/'
        for i in range(1, 25):
            url = burl
            if i > 1:
                url = url + str(i) + '/'
            yield scrapy.Request(url=url,
                                 headers=self.header,
                                 method='GET',
                                 callback=self.parse_list)

    def parse_list(self, response):
        """

        :param response: 爬取的数据返回值。
        """
        try:
            ht = response.body.decode()
            tree = etree.HTML(ht)
            hrefs = tree.xpath('//div[@class="mb" or @class="mb hdy"]/a/@href')
            for href in hrefs:
                url = 'https://www.eporner.com' + href
                item = setappspideritem('AppSpider-0004-001', 'url', url, **CONST_INFO)
                yield item
                yield scrapy.Request(url=url,
                                     headers=self.header,
                                     method='GET',
                                     callback=self.parse_url)
        except Exception as e:
            logger.error(str(e))

    def parse_url(self, response):
        try:
            ht = response.body.decode()
            tree = etree.HTML(ht)
            # not gay
            namenode = tree.xpath('//div[@id="undervideomenu"]/h1/a')
            name = namenode[0].text
            hrefs = tree.xpath('//div[@id="hd-porn-dload"]/table/tr[last()]/td[2]/a/@href')
            for href in hrefs:
                url = 'https://www.eporner.com' + href
                data = {'name' : name, 'url': url}
                item = setappspideritem('AppSpider-0004-002', 'json', data, **CONST_INFO)
                yield item
        except Exception as e:
            logger.error(str(e))
