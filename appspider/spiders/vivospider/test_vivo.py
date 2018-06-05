# -*- coding: utf-8 -*-
# @Time    : 2018/6/1 16:44
# @Author  : ddvv
# @Site    : 
# @File    : test_vivo.py
# @Software: PyCharm


import requests
import time
import random


def vivo_encode(data, data_len):
    tables = 'Q8vN-ryaEJGoTWOtK_qMkh5RZ6LxcUA3dnzeHu2XjSbVsFYwfPD94C0lm1Ip7gBi'
    r_len = 2 * data_len
    result = [0] * r_len
    origin_pos = 0
    out_pos = 0
    for i in range(0, r_len, 4):
        if data_len - origin_pos <= 2:
            break
        result[i] = tables[(ord(data[origin_pos]) >> 2) & 0xff]
        result[i + 1] = tables[((ord(data[origin_pos + 1]) >> 4) | 16 * ord(data[origin_pos]) & 0x30) & 0xff]
        result[i + 2] = tables[((ord(data[origin_pos + 2]) >> 6) | 4 * ord(data[origin_pos + 1]) & 0x3c) & 0xff]
        result[i + 3] = tables[ord(data[origin_pos + 2]) & 0x3f]
        origin_pos += 3
        out_pos += 4
    end = out_pos
    if data_len - origin_pos > 0:
        result[out_pos] = tables[(ord(data[origin_pos]) >> 2) & 0xff]
        if data_len - origin_pos == 2:
            result[out_pos + 1] = tables[(16 * ord(data[origin_pos]) & 0x30 | ord(data[origin_pos + 1]) >> 4) & 0xff]
            result[out_pos + 2] = tables[4 * ord(data[origin_pos + 1]) & 0x3c]
            end = out_pos + 2
        else:
            result[out_pos + 1] = tables[16 * ord(data[origin_pos]) & 0x30]
            end = out_pos + 1

    return ''.join(result[:end])


def vivo_decode(data, data_len):
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
    result = [0] * data_len
    origin_pos = 0
    out_pos = 0
    end = 0
    for i in range(0, data_len, 3):
        out_pos = data_len - origin_pos
        if out_pos <= 3:
            break
        result[i] = ((tables[ord(data[origin_pos + 1])] >> 4) & 3 | 4 * tables[ord(data[origin_pos])]) & 0xff
        result[i + 1] = (tables[ord(data[origin_pos + 2])] >> 2 & 0xf | 16 * tables[ord(data[origin_pos + 1])]) & 0xff
        result[i + 2] = (tables[ord(data[origin_pos + 2])] << 6 | tables[ord(data[origin_pos + 3])]) & 0xff
        origin_pos += 4
        end = i + 3
    if out_pos == 1:
        tmp = (4 * tables[ord(data[origin_pos])]) & 0xff
        if tmp:
            result[end] = tmp
    elif out_pos == 2:
        result[end] = ((tables[ord(data[origin_pos + 1])] << 26 >> 30) | 4 * tables[ord(data[origin_pos])]) & 0xff
        tmp = (16 * tables[ord(data[origin_pos + 1])]) & 0xff
        if tmp:
            result[end + 1] = tmp
        end += 1
    elif out_pos == 3:
        result[end] = ((tables[ord(data[origin_pos + 1])] >> 4) & 3 | 4 * tables[ord(data[origin_pos])]) & 0xff
        result[end + 1] = ((tables[ord(data[origin_pos + 2])] << 26 >> 28) | 16 * tables[
            ord(data[origin_pos + 1])]) & 0xff
        tmp = (tables[ord(data[origin_pos + 2])] << 6) & 0xff
        if tmp:
            result[end + 2] = tmp
        end += 2

    str_out = bytearray(result[:end])
    return str_out.decode('utf8')


def work():
    burl = 'http://pl.appstore.vivo.com.cn/port/comments/?param={param}&jvq=1.0.9'
    headers = {
        'Accept-Encoding': 'gzip, deflate',
        'Host': 'pl.appstore.vivo.com.cn',
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.2) Gecko/20100115 Firefox/3.6',
    }
    f = open('vivo_comments.txt', 'w', encoding='utf8')
    for page_index in range(1, 50):
        param = 'apps_per_page=41&screensize=1080_1812&pictype=webp&appversioncode=621&u=1234567890&cur=0&plat_key_ver=&imei=863336037384660&appversion=6.2.1&id=696&nt=WIFI&platApkVer=0&showDefault=0&build_number=NXT-AL10C00B577&elapsedtime=69148469&plateformVersionName=null&cs=0&density=3.0&av=24&an=7.0&plateformVersion=0&platApkVerName=null&app_version=1146&page_index={page_index}&target=local&model=HUAWEI+NXT-AL10&s=2%7C2631655377&jvq_type=0'.format(
            page_index=page_index)
        sleep_time = random.randint(10, 20)
        print('page : %d, sleep : %d' % (page_index, sleep_time))
        url = burl.format(param=vivo_encode(param, len(param)))
        rs = requests.get(url=url, headers=headers)
        f.write(vivo_decode(rs.text, len(rs.text)))
        f.flush()
        time.sleep(sleep_time)
    f.close()


def main():
    work()


if __name__ == "__main__":
    main()
