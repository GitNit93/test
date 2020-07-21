from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
driver.get("http://blueorchid.ghsdomain.com/")

login=driver.find_element_by_xpath('//*[@id="navbarNavDropdown"]/ul/li[8]/a').click()
time.sleep(5)


email=driver.find_element_by_xpath('//*[@id="login-modal"]/div/div/div[3]/div/div[1]/form/div[1]/input').send_keys('niteshinnovanda@gmail.com')

password=driver.find_element_by_xpath('//*[@id="login-modal"]/div/div/div[3]/div/div[1]/form/div[2]/input').send_keys('123456789')
submit=driver.find_element_by_xpath('//*[@id="login-modal"]/div/div/div[3]/div/div[1]/form/input').click()
time.sleep(5)



search=driver.find_element_by_xpath('//*[@id="btn-search-hotel"]').click()
#driver.maximize_window()
#driver.execute_script("window.scrollBy(0,200)", "")
time.sleep(3)


driver.find_element_by_xpath('//*[@id="seacrhResult"]/div/div[2]/div/div[2]/div[1]/div/div[2]/h4/a').click()
time.sleep(5)


allTabs = driver.window_handles
#print(allTabs)
for tab in allTabs:
    driver.switch_to.window(tab)
    #print(driver.current_url)
    if (driver.current_url=="http://blueorchid.ghsdomain.com/en/hotels/gb/london/london-tower-suites?location=All%20Blue%20Orchid%20Hotel&locationtype=Hotel&lid=0&checkin=18%20Jul%202020&checkout=19%20Jul%202020&RoomsSelector=1-0&rateaccesscode="):

     element=driver.find_element_by_xpath('//*[@id="modifytop"]/div[2]/div[1]/table/tbody/tr[1]/td[6]/select')
     time.sleep(4)
     drp=Select(element)
     drp.select_by_index(1)


driver.find_element_by_xpath('//*[@id="modifytop"]/div[2]/div[1]/table/tbody/tr[1]/td[7]/div/div/button').click()

driver.maximize_window()
driver.execute_script("window.scrollBy(0,300)", "")
time.sleep(3)
driver.find_element_by_xpath('//*[@id="enhance-stay"]/div/div[1]/div[2]/div/div[2]/div[4]/div[3]/form/div[2]/a').click()
driver.find_element_by_xpath('//*[@id="enhance-stay"]/div[1]/div[2]/div[1]/form/div/div[9]/div/div[2]/input').send_keys('test')

driver.execute_script("window.scrollBy(0,300)", "")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="enhance-stay"]/div[1]/div[2]/div[1]/form/div/div[15]/a/span').click()

time.sleep(3)
driver.switch_to.frame('_iframe_holder')
time.sleep(3)
driver.find_element_by_xpath('//*[@id="_el_input_nameoncard"]/input').send_keys('test')


#driver.find_element_by_xpath('//*[@id="_el_input_nameoncard"]/input').send_keys('123')
#driver.find_element_by_xpath('//*[@id="_el_input_nameoncard"]/input').send_keys('test')
driver.find_element_by_xpath('//*[@id="_el_input_cardnumber"]/input').send_keys('4444333322221111')
time.sleep(3)

driver.find_element_by_xpath('//*[@id="_el_input_expirationmonth"]/input').send_keys('12')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="_el_input_expirationyear"]/input').send_keys('2022')
time.sleep(2)

driver.find_element_by_xpath('//*[@id="_el_input_cvc"]/input').send_keys('1234')

driver.switch_to.default_content()
driver.find_element_by_xpath('//*[@id="address"]').send_keys('london')
time.sleep(2)

#driver.execute_script("window.scrollBy(0,200)", "")
driver.find_element_by_xpath('//*[@id="paymentForm"]/div[4]/input').click()

#time.sleep(5)