#coding=utf-8
from selenium import webdriver
import pymysql
import unittest,time
wf = webdriver.Firefox()
def adduser(num,name):
    wf.get("http://192.168.17.66:8080/LexianMall/sc/login.html")
    #前面更改你主机所在ip
    wf.refresh()
    time.sleep(1)
    wf.find_element_by_xpath(".//*[@id='wrapper']/div[2]/div/div[2]/div/div/div[1]/a").click()
    time.sleep(2)
    wf.find_element_by_xpath(".//*[@id='phone']").send_keys(num)
    wf.find_element_by_xpath(".//*[@id='username']").send_keys(name)
    wf.find_element_by_xpath(".//*[@id='password']").send_keys("123456")
    wf.find_element_by_xpath(".//*[@id='surepassword']").send_keys("123456")
    time.sleep(1)
    wf.find_element_by_xpath(".//*[@id='submit']").click()
    time.sleep(2)
    return

#可用xlsx表格生成，也可应用循环来自动填写账号手机和用户名
adduser("18800188601","test001")
adduser("18800188602","test002")
adduser("18800188603","test003")
adduser("18800188604","test004")
adduser("18800188605","test005")
adduser("18800188606","test006")
adduser("18800188607","test007")
adduser("18800188608","test008")
adduser("18800188609","test009")
adduser("18800188610","test010")
adduser("18800188611","test011")
adduser("18800188612","test012")
adduser("18800188613","test013")
adduser("18800188614","test014")
adduser("18800188615","test015")
adduser("18800188616","test016")
adduser("18800188617","test017")
adduser("18800188618","test018")
adduser("18800188619","test019")
adduser("18800188620","test020")

