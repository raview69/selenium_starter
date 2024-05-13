from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from termcolor import colored
from twisted.internet import task, reactor
import threading 
import time



position = int(input('Enter how many open position: '))
type = input('Enter position type: ')
timeFrame = int(input('Enter time frame: '))
data = []
cutloss = False
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ['enable-automation'])
driver = webdriver.Chrome(service=Service(""),
options=options)
action = ActionChains(driver)
url = 'https://www.speedtest.net/'
driver.get(url)
driver.maximize_window()
driver.delete_all_cookies()
sleep(80)



for i in range(0, position):
    print('open position ke', i)
    dataopen = []
    while True:
          
          price = driver.find_element('xpath', '/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[5]/div/div[2]/div/div/div[3]/div[2]/div[1]').text
          driver.find_element('xpath', '/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[5]/div/div[2]/div/div/div[3]/div[3]/div[1]/div/div/div[1]/div/div[1]/div[1]').click()
          #error disini setelah sukses close order
          try:
              priceOpen = driver.find_element('xpath', '/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[5]/div/div[2]/div/div/div[3]/div[2]/div[1]').text
              driver.find_element('xpath', '//*[@id="server-side"]/div/div[2]/div[1]/div/div[4]/div[2]/form/div/div[1]/div[3]/div[1]/div/div/div[9]').click()
              
          except:
              print('already 100 amount')
         
          #mau short/long edit disini
          if(type == 'short'):
              driver.find_element('xpath', '/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[1]/div/div[4]/div[2]/form/div/div[2]/div[2]/div/button[2]').click()
          else:
              driver.find_element('xpath', '//*[@id="server-side"]/div/div[2]/div[1]/div/div[4]/div[2]/form/div/div[2]/div[2]/div/button[1]').click()
          
          isOpen = driver.find_element('xpath', '/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[7]/div[2]/div/div[1]/div[1]').text
          j=0
          if isOpen != "Positions(0)":
              while j < 10000:
                  price3 = driver.find_element('xpath', '/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[5]/div/div[2]/div/div/div[3]/div[2]/div[1]').text
                  data.append(price3)
                  print(data)
                  print("j", j)
                  driver.find_element('css selector', '#tab-POSITIONS').click()

                  #if cutlosss
                  if cutloss:
                        data.clear()
                        cutloss = False
                        print('cutloss called')
                        break
                  

                  if(type == 'short'):
                      if(len(data) > 1):
                        if(data[j - 1] > data[j]):
                            #error disini
                            print(colored('Price is decreasing', 'red'))
                            
                        elif(data[j - 1] == data[j]):
                          #   driver.find_element('css selector', '#tab-POSITIONS').click()
                            print(colored('Price is relatively stable', 'yellow'))
                          #   sleep(20)
                        elif(data[j - 1] < data[j]):
                          #   driver.find_element('css selector', '#tab-POSITIONS').click()
                            print(colored('Price is increasing', 'green'))
                            driver.find_element('css selector', '#position-pc > div > div.list-container.css-eaerhv > div.list-auto-sizer > div > div > div > div > div.closePosition > div > button.css-17ech4f').click()
                            data.clear()
                            break
                          #   sleep(20)
                  
                  
                  else:
                      if len(data) > 0:
                        if len(data) == 1:
                            m = 0
                            for m in range(0, timeFrame):
                                print('open position ke', i)
                                print('m', m)
                                print('j', j)
                                try:
                                    precent = driver.find_element('xpath', '/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[7]/div[2]/div/div[2]/div/div/div/div/div/div[3]/div[1]/div/div/div/div/div[9]/span/div[2]').text
                                    print(precent)
                                    #bug disini
                                    if(float(precent[1:-2]) < -2.5):
                                        print('closed')
                                        driver.find_element('css selector', '#position-pc > div > div.list-container.css-eaerhv > div.list-auto-sizer > div > div > div > div > div.closePosition > div > button.css-17ech4f').click()
                                        data.append("cutloss")
                                        cutloss = True
                                        break
                                    else:
                                        print('not closed')
                                        sleep(3)
                                except:
                                    print('not called')
                                    sleep(1)
                        elif data[j - 1] == data[j]:
                          #   driver.find_element('css selector', '#tab-POSITIONS').click()
                            print(colored('Price is relatively stable', 'yellow'))
                            l = 0
                            for l in range(0, timeFrame):
                                print('open position ke', i)
                                print('l', l)
                                print('j', j)
                                try:
                                    precent = driver.find_element('xpath', '/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[7]/div[2]/div/div[2]/div/div/div/div/div/div[3]/div[1]/div/div/div/div/div[9]/span/div[2]').text
                                    print(precent)
                                    #bug disini
                                    if(float(precent[1:-2]) < -2.5):
                                        print('closed')
                                        driver.find_element('css selector', '#position-pc > div > div.list-container.css-eaerhv > div.list-auto-sizer > div > div > div > div > div.closePosition > div > button.css-17ech4f').click()
                                        data.append("cutloss")
                                        cutloss = True
                                        break
                                    else:
                                        print('not closed')
                                        sleep(3)
                                except:
                                    print('not called')
                                    sleep(3)
                        elif data[j - 1] < data[j]:
                          #   driver.find_element('css selector', '#tab-POSITIONS').click()
                            print(colored('Price is increasing', 'green'))
                            k = 0
                            for k in range(0, timeFrame):
                                print('open position ke', i)
                                print('k', k)
                                print('j', j)
                                try:
                                    precent = driver.find_element('xpath', '/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[7]/div[2]/div/div[2]/div/div/div/div/div/div[3]/div[1]/div/div/div/div/div[9]/span/div[2]').text
                                    print(precent)
                                    #bug disini
                                    if(float(precent[1:-2]) < -2.5):
                                        print('closed')
                                        driver.find_element('css selector', '#position-pc > div > div.list-container.css-eaerhv > div.list-auto-sizer > div > div > div > div > div.closePosition > div > button.css-17ech4f').click()
                                        data.append("cutloss")
                                        cutloss = True
                                        break
                                    else:
                                        print('not closed')
                                        sleep(3)
                                except:
                                    print('not called')
                                    sleep(1)
                        elif data[j - 1] > data[j]:
                            #error disini
                            print(colored('Price is decreasing', 'red'))
                            try:
                                driver.find_element('css selector', '#position-pc > div > div.list-container.css-eaerhv > div.list-auto-sizer > div > div > div > div > div.closePosition > div > button.css-17ech4f').click()
                            except:
                                print('already closed')
                            data.clear()
                            break
                            
                  j += 1
                  sleep(3)    
              print('Price morethan', price)
              break
          else:
            try:
               driver.find_element('xpath', '/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[7]/div[2]/div/div[1]/div[2]').click()
               driver.find_element('css selector', '#OPEN_ORDERS > div > div > div > div.list-container.css-eaerhv > div.list-auto-sizer > div > div > div > div > div.action.css-10nf7hq > svg').click()
               sleep(3)
               driver.find_element('xpath', '/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[1]/div/div[4]/div[2]/form/div/div[1]/div[3]/div[1]/div/div/div[5]').click()
               print('position closed successfully')
               sleep(3)
            except:
                print('not')
                sleep(3)
                print('Price is less than', price)
          sleep(6)
    sleep(50)
