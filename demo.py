from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
driver.get("https://www.google.com/")


Print('hello')