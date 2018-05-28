# -*- coding: utf-8 -*-
# @Time    : 2018/5/25 11:06
# @Author  : ddvv
# @Site    : 
# @File    : test.py
# @Software: PyCharm

from appspider.spiders.oppostorespider.protobuf import oppoStoreStruct_pb2


cr = oppoStoreStruct_pb2.commentRequest()
cr.userId = -1
cr.size = 20
cr.start = 280
cr.compress = 1
cr.relateId = 20397032
cr.source = 1
cr.imei = '869415177220522'
# 对数据进行序列化
data = cr.SerializeToString()
print(data)

# 对已经序列化的数据进行反序列化
# with open('response.pb', 'rb') as f:
#     data = f.read()
# target = oppoStoreStruct_pb2.commentlist()
# target.ParseFromString(data)
# print(target)


# 对已经序列化的数据进行反序列化
with open('request15.pb', 'rb') as f:
    data = f.read()
print(data)
target1 = oppoStoreStruct_pb2.commentRequest()
target1.ParseFromString(data)
print(target1)