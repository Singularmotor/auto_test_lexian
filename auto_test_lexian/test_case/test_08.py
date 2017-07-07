#coding=utf-8
from selenium import webdriver
import pymysql
import unittest,time

print("test08")
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
    wf.find_element_by_xpath(".//*[@id='leftMenus']/div[2]/div[1]/div[2]/a[2]").click()
    time.sleep(1)
    mark_01=wf.find_element_by_xpath(".//*[@id='leftMenus']/div[2]/div[2]/ul/li/a").text
except:
    print("bank")
time.sleep(1)
wf.find_element_by_xpath(".//*[@id='leftMenus']/div[2]/div[1]/div[2]/a[2]").click()
time.sleep(1)
try:
    wf.find_element_by_xpath(".//*[@id='leftMenus']/div[2]/div[2]/ul/li/a").click()
except:
    mark_02=1
if mark_01=="查看会员信息" and mark_02==1:
    print("pass")
else:
    print("fail")
wf.close()

if __name__ == "__main__":
    unittest.main()