# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 10:15:58 2019

@author: Administrator
"""

# -*- coding: utf-8 -*-
 
import subprocess
import re
 
def get_ping_result(ip_address):
    try:
        if ip_address == None:
            return
        p = subprocess.Popen(["ping.exe", ip_address], stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True)
        out = p.stdout.read().decode('gbk')
      
        reg_receive = '已接收 = \d'
        match_receive = re.search(reg_receive, out)
      
        receive_count = -1
      
        if match_receive:
            receive_count = int(match_receive.group()[6:])
      
        if receive_count > 0: #接受到的反馈大于0，表示网络通
            reg_min_time = '最短 = \d+ms'
            reg_max_time = '最长 = \d+ms'
            reg_avg_time = '平均 = \d+ms'
       
            match_min_time = re.search(reg_min_time, out)
            min_time = int(match_min_time.group()[5:-2])
       
            match_max_time = re.search(reg_max_time, out)
            max_time = int(match_max_time.group()[5:-2])
       
            match_avg_time = re.search(reg_avg_time, out)
            avg_time = int(match_avg_time.group()[5:-2])
      
            print("平均时间:",avg_time,"ms  ",end="")
        else:
            print('网络不通，目标服务器不可达！  ',end="")
    
    except:
        print("ping失败  ",end="")
        
   
if __name__ == '__main__':
    IP = None
    get_ping_result(IP)
