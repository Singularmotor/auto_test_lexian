#coding=utf-8
from selenium import webdriver
import pymysql
import unittest,time
from selenium.webdriver.common.keys import Keys

print("test17")
wf = webdriver.Firefox()
ps=pymysql
bp=ps.connect(host='192.168.17.66',port=3306,user='root',passwd='123456',db='lexian',charset='utf8')
#connect to the database ,if you want to use chinese in you request on pymysql, please type charset='utf8' at last
res=bp.cursor()
mark_01=0
mark_02=0

def login(ph,pw):
    wf.get("http://192.168.17.66:8080/LexianMall/sc/login.html")
    wf.find_element_by_xpath(".//*[@id='username']").send_keys(ph)
    wf.find_element_by_xpath(".//*[@id='password']").send_keys(pw)
    wf.find_element_by_xpath(".//*[@id='submit']").click()
    return

wf.get("http://192.168.17.66:8080/LexianManager/html/login.html")
wf.find_element_by_xpath(".//*[@id='login']").click()
time.sleep(1)
wf.find_element_by_xpath(".//*[@id='leftMenus']/div[2]/div[1]/div[2]/a[2]").click()
time.sleep(1)
wf.find_element_by_xpath(".//*[@id='leftMenus']/div[2]/div[2]/ul/li/a").click()
time.sleep(1)
wf.switch_to_frame("manager")
try:
    wf.find_element_by_xpath(".//*[@id='datagrid-row-r1-2-0']/td[5]/div/span/a").click()
    time.sleep(1)
    wf.find_element_by_xpath(".//*[@id='content']/div/div/div[2]/table/tbody/tr/td[13]/a/span/span[2]").click()
    time.sleep(1)
    mark_01=wf.find_element_by_xpath(".//*[@id='datagrid-row-r2-2-0']/td[4]/div/span").text
except:
    print("bank")
if mark_01=="禁用":
    login("18800188612","123456")
    time.sleep(1)
    try:
        mark_02=wf.find_element_by_xpath(".//*[@id='asynctips_error_content']").text
    except:
        print("fail")
    if mark_02=="用户被冻结":
        print("pass")
else:
    print("fail")

wf.get("http://192.168.17.66:8080/LexianManager/html/login.html")
wf.find_element_by_xpath(".//*[@id='login']").click()
time.sleep(1)
wf.find_element_by_xpath(".//*[@id='leftMenus']/div[2]/div[1]/div[2]/a[2]").click()
time.sleep(1)
wf.find_element_by_xpath(".//*[@id='leftMenus']/div[2]/div[2]/ul/li/a").click()
time.sleep(1)
wf.switch_to_frame("manager")
wf.find_element_by_xpath(".//*[@id='datagrid-row-r1-2-0']/td[5]/div/span/a").click()
#reset the user's function
wf.quit()
if __name__ == "__main__":
    unittest.main()