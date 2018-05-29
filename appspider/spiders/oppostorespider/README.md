oppo应用市场爬虫
===

oppostore采用gRPC通信协议，通信数据采用protobuf规范进行序列化。

## 外部依赖工具
* google的工具[protobuf](https://github.com/google/protobuf/releases)
下载需要的版本，将protoc.exe添加环境变量，查看帮助信息，支持以下语言：

```
> protoc.exe -h
...
  --cpp_out=OUT_DIR           Generate C++ header and source.
  --csharp_out=OUT_DIR        Generate C# source file.
  --java_out=OUT_DIR          Generate Java source file.
  --javanano_out=OUT_DIR      Generate Java Nano source file.
  --js_out=OUT_DIR            Generate JavaScript source.
  --objc_out=OUT_DIR          Generate Objective C header and source.
  --php_out=OUT_DIR           Generate PHP source file.
  --python_out=OUT_DIR        Generate Python source file.
  --ruby_out=OUT_DIR          Generate Ruby source file.
...
```
本例中，使用python作为开发语言，**切换**到`oppoStoreStruct.proto`所在目录，执行如下命令，生成`oppoStoreStruct_pb2.py`脚本，即可使用该脚本进行开发：

```
> protoc.exe --python_out=. oppoStoreStruct.proto
```

## 重点：
1. 通信协议数据结构体的还原
2. 通信协议接口分析

## 结构体还原
经过逆向，结构体保存在`oppoStoreStruct.proto`文件中：

```
syntax = "proto3";
package protobuf;

message commentRequest{
    int32 userId = 1;
    int32 os = 2;
    int32 size = 3;
    int32 start = 4;
    string mobile = 5;
    int32 orderBy = 6;
    int32 categoryId = 7;
    int32 themeVersion = 8;
    int32 platform = 9;
    int32 compress = 10;
    int32 resType = 11;
    int64 relateId = 12;
    string keyword = 13;
    string screen = 14;
    int32 source = 15;
    string userToken = 16;
    int32 randomCount = 17;
    string imei = 18;
    int32 searchType = 19;
    string imsi = 20;
    string net = 21;
    int32 pageNo = 22;
    string package = 23;
}

message commentItem {
    int32 id = 1;
    int32 userId = 2;
    string userNickName = 3;
    string word = 4;
    int64 createTime = 5;
    double userGrade = 6;
    int32 state = 7;
    string userIp = 8;
    string imei = 9;
    string version = 10;
    int32 isMobile = 11;
    int32 platform = 12;
    int32 orderIndex = 13;
    string mobileName = 14;
    int64 productId = 15;
    int64 masterId = 16;
    string userToken = 17;
    int32 replyId = 18;
    string reply = 19;
    int64 subjectId = 20;
    int32 isSendPoints = 21;
    int32 Count = 22;
}

message commentlist {
    int64 productId = 1;
    int32 total = 2;
    int32 start = 3;
    int32 end = 4;
    repeated commentItem comment = 5;
    int32 gradeNum = 6;
    string startsRate = 7;
    int64 masterId = 8;
    commentItem userComment = 9;
    repeated commentItem topComment = 10;
}
```
* commentRequest：request中，body结构体
* commentItem ：response中，单条评论的结构体
* commentlist ：response中，评论列表的结构体

## 通信接口
评论接口：
url：

```
http://i3.store.nearme.com.cn/client/get_comments.pb
```

header：

```
headers = {
        'Referer': 'SM-G9350/appstore/4.6.2/869415177220521',
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

```
body:

```
        cr = oppoStoreStruct_pb2.commentRequest()
        cr.userId = -1
        # 每次返回20条
        cr.size = 20
        # 起始偏移
        cr.start = 0
        cr.compress = 1
        # app ID
        cr.relateId = 20451860
        cr.source = 1
        cr.imei = '869415177220522'
        # 对数据进行序列化
        endata = cr.SerializeToString()

```
## 示例代码
[完整代码](./protobuf/getcomment.py)

## 运行

```
> python.exe .\getcomment.py
```
评论保存在当前目录的`comments.txt`中