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
sleep(40)
# openPrice = driver.find_element('xpath', '//*[@id="futuresOrderbook"]/div[3]/div[2]/div[1]').text


# action.double_click(driver.find_element('xpath', '/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[1]/div/div[4]/div[2]/form/div/div[1]/div[1]/div[1]/div/div/input')).perform()
# # driver.find_element('xpath', '/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[1]/div/div[4]/div[2]/form/div/div[1]/div[1]/div[1]/div/div/input').click()
# # toClear.send_keys(Keys.CONTROL + "a")
# # toClear.send_keys(Keys.DELETE)
# driver.find_element('xpath', '/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[1]/div/div[4]/div[2]/form/div/div[1]/div[1]/div[1]/div/div/input').send_keys(87232)
# print(openPrice, 'price')

# print('finish')
# sleep(20)




# for i in range(0, 2):
#   try:
#     driver.find_element('xpath', '/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[7]/div[2]/div/div[1]/div[1]/div').click()
#     driver.find_element('xpath', '/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[7]/div[2]/div/div[2]/div/div/div/div/div/div[3]/div[1]/div/div/div/div/div[10]/div/button[1]').click()
#     sleep(5)
#     print('position closed successfully')
#   except:
#     print('not called')




for i in range(0, position):
    while True:
          price = driver.find_element('xpath', '//*[@id="futuresOrderbook"]/div[3]/div[2]/div[1]').text
          driver.find_element('xpath', '//*[@id="futuresOrderbook"]/div[3]/div[3]/div[1]/div/div/div[1]/div/div[1]/div[1]').click()
          #error disini setelah sukses close order
          driver.find_element('xpath', '//*[@id="server-side"]/div/div[2]/div[1]/div/div[4]/div[2]/form/div/div[1]/div[3]/div[1]/div/div/div[9]').click()
          driver.find_element('xpath', '//*[@id="server-side"]/div/div[2]/div[1]/div/div[4]/div[2]/form/div/div[2]/div[2]/div/button[1]').click()
          isOpen = driver.find_element('xpath', '/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[7]/div[2]/div/div[1]/div[1]').text
          j=0
          if isOpen != "Positions(0)":
              while j < 10000:
                  price2 = driver.find_element('xpath', '//*[@id="futuresOrderbook"]/div[3]/div[2]/div[1]').text
                  data.append(price2)
                  print(data)
                  print("j", j)
                  if(len(data) > 1):
                      if(data[j - 1] > data[j]):
                          print(colored('Price is decreasing', 'red'))
                          ## bugg for lose order
                          driver.find_element('css selector', '#tab-POSITIONS').click()
                          sleep(1)
                          driver.find_element('css selector', '#position-pc > div > div.list-container.css-eaerhv > div.list-auto-sizer > div > div > div > div > div.closePosition > div > button.css-17ech4f').click()
                          sleep(20)
                          data.clear()
                          break
                      if(data[j - 1] == data[j]):
                          print(colored('Price is relatively stable', 'yellow'))
                      if(data[j - 1] < data[j]):
                          print(colored('Price is increasing', 'green'))
                          sleep(20)
                  j += 1
                  sleep(20)
              print('Price morethan', price)
              break
          else:
            try:
               driver.find_element('xpath', '/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[7]/div[2]/div/div[1]/div[2]').click()
               driver.find_element('css selector', '#OPEN_ORDERS > div > div > div > div.list-container.css-eaerhv > div.list-auto-sizer > div > div > div > div > div.action.css-10nf7hq > svg').click()
               sleep(5)
               driver.find_element('xpath', '/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[1]/div/div[4]/div[2]/form/div/div[1]/div[3]/div[1]/div/div/div[5]').click()
               print('position closed successfully')
               sleep(5)
            except:
                print('not called')
                sleep(5)
                print('Price is less than', price)
    sleep(10)

