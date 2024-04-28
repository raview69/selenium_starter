from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from termcolor import colored



position = 5
data = []

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ['enable-automation'])
driver = webdriver.Chrome(service=Service(""),
options=options)
action = ActionChains(driver)
url = 'https://www.binance.com/en/futures/NEARUSDT'
driver.get(url)
driver.maximize_window()
sleep(10)
# openPrice = driver.find_element('xpath', '//*[@id="futuresOrderbook"]/div[3]/div[2]/div[1]').text

# # driver.find_element('xpath', '//*[@id="server-side"]/div/div[2]/div[1]/div/div[4]/div[2]/form/div/div[1]/div[3]/div[1]/div/div/div[9]').click()
# action.double_click(driver.find_element('xpath', '/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[1]/div/div[4]/div[2]/form/div/div[1]/div[1]/div[1]/div/div/input')).perform()
# # driver.find_element('xpath', '/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[1]/div/div[4]/div[2]/form/div/div[1]/div[1]/div[1]/div/div/input').click()
# # toClear.send_keys(Keys.CONTROL + "a")
# # toClear.send_keys(Keys.DELETE)
# driver.find_element('xpath', '/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[1]/div/div[4]/div[2]/form/div/div[1]/div[1]/div[1]/div/div/input').send_keys(87232)
# print(openPrice, 'price')
# # driver.find_element('xpath', '//*[@id="server-side"]/div/div[2]/div[1]/div/div[4]/div[2]/form/div/div[2]/div[2]/div/button[1]').click()
# print('finish')
# sleep(20)
for i in range(0, position):
    while True:
          price = driver.find_element('xpath', '//*[@id="futuresOrderbook"]/div[3]/div[2]/div[1]').text
          print(i)
          if float(price) >= 7.210:
              print('Price morethan', price)
              break
          else:
              print('Price is less than', price)
              sleep(5)

    # price = driver.find_element('xpath', '//*[@id="futuresOrderbook"]/div[3]/div[2]/div[1]').text
    # data.append(price)
    # # len(data)
    # # print(data)
    # # print(len(data))
    # print(i+1, 'Price:', price)
    # if(len(data) > 1):
    #     if(data[i - 1] > data[i]):
    #         print(colored('Price is decreasing', 'red'))
    #     if(data[i - 1] == data[i]):
    #         print(colored('Price is relatively stable', 'yellow'))
    #     if(data[i - 1] < data[i]):
    #         print(colored('Price is increasing', 'green'))
    
    sleep(10)

