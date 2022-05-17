#!/usr/bin/python
#coding=utf-8

#导入用到的库
import logging,os

# 日志系统， 既要把日志输出到控制台， 还要写入日志文件
class Log():
    def __init__(self, logname, loglevel, logger, logdelete):
        #logdelete为0清理重写，1是不清理
        if(logdelete == 0):
            #删除日志文件，重新创建
            if(os.path.isfile(".//log//" + logname)):
                os.remove(".//log//" + logname)

        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(".//log//" + logname,encoding='utf-8')
        fh.setLevel(logging.DEBUG)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        #formatter = logging.Formatter('%(asctime)s--%(name)s - %(levelname)s - %(message)s')
        formatter = logging.Formatter('%(asctime)s--%(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger