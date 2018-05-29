# -*- coding: utf-8 -*-
# @Time    : 2018/5/28 15:04
# @Author  : ddvv
# @Site    : 
# @File    : getcomment.py
# @Software: PyCharm

import requests
from appspider.spiders.oppostorespider.protobuf import oppoStoreStruct_pb2


def main():
    headers = {
        'Referer': 'SM-G9350/appstore/4.6.2/869415177210521',
        'Ext-User': '-1/0/0',
        'brand': 'samsung',
        'locale': 'zh_CN',
        'uid': 'oppo.uid.nearme',
        'desktop': 'desktop_other',
        'Ext-System': 'SM-G9350/5.1.1/0/2/2/4.6.2/1',
        'User-Agent': 'SM-G9350/5.1.1/Market/4.6.2',
        'rom': '2',
        'VersionCode': '4605',
        'Connection': 'close',
        'Content-Type': 'application/octet-stream',
        'Accept-Encoding': 'gzip, deflate',
        'Screen': '1280#800',
        'ImgType': 'webp',
        'dataType': 'protobuf',
        'Host': 'i3.store.nearme.com.cn'
    }
    url = 'http://i3.store.nearme.com.cn/client/get_comments.pb'
    f = open('comments.txt', 'w')
    # 16520，当前已知的评论数
    for start in range(0, 16520, 20):
        cr = oppoStoreStruct_pb2.commentRequest()
        cr.userId = -1
        # 每次返回20条
        cr.size = 20
        # 起始偏移
        cr.start = 0
        cr.compress = 1
        # app ID，测试抖音
        cr.relateId = 20451860
        cr.source = 1
        cr.imei = '869415177210522'
        # 对数据进行序列化
        endata = cr.SerializeToString()
        # 发起请求
        rs = requests.post(url=url, headers=headers, data=endata)
        dedata = rs.content
        target = oppoStoreStruct_pb2.commentlist()
        # 反序列化
        target.ParseFromString(dedata)
        # 以str方式保存到文件
        f.write(str(target))
        f.flush()
        print(start)
    f.close()


if __name__ == "__main__":
    main()
