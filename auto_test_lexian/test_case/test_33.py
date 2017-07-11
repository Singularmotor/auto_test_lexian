#coding=utf-8
from selenium import webdriver
import pymysql
import unittest,time
from selenium.webdriver.common.keys import Keys

print("test33")
wf = webdriver.Firefox()
mark_01=0
wf.get("http://192.168.17.66:8080/LexianManager/html/login.html")
wf.find_element_by_xpath(".//*[@id='login']").click()
time.sleep(1)
wf.find_element_by_xpath(".//*[@id='leftMenus']/div[8]/div[1]/div[2]/a[2]").click()
time.sleep(1)
wf.find_element_by_xpath(".//*[@id='leftMenus']/div[8]/div[2]/ul/li[2]/a").click()
wf.switch_to_frame("manager")
try:
    wf.find_element_by_xpath("html/body/div[1]/div/div[2]/span/input[1]").send_keys("13800138000")
    wf.find_element_by_xpath("html/body/div[1]/div/div[2]/span/span/a").click()
    time.sleep(1)
    mark_01=wf.find_element_by_xpath(".//*[@id='datagrid-row-r2-2-0']/td[1]/div").text
except:
    print("bank")
if  mark_01=="13800138000":
    print("pass")
else:
    print("fail")
wf.quit()

if __name__ == "__main__":
    unittest.main()