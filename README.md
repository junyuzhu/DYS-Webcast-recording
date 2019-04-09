# DYS-Webcast-recording
录制德云色的直播
<br>
使用python3 + ffmpeg 实现对直播流的录像
<br>
录像文件为flv格式,如:(20190408211730.flv)
<br>

<br>
初次运行时需要自己配置录像存放的本地地址
<br>
<h2>Linux平台</h2>
<i>record.py</i>为linux下的程序 
<br>执行命令为 python3 record.py
<br>
需要预先安装python3与 ffmpeg
<br>
<i>record.py</i>

目前已实现的功能
<br>
1.可调录像的工作时间，当设定非直播时间开启程序会程序会自动关闭
<br>
2.自动检测开播后会自动录制
<br>
3.当程序运行超过30分钟后，直播还未开启，程序自动结束
<br>
4.录制文件以时间命名(%Y%m%d%H%M%S)
<br>
5.修改请求的User-Agent
<br>
6.在直播时间内，断开直播后会继续检测30分钟(针对调码率,改延迟,修电脑添加),继续开播后再进行录制
<br>
7.录像的码率根据当前的推流的码率而定
<br>
8.按键盘的q键分P
<br>

<br><br>
<h2>windows平台(使用标题命令行或者power shell运行)</h2>
<br>
<i>rec_in_win.py</i>为window平台下的录制程序，需要存放于与bin/ffmpeg.exe同一个文件夹下，并且录制的视频存放于此文件夹里。
<br>
ffmpeg的下载地址为:<a href="https://ffmpeg.zeranoe.com/builds/">选择Architecture的x64-bit or x32-bit</a>
<br>
命令为：python .\rec_in_win.py
<br>
提示，window下录像文件需要停止写入当前文件后录像文件才会再文件管理器显示文件大小,不停止的话一直会显示大小未0kb
<br>
一些bug
<br>
1.调用的ffmpeg录制会出现卡住，这么久出先过3次,未得出是网络问题还是ffmpeg的问题
<br>
