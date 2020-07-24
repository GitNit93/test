from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select




driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")

driver.get('http://demo:Test@123@test.bookingclap.com/en/index.html')
driver.maximize_window()

elem = driver.find_element_by_xpath('//*[@id="home"]/form/div[1]/div/div[1]/div[1]/input[2]')
elem.send_keys('london')
#elem=input('enter location') #for dynamic sea0rch

time.sleep(2)

#elem.send_keys(Keys.DOWN)
elem.send_keys(Keys.TAB)
#sleep(2)
elem.send_keys(Keys.TAB)
time.sleep(2)

searchBox = driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[5]/td[5]/a')
searchBox.send_keys(Keys.ENTER)
#sleep(2)
searchBtn = driver.find_element_by_xpath('//*[@id="btn-search-hotel"]')
searchBtn.click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="booknowbtn_10498"]').click()

allTabs = driver.window_handles
#print(allTabs)
for tab in allTabs:
    driver.switch_to.window(tab)
    #print(driver.current_url)
    if (driver.current_url== "http://test.bookingclap.com/en/hotels/gb/london/london-tower-suites?location=London,%20Greater%20London,%20United%20Kingdom&locationtype=Hotel&lid=2&checkin=30%20Jul%202020&checkout=31%20Jul%202020&RoomsSelector=1-0&rateaccesscode=#choose-room"):

      #element=driver.find_element_by_xpath('//*[@id="choose-room"]/div[1]/div[1]/div/div/div[1]/div[3]/table/tbody/tr[1]/td[6]/select')
      element=driver.find_element_by_xpath('//*[@id="choose-room"]/div[1]/div[1]/div/div/div[1]/div[3]/table/tbody/tr[3]/td[6]/select')
      time.sleep(4)
      drp=Select(element)
      drp.select_by_index(1)



driver.find_element_by_xpath('//*[@id="choose-room"]/div[1]/div[1]/div/div/div[1]/div[3]/table/tbody/tr[1]/td[7]/div/button').click()

driver.execute_script("window.scrollBy(0,300)", "")
time.sleep(3)
driver.find_element_by_xpath('//*[@id="enhance-stay"]/div/div[1]/div[2]/div/div/div/div[7]/div/a').click()

driver.find_element_by_xpath('//*[@id="btncontinue"]').click()

#driver.execute_script("window.scrollBy(0,300)", "")
time.sleep(2)

driver.find_element_by_xpath('//*[@id="enhance-stay"]/div[1]/div[3]/div[1]/div[1]/div[2]/form/div[2]/div/div[2]/input').send_keys('test')

driver.find_element_by_xpath('//*[@id="enhance-stay"]/div[1]/div[3]/div[1]/div[1]/div[2]/form/div[4]/div/div[2]/input').send_keys('auto')
driver.find_element_by_xpath('//*[@id="enhance-stay"]/div[1]/div[3]/div[1]/div[1]/div[2]/form/div[5]/div/div[2]/input').send_keys('niteshinnovanda@gmail.com')
driver.find_element_by_xpath('//*[@id="enhance-stay"]/div[1]/div[3]/div[1]/div[1]/div[2]/form/div[6]/div/div[2]/input').send_keys('123333')
driver.find_element_by_xpath('//*[@id="enhance-stay"]/div[1]/div[3]/div[1]/div[1]/div[2]/form/div[8]/div/div[2]/input').send_keys('test')
driver.find_element_by_xpath('//*[@id="enhance-stay"]/div[1]/div[3]/div[1]/div[1]/div[2]/form/div[9]/div/div[2]/textarea').send_keys('london')

driver.execute_script("window.scrollBy(0,400)", "")

driver.find_element_by_xpath('//*[@id="enhance-stay"]/div[1]/div[3]/div[1]/div[1]/div[2]/form/div[10]/div/div[2]/input').send_keys('london')
country=driver.find_element_by_xpath('//*[@id="enhance-stay"]/div[1]/div[3]/div[1]/div[1]/div[2]/form/div[11]/div/div[2]/select')
time.sleep(4)
dropdown=Select(country)
dropdown.select_by_index(1)

driver.find_element_by_xpath('//*[@id="enhance-stay"]/div[1]/div[3]/div[1]/div[1]/div[2]/form/div[12]/div/div[2]/input').send_keys('32165')
driver.find_element_by_xpath('//*[@id="enhance-stay"]/div[1]/div[3]/div[1]/div[1]/div[2]/form/div[13]/div/div/textarea').send_keys('test request')

status=driver.find_element_by_xpath('//*[@id="enhance-stay"]/div[1]/div[3]/div[1]/div[1]/div[2]/form/div[14]/div/div[2]/div/input[1]').is_selected()
driver.find_element_by_xpath('//*[@id="enhance-stay"]/div[1]/div[3]/div[1]/div[1]/div[2]/form/div[14]/div/div[2]/div/input[1]').click()

driver.find_element_by_xpath('//*[@id="enhance-stay"]/div[1]/div[3]/div[1]/div[1]/div[2]/form/div[16]/a/span').click()
time.sleep(2)
card=driver.find_element_by_xpath('//*[@id="enhance-stay"]/div[2]/div[1]/div[1]/form/div[2]/div/div[1]/div/div/select')
time.sleep(4)
maestro=Select(card)
maestro.select_by_index(2)

driver.find_element_by_xpath('//*[@id="enhance-stay"]/div[2]/div[1]/div[1]/form/div[2]/div/div[2]/div/div/input').send_keys('5555555555554444')
time.sleep(2)
month=driver.find_element_by_xpath('//*[@id="ExpiryMonth"]')
time.sleep(4)
cardmonth=Select(month)
cardmonth.select_by_index(3)

time.sleep(2)

year=driver.find_element_by_xpath('//*[@id="ExpiryYear"]')
time.sleep(4)
yearmonth=Select(year)
yearmonth.select_by_index(3)
time.sleep(4)

driver.find_element_by_xpath('//*[@id="enhance-stay"]/div[2]/div[1]/div[1]/form/div[2]/div/div[5]/div/div/input').send_keys('test')
time.sleep(2)

driver.find_element_by_xpath('//*[@id="enhance-stay"]/div[2]/div[1]/div[1]/form/div[2]/div/div[6]/div/div/input').send_keys('123')

time.sleep(4)
driver.find_element_by_xpath('//*[@id="enhance-stay"]/div[2]/div[1]/div[1]/form/div[6]/a').click()

time.sleep(3)
driver.find_element_by_xpath('//*[@id="body"]/div[3]/section[2]/div[1]/a').click()


cancelTabs = driver.window_handles
for cancel in cancelTabs:
    driver.switch_to.window(cancel)
    print(driver.current_url)
    if(driver.current_url=="http://test.bookingclap.com/en/order/managebooking?Key=IosV4zsPnZ2kNytWZh_etPkYeEpMN937nyD3QTlkzluBVYn2zk0H9Sbz7mmffGfut4KJPG32ovoEg4CxORjdGlYSj3NYD-m2D80uC4iRud6HbmAEnYkZR7Coa8aAeIl0"):

     time.sleep(5)
     driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/div[1]/div[1]/div[1]/div[1]/div[2]/div/a[3]').click()