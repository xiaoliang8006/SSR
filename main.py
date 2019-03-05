# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 11:10:02 2019

@author: Administrator
"""
import sys
from SSR_parse2 import parse
from PingIP import get_ping_result
from LocateIP import LocateIP

#log
class Logger(object):
    def __init__(self,fileN ="Default.log"):
        self.terminal = sys.stdout
        self.log = open(fileN,"w")
    def write(self,message):
        self.terminal.write(message)
        self.log.write(message)
    def flush(self):
        pass
sys.stdout = Logger("result.txt") 
#下面所有的方法，只要控制台输出，都将写入"result.txt"


country=[]
for line in open("SSR.txt","r"): #设置文件对象并读取每一行文件
    temp=line.split('\t')
    print("\n第",temp[0],"个:")
    ssr = temp[1][:-1]
    print(ssr)
    
    IP = parse(ssr)
    get_ping_result(IP)
    location = LocateIP(IP)
    country.append(location)

#print(country)

country_set = set(country) 
for item in country_set: 
    print("%s 有 %d 个" %(item,country.count(item)))


 