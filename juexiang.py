#!/usr/local/bin/python3
# Copyright [c] 2016 By Ansion All rights Reserved.
import re
from pyquery import PyQuery as pq
import time
import mysql.connector as connector

#过滤html标签
def stripTag(x):
	return re.sub(r'<(.*?)>','',str(x))

#转换时间戳
def timeStamp(x):
	return time.mktime(time.strptime(x,'%Y-%m-%d %H:%M'))

#获取网页局部源码
d = pq(url='http://www.juexiang.com/list/1017')
d = pq(d('.left').html())
x = d('div.arttitle')

#匹配时间格式
pattern = re.compile(r"[0-9]{4}(.*)[0-9]{2}")

#采集网页信息
def get_content(x):
    a = pq(pq(x).html())
    title = stripTag(pq(a('a').eq(0).text()))
    author = stripTag(pq(a('a').eq(1).text()))
    time1 = str(pq(a('span').eq(2).text()))
    time1 = timeStamp((pattern.search(time1)).group())
    return title,author,time1

#连接mysql数据库
def connection():
    config = {
    'user': '',
    'password': '',
    'host': '',
    "port": 3306,
    'database': ''
	}
    # try:
    #     c = connector.connect(**config)
    #     return c
    # except:
    #     print("connection error")
    #     exit(1)

# cn = connection()
# cur = cn.cursor()

#for循环获取标题、作者、时间
for i in x:
    title,author,time1 = get_content(i)
    data = (title,author,time1,3,1)
    print(data)
    # cur.execute("insert into article (title,author,time,nav,state) values (%s,%s,%s,%s,%s)", data)

# cur.close()
# cn.close()
