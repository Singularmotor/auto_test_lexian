#coding=utf-8
from selenium import webdriver
import pymysql
import unittest,time
from selenium.webdriver.common.keys import Keys

print("test19")
wf = webdriver.Firefox()
mark_01=0
mark_02=0
wf.get("http://192.168.17.66:8080/LexianManager/html/login.html")
wf.find_element_by_xpath(".//*[@id='login']").click()
time.sleep(1)
wf.find_element_by_xpath(".//*[@id='leftMenus']/div[8]/div[1]/div[2]/a[2]").click()
time.sleep(1)
wf.find_element_by_xpath(".//*[@id='leftMenus']/div[8]/div[2]/ul/li[1]/a").click()
wf.switch_to_frame("manager")
try:
    mark_01=wf.find_element_by_xpath("html/body/div[1]/div/div[1]/span[4]").text
except:
    print("bank")
if mark_01=="app版本管理":
    print("pass")
else:
    print("fail")
wf.quit()

if __name__ == "__main__":
    unittest.main()