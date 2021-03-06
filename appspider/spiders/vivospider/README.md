VIVO应用市场爬虫
===

vivo应用市场关键数据采用二次加密，需要还原加解密算法。

## 加密函数
类似base64变形算法，更换了码表，码表如下：

```
tables = 'Q8vN-ryaEJGoTWOtK_qMkh5RZ6LxcUA3dnzeHu2XjSbVsFYwfPD94C0lm1Ip7gBi'
```

## 解密函数
码表如下：

```
tables = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF,
              0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF,
              0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF,
              0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF,
              0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF,
              0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 4, 0xFFFFFFFF, 0xFFFFFFFF, 0x36, 0x39, 0x26,
              0x1F, 0x34, 0x16, 0x19, 0x3C, 1, 0x33, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF,
              0xFFFFFFFF, 0xFFFFFFFF, 0x1E, 0x3E, 0x35, 0x32, 8, 0x2D, 0xA, 0x24, 0x3A, 9, 0x10, 0x1A, 0x13, 3, 0xE,
              0x31, 0, 0x17, 0x29, 0xC, 0x1D, 0x2B, 0xD, 0x27, 0x2E, 0x18, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF,
              0xFFFFFFFF, 0x11, 0xFFFFFFFF, 7, 0x2A, 0x1C, 0x20, 0x23, 0x30, 0x3D, 0x15, 0x3F, 0x28, 0x14, 0x37, 0x38,
              0x21, 0xB, 0x3B, 0x12, 5, 0x2C, 0xF, 0x25, 2, 0x2F, 0x1B, 6, 0x22, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF,
              0xFFFFFFFF, 0xFFFFFFFF, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

## 通信接口
host：

```
http://pl.appstore.vivo.com.cn
```

header：

```
    headers = {
        'Accept-Encoding': 'gzip, deflate',
        'Host': 'pl.appstore.vivo.com.cn',
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.2) Gecko/20100115 Firefox/3.6',
    }
```

## 示例代码
[完整代码](./test_vivo.py)

## 运行
结果保存在当前目录的`comments.txt`中