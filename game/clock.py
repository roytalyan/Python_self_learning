# coding: utf-8

import os
import time
import logging

# print('==========1===========')
# abspath = os.getcwd()  # 获取当前路径
# rootpath = os.path.abspath('..')  # 获取上级路径
# print(abspath)
# print(rootpath)
#
# print('==========2===========')
# ret = abspath.replace(rootpath, '.', 1)
# print(ret)
# print('此路径是否为文件夹：%s' % os.path.isdir('../' + ret))

# def main():
#     content = 'this is a test......'
#     while True:
#         # 清理屏幕上的输出
#         os.system('cls')  # os.system('clear')
#         print(content)
#         # 休眠200毫秒
#         time.sleep(0.2)
#         content = content[1:] + content[0]
#
#
# if __name__ == '__main__':
#     main()

class Clock(object):
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        """初始化方法

        :param hour: 时
        :param minute: 分
        :param second: 秒
        """
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """显示时间"""
        return ' '*50 + ('%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second))


def main():
    h = time.strftime("%H", time.localtime())
    m = time.strftime("%M", time.localtime())
    s = time.strftime("%S", time.localtime())
    clock = Clock(int(h), int(m), int(s))
    while True:
        os.system('cls')
        print ('\n'*15)
        print(clock.show())
        time.sleep(1)
        clock.run()


if __name__ == '__main__':
    main()