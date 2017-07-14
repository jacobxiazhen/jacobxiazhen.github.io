# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 10:22:15 2017

@author: zxia
"""

import requests
from bs4 import BeautifulSoup #导入包
import dryscrape

url="http://www.ziyoubaba.com/2016/05/29/python_catch_js"

#传统方式抓取页面
def get_url_code(url):
    #声明header，伪装成浏览器
    headers={"user-agent":"Mozilla/5.0 (windows NT6.1;WOW64 ; rv:42 ) Gecko/20100101 Firefox/42.0"}
    session_req=requests.session() #构造一个兼容cookie的请求
    req=session_req.get(url=url,headers=headers) #向url发送get请求，获取整个页面
    req.encoding="utf-8" #指定页面的编码
    #print(req.text) #将页面的源代码输出到屏幕
    return req.text #返回页面的源代码

def get_text_line(html):
    soup=BeautifulSoup(html,'lxml')
    text_line=soup.find('span',id='text_line') #找到id='text_line'的span标签
    print(text_line.text) #打印出来该span标签的文本
#执行一下看看效果如何
get_text_line(get_url_code(url)) #将输出一条文本

def get_url_dynamic(url):
    session_req=dryscrape.Session()
    session_req.visit(url) #请求页面
    response=session_req.body() #网页的文本
    #print(response)
    return response
get_text_line(get_url_dynamic(url)) #将输出一条文本