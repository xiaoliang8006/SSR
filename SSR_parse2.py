# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 00:03:18 2019

@author: Administrator
"""
import base64
from PingIP import get_ping_result
from LocateIP import LocateIP

def parse(ssr):
   try:
        if ssr.startswith('ss://'):
           base64_encode_str = ssr[5:]
           server = parse_ss(base64_encode_str)
    
        if ssr.startswith('ssr://'):
           base64_encode_str = ssr[6:]
           server = parse_ssr(base64_encode_str)

        return server
   except:
       print("解析失败")
       return None
        


def parse_ss(base64_encode_str):
   decode_str = base64_decode(base64_encode_str)
   parts = decode_str.split(':')
   if len(parts) != 3:
       print('不能解析SS链接: %s' % base64_encode_str)
       return
   method = parts[0]
   password_and_ip = parts[1]
   port = parts[2]

   pass_and_server = password_and_ip.split('@')
   password = pass_and_server[0]
   server = pass_and_server[1]

   print('加密方法: %s, 密码: %s, server: %s, port: %s' % (method, password, server, port))
   return server

def parse_ssr(base64_encode_str):
   decode_str = base64_decode(base64_encode_str)
   print("decode_str:",decode_str)
   parts = decode_str.split(':')
   if len(parts) != 6:
       print('不能解析SSR链接: %s' % base64_encode_str)
       return

   server = parts[0]
   port = parts[1]
   protocol = parts[2]
   method = parts[3]
   obfs = parts[4]
   password_and_params = parts[5]
   print("password_and_params:",password_and_params)
   password_and_params = password_and_params.split("/?")

   password_encode_str = password_and_params[0]
   password = base64_decode(password_encode_str)
   print("password:",password)

   print('server: %s, port: %s, 协议: %s, 加密方法: %s, 密码: %s, 混淆: %s'
       % (server, port, protocol, method, password, obfs))
   return server

def fill_padding(base64_encode_str):

   need_padding = len(base64_encode_str) % 4 != 0

   if need_padding:
       missing_padding = 4 - need_padding
       base64_encode_str += '=' * missing_padding
   return base64_encode_str


def base64_decode(base64_encode_str):
   base64_encode_str = fill_padding(base64_encode_str)
   return base64.urlsafe_b64decode(base64_encode_str).decode('utf-8')


if __name__ == '__main__':
   ssr = input("输入SS或者SSR:")

   IP = parse(ssr)
   get_ping_result(IP)
   LocateIP(IP)
