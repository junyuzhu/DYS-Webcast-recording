# -*- coding: utf-8 -*-
import time
import os
from urllib import request
import urllib.error

g_time = 1
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}

dysurl = "http://3954.liveplay.myqcloud.com/live/3954_497383565.flv"
testurl = "http://127.0.0.1:8990/"


def record():
    # 调用ffmpeg进行直播录像
    print("----正在录像中----")
    os.system("ffmpeg -i " + dysurl + " -c copy -f flv "
              ".//" + time.strftime('%Y%m%d%H%M%S',time.localtime())+".flv")
    print("----本次录像完毕----")


def request_link():
    # 请求直播间的推流连接，用来检测是否开播
    open_url = urllib.request.Request(url=dysurl, headers=headers)
    urllib.request.urlopen(open_url)


def main():
    # 程序从这开始执行
    global g_time
    # 用 global 修改全局变量
    while True:
        current_time = int(time.strftime('%H', time.localtime(time.time())))  # 获取当前系统时间单位为24小时制
        if current_time >= 12 or current_time < 3:  # 如果当前时间在设定的直播时间内，调用request_link函数
            try:
                request_link()
            except urllib.error.HTTPError as e:  # 如果是返回 HTTP/1.1 404 Not Found 表示并未开播
                time.sleep(1)
                # print("%d " % g_time)
                if g_time >= 3600:  # 重复检测30分钟后程序结束
                    break
                else:  # 每请求一次(一秒),记录一次
                    g_time += 1
            else:
                g_time = 1
                record()  # 如果返回 HTTP/1.1 200 OK 表示直播开启，调用录像函数
                print(time.ctime())
        else:
            print("现在时间是%d点, 并不是直播时间" % current_time)
            break


if __name__ == '__main__':
    main()
