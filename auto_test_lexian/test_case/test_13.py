#coding=utf-8
from selenium import webdriver
import pymysql
import unittest,time
from selenium.webdriver.common.keys import Keys

print("test13")
wf = webdriver.Firefox()
ps=pymysql
bp=ps.connect(host='192.168.17.66',port=3306,user='root',passwd='123456',db='lexian',charset='utf8')
#connect to the database ,if you want to use chinese in you request on pymysql, please type charset='utf8' at last
res=bp.cursor()
mark_01=0
wf.get("http://192.168.17.66:8080/LexianManager/html/login.html")
wf.find_element_by_xpath(".//*[@id='login']").click()
time.sleep(1)
wf.find_element_by_xpath(".//*[@id='leftMenus']/div[2]/div[1]/div[2]/a[2]").click()
time.sleep(1)
wf.find_element_by_xpath(".//*[@id='leftMenus']/div[2]/div[2]/ul/li/a").click()
time.sleep(1)
wf.switch_to_frame("manager")
try:
    wf.find_element_by_xpath(".//*[@id='content']/div/div/div[2]/table/tbody/tr/td[7]/input").clear()
    wf.find_element_by_xpath(".//*[@id='content']/div/div/div[2]/table/tbody/tr/td[7]/input").send_keys("3")
    time.sleep(1)
    wf.find_element_by_xpath(".//*[@id='content']/div/div/div[2]/table/tbody/tr/td[7]/input").send_keys(Keys.ENTER)
    time.sleep(1)
    mark_01=wf.find_element_by_xpath(".//*[@id='datagrid-row-r1-1-0']/td/div").text
except:
    print("bank")
if mark_01=="45":
    print("pass")
else:
    print("fail")
wf.quit()

if __name__ == "__main__":
    unittest.main()