from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from termcolor import colored



position = 5
data = []

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ['enable-automation']);
driver = webdriver.Chrome(service=Service(""),
options=options)
url = 'https://www.binance.com/en/trade/ARB_USDT?type=spot'
driver.get(url)
driver.maximize_window()
sleep(15)
# price = driver.find_element('xpath', '//*[@id="spotOrderbook"]/div[3]/div[2]/div[1]').text
# print(price)

for i in range(0, position):
    price = driver.find_element('xpath', '//*[@id="spotOrderbook"]/div[3]/div[2]/div[1]').text
    data.append(price)
    # len(data)
    # print(data)
    # print(len(data))
    print(i+1, 'Price:', price)
    if(len(data) > 1):
        if(data[i - 1] > data[i]):
            print(colored('Price is decreasing', 'red'))
        if(data[i - 1] == data[i]):
            print(colored('Price is relatively stable', 'yellow'))
        if(data[i - 1] < data[i]):
            print(colored('Price is increasing', 'green'))
    
    sleep(30)

