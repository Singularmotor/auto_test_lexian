#coding=utf-8
from selenium import webdriver
import pymysql
import unittest,time

print("test01")
wf = webdriver.Firefox()
ps=pymysql
bp=ps.connect(host='192.168.17.66',port=3306,user='root',passwd='123456',db='lexian',charset='utf8')
#connect to the database ,if you want to use chinese in you request on pymysql, please type charset='utf8' at last
res=bp.cursor()
mark_01=0
mark_02=0
try:
    wf.get("http://192.168.17.66:8080/LexianManager/html/login.html")
    wf.find_element_by_xpath(".//*[@id='login']").click()
    time.sleep(1)
    mark_01=wf.find_element_by_xpath(".//*[@id='left']/div[1]/div[3]/a").text
    #get the identify mark of web page
    mark_02=wf.find_element_by_xpath(".//*[@id='userName']").text
except:
    print("bank")
if mark_01=="退出登录" and mark_02=="13800138000":
    print("pass")
else:
    print("fail")
wf.close()

if __name__ == "__main__":
    unittest.main()