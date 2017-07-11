#coding=utf-8
from selenium import webdriver
import pymysql
import unittest,time
from selenium.webdriver.common.keys import Keys

print("test35")
wf = webdriver.Firefox()
mark_01=0
n=0
wf.get("http://192.168.17.66:8080/LexianManager/html/login.html")
wf.find_element_by_xpath(".//*[@id='login']").click()
time.sleep(1)
wf.find_element_by_xpath(".//*[@id='leftMenus']/div[8]/div[1]/div[2]/a[2]").click()
time.sleep(1)
wf.find_element_by_xpath(".//*[@id='leftMenus']/div[8]/div[2]/ul/li[2]/a").click()
wf.switch_to_frame("manager")
wf.find_element_by_xpath("html/body/div[1]/div/div[2]/span/a/span/span[3]").click()
wf.find_element_by_xpath(".//*[@id='choice']/div[3]").click()
time.sleep(1)
wf.find_element_by_xpath("html/body/div[1]/div/div[2]/span/input[1]").send_keys("/LexianManager/login/login.do")
time.sleep(1)
wf.find_element_by_xpath("html/body/div[1]/div/div[2]/span/span/a").click()
time.sleep(1)
try:
    mark_01=wf.find_element_by_xpath(".//*[@id='datagrid-row-r2-2-0']/td[4]/div").text
except:
    print("bank")
if mark_01=="/LexianManager/login/login.do":
    print("pass")
else:
    print("fail")
wf.quit()

if __name__ == "__main__":
    unittest.main()