from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from termcolor import colored
import time
from datetime import datetime
import chromedriver_autoinstaller
import json
import undetected_chromedriver as uc

position = int(input("Enter how many open position: "))
timeFrame = int(input("Enter time frame: "))
detectSecond = int(input("Enter detect second: "))
data = []
cutloss = False
file = open("cookies.json")
datac = json.load(file)
chromedriver_autoinstaller.install()
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
# options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
action = ActionChains(driver)
url = "https://www.binance.com/en/futures/DOGSUSDT"
driver.get(url)
driver.maximize_window()


sleep(10)
for i in datac:
    cookie_with_name_and_value = {"name": i["name"], "value": i["value"]}
    driver.add_cookie(cookie_with_name_and_value)

sleep(5)
driver.refresh()
sleep(5)
driver.execute_script("window.scrollTo(0, 150)")
print("Success Login")

now = datetime.now()
print("Current Time =", now)

# /html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[7]/div[2]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div[1]/div/div/div/div/div[10]/div/div[1]/button[1]

for i in range(0, position):
    print("open position ke", i)
    dataopen = []
    type = ""

    # error di tutorial setelah sukses posisi pertama
    try:
        driver.find_element(
            "css selector",
            "body > div.css-1u2nk9f > div.css-139si9b > div.css-4rbxuz > svg",
        ).click()
        sleep(1)
        driver.find_element(
            "css selector",
            "body > div.bn-trans.data-show.bn-tooltips-trans > div > div > div > button",
        ).click()
    except:
        print("Tutorial Already closed")

    while True:
        # detect price
        price = driver.find_element(
            "xpath",
            "/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[5]/div/div[2]/div/div/div/div[3]/div[2]/div[1]/div",
        ).text

        dataopen.append(price)

        # detect if position is open
        isOpenPosition = driver.find_element(
            "xpath",
            "/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[7]/div[2]/div/div/div[1]/div[1]/div/div/div",
        ).text

        # detect if open order position
        isOpenOrder = driver.find_element(
            "xpath",
            "/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[7]/div[2]/div/div/div[1]/div[2]/div",
        ).text

        print("trying to make position", len(dataopen))

        if len(dataopen) > 2 and isOpenPosition == "Positions(0)":
            # long
            if (
                dataopen[len(dataopen) - 4] < dataopen[len(dataopen) - 3]
                and dataopen[len(dataopen) - 3] < dataopen[len(dataopen) - 2]
                and dataopen[len(dataopen) - 2] < dataopen[len(dataopen) - 1]
                # and type == "long"
            ):

                try:
                    driver.find_element(
                        "xpath",
                        "/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div[3]/div[1]/div/div/div[9]",
                    ).click()
                    print("clicked 100%")

                except:
                    driver.find_element(
                        "xpath",
                        "/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div[3]/div[1]/div/div/div[8]",
                    ).click()
                    sleep(1)
                    driver.find_element(
                        "xpath",
                        "/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div[3]/div[1]/div/div/div[9]",
                    ).click()
                    print("clicked 0 and then 100")

                try:
                    # click to open order long
                    driver.find_element(
                        "xpath",
                        "/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[5]/div/div[2]/div/div/div/div[3]/div[1]/div[1]/div/div/div[8]/div/div[1]/div[1]",
                    ).click()

                    driver.find_element(
                        "xpath",
                        "/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[3]/div[1]/button",
                    ).click()

                    type = "long"
                    print("open order")
                except:
                    print("failed to open order")

            # short
            if (
                dataopen[len(dataopen) - 4] > dataopen[len(dataopen) - 3]
                and dataopen[len(dataopen) - 3] > dataopen[len(dataopen) - 2]
                and dataopen[len(dataopen) - 2] > dataopen[len(dataopen) - 1]
                # and type == "short"
            ):
                try:
                    driver.find_element(
                        "xpath",
                        "/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div[3]/div[1]/div/div/div[9]",
                    ).click()
                    print("clicked 100%")

                except:
                    driver.find_element(
                        "xpath",
                        "/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div[3]/div[1]/div/div/div[8]",
                    ).click()
                    sleep(1)
                    driver.find_element(
                        "xpath",
                        "/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div[3]/div[1]/div/div/div[9]",
                    ).click()
                    print("clicked 0 and then 100")

                try:
                    # click to open order short
                    driver.find_element(
                        "xpath",
                        "/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[5]/div/div[2]/div/div/div/div[3]/div[3]/div[1]/div/div/div[1]/div/div[1]/div[1]",
                    ).click()

                    driver.find_element(
                        "xpath",
                        "/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[3]/div[2]/button",
                    ).click()

                    type = "short"
                    print("open order")
                except:
                    print("failed to open order")

        if isOpenOrder != "Open Orders(0)":
            # chase order
            try:
                print("open order detected")
                driver.find_element(
                    "xpath",
                    "/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[7]/div[2]/div/div/div[1]/div[2]/div",
                ).click()
                sleep(1)
                driver.find_element(
                    "xpath",
                    "/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[7]/div[2]/div/div/div[2]/div[2]/div/div/div/div/div[2]/div[3]/div[1]/div/div/div/div/div[13]/div/div/button",
                ).click()
                # sleep(1)
                # driver.find_element(
                #     "css selector",
                #     "body > div.css-1u2pn8e > div.css-vra5kf > div.css-ikx47k > div.check-row.css-1m4hmg6 > div.css-jj3wml > svg",
                # ).click()
                # driver.find_element(
                #     "xpath",
                #     "/html/body/div[5]/div[1]/div[2]/button[2]",
                # ).click()

            except:
                print("failed to chase order")

        j = 0
        if isOpenPosition != "Positions(0)":
            while j < 10000:
                price3 = driver.find_element(
                    "xpath",
                    "/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[5]/div/div[2]/div/div/div/div[3]/div[2]/div[1]/div",
                ).text
                data.append(price3)
                print(data)
                print("j", j)
                driver.find_element("css selector", "#Positions----\!\!\!").click()

                # if cutlosss
                if cutloss:
                    data.clear()
                    dataopen.clear()
                    cutloss = False
                    print("cutloss called")
                    break

                if type == "short":
                    if len(data) > 0:
                        if len(data) == 1:
                            m = 0
                            for m in range(0, timeFrame):
                                print("open position ke", i)
                                print("m", m)
                                print("j", j)
                                try:
                                    precent = driver.find_element(
                                        "xpath",
                                        "/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[7]/div[2]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div[1]/div/div/div/div/div[9]/div/div[2]",
                                    ).text
                                    if precent.find("+") == -1:
                                        print(colored(precent, "red"))
                                    else:
                                        print(colored(precent, "green"))
                                    # bug disini
                                    if float(precent[1:-2]) < -3:
                                        print("closed")
                                        try:
                                            driver.find_element(
                                                "css selector",
                                                "#position-pc > div > div.list-container.css-eaerhv > div.list-auto-sizer > div > div > div > div > div:nth-child(10) > div > div.flex.items-center.space-x-\[8px\].shrink-0.mr-\[8px\] > button.bn-button.bn-button__text.bn-button__text__yellow.data-size-tiny.\!min-w-0.w-\[40px\].truncate.inline-block.text-left.\!typography-caption0.\!px-0.\!min-w-0",
                                            ).click()
                                            print("click closed")
                                            sleep(1)
                                        except:
                                            print("gagal click closed")
                                        data.append("cutloss")
                                        cutloss = True
                                        type = ""
                                        break
                                    else:
                                        print("not closed")
                                        sleep(detectSecond)
                                except:
                                    print("not called")
                                    sleep(1)

                        elif data[j - 1] == data[j]:
                            #   driver.find_element('css selector', '#tab-POSITIONS').click()
                            print(colored("Price is relatively stable", "yellow"))
                            l = 0
                            for l in range(0, timeFrame):
                                print("open position ke", i)
                                print("l", l)
                                print("j", j)
                                try:
                                    precent = driver.find_element(
                                        "xpath",
                                        "/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[7]/div[2]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div[1]/div/div/div/div/div[9]/div/div[2]",
                                    ).text
                                    if precent.find("+") == -1:
                                        print(colored(precent, "red"))
                                    else:
                                        print(colored(precent, "green"))
                                    # bug disini
                                    if float(precent[1:-2]) < -3:
                                        print("closed")
                                        try:
                                            driver.find_element(
                                                "css selector",
                                                "#position-pc > div > div.list-container.css-eaerhv > div.list-auto-sizer > div > div > div > div > div:nth-child(10) > div > div.flex.items-center.space-x-\[8px\].shrink-0.mr-\[8px\] > button.bn-button.bn-button__text.bn-button__text__yellow.data-size-tiny.\!min-w-0.w-\[40px\].truncate.inline-block.text-left.\!typography-caption0.\!px-0.\!min-w-0",
                                            ).click()
                                            print("click closed")
                                            sleep(1)
                                        except:
                                            print("gagal click closed")
                                        data.append("cutloss")
                                        cutloss = True
                                        type = ""
                                        break
                                    else:
                                        print("not closed")
                                        sleep(detectSecond)
                                except:
                                    print("not called")
                                    sleep(3)

                        elif data[j - 1] < data[j]:
                            ## eror di closing order
                            print(colored("Price is increasing", "red"))
                            try:
                                driver.find_element(
                                    "css selector",
                                    "#position-pc > div > div.list-container.css-eaerhv > div.list-auto-sizer > div > div > div > div > div:nth-child(10) > div > div.flex.items-center.space-x-\[8px\].shrink-0.mr-\[8px\] > button.bn-button.bn-button__text.bn-button__text__yellow.data-size-tiny.\!min-w-0.w-\[40px\].truncate.inline-block.text-left.\!typography-caption0.\!px-0.\!min-w-0",
                                ).click()
                                sleep(1)
                                type = ""
                                print("closed order click")
                            except:
                                print("already closed")
                            data.clear()
                            break

                        elif data[j - 1] > data[j]:
                            print(colored("Price is decreasing", "green"))
                            k = 0
                            for k in range(0, timeFrame):
                                print("open position ke", i)
                                print("k", k)
                                print("j", j)
                                try:
                                    precent = driver.find_element(
                                        "xpath",
                                        "/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[7]/div[2]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div[1]/div/div/div/div/div[9]/div/div[2]",
                                    ).text
                                    if precent.find("+") == -1:
                                        print(colored(precent, "red"))
                                    else:
                                        print(colored(precent, "green"))
                                    # bug disini
                                    if float(precent[1:-2]) < -3:
                                        print("closed")
                                        try:
                                            driver.find_element(
                                                "css selector",
                                                "#position-pc > div > div.list-container.css-eaerhv > div.list-auto-sizer > div > div > div > div > div:nth-child(10) > div > div.flex.items-center.space-x-\[8px\].shrink-0.mr-\[8px\] > button.bn-button.bn-button__text.bn-button__text__yellow.data-size-tiny.\!min-w-0.w-\[40px\].truncate.inline-block.text-left.\!typography-caption0.\!px-0.\!min-w-0",
                                            ).click()
                                            print("click closed")
                                            sleep(1)
                                        except:
                                            print("gagal click closed")
                                        cutloss = True
                                        type = ""
                                        break
                                    else:
                                        print("not closed")
                                        sleep(detectSecond)
                                except:
                                    print("not called")
                                    sleep(1)

                else:
                    if len(data) > 0:
                        if len(data) == 1:
                            m = 0
                            for m in range(0, timeFrame):
                                print("open position ke", i)
                                print("m", m)
                                print("j", j)
                                try:
                                    precent = driver.find_element(
                                        "xpath",
                                        "/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[7]/div[2]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div[1]/div/div/div/div/div[9]/div/div[2]",
                                    ).text
                                    if precent.find("+") == -1:
                                        print(colored(precent, "red"))
                                    else:
                                        print(colored(precent, "green"))
                                    # bug disini
                                    if float(precent[1:-2]) < -3:
                                        print("closed")
                                        try:
                                            driver.find_element(
                                                "css selector",
                                                "#position-pc > div > div.list-container.css-eaerhv > div.list-auto-sizer > div > div > div > div > div:nth-child(10) > div > div.flex.items-center.space-x-\[8px\].shrink-0.mr-\[8px\] > button.bn-button.bn-button__text.bn-button__text__yellow.data-size-tiny.\!min-w-0.w-\[40px\].truncate.inline-block.text-left.\!typography-caption0.\!px-0.\!min-w-0",
                                            ).click()
                                            print("click closed")
                                            sleep(1)
                                        except:
                                            print("gagal click closed")
                                        data.append("cutloss")
                                        cutloss = True
                                        type = ""
                                        break
                                    else:
                                        print("not closed")
                                        sleep(detectSecond)
                                except:
                                    print("not called")
                                    sleep(1)
                        elif data[j - 1] == data[j]:
                            #   driver.find_element('css selector', '#tab-POSITIONS').click()
                            print(colored("Price is relatively stable", "yellow"))
                            l = 0
                            for l in range(0, timeFrame):
                                print("open position ke", i)
                                print("l", l)
                                print("j", j)
                                try:
                                    precent = driver.find_element(
                                        "xpath",
                                        "/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[7]/div[2]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div[1]/div/div/div/div/div[9]/div/div[2]",
                                    ).text
                                    if precent.find("+") == -1:
                                        print(colored(precent, "red"))
                                    else:
                                        print(colored(precent, "green"))
                                    # bug disini
                                    if float(precent[1:-2]) < -3:
                                        print("closed")
                                        try:
                                            driver.find_element(
                                                "css selector",
                                                "#position-pc > div > div.list-container.css-eaerhv > div.list-auto-sizer > div > div > div > div > div:nth-child(10) > div > div.flex.items-center.space-x-\[8px\].shrink-0.mr-\[8px\] > button.bn-button.bn-button__text.bn-button__text__yellow.data-size-tiny.\!min-w-0.w-\[40px\].truncate.inline-block.text-left.\!typography-caption0.\!px-0.\!min-w-0",
                                            ).click()
                                            print("click closed")
                                            sleep(1)
                                        except:
                                            print("gagal click closed")
                                        data.append("cutloss")
                                        cutloss = True
                                        type = ""
                                        break
                                    else:
                                        print("not closed")
                                        sleep(detectSecond)
                                except:
                                    print("not called")
                                    sleep(3)
                        elif data[j - 1] < data[j]:
                            #   driver.find_element('css selector', '#tab-POSITIONS').click()
                            print(colored("Price is increasing", "green"))
                            k = 0
                            for k in range(0, timeFrame):
                                print("open position ke", i)
                                print("k", k)
                                print("j", j)
                                try:
                                    precent = driver.find_element(
                                        "xpath",
                                        "/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[7]/div[2]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div[1]/div/div/div/div/div[9]/div/div[2]",
                                    ).text
                                    if precent.find("+") == -1:
                                        print(colored(precent, "red"))
                                    else:
                                        print(colored(precent, "green"))
                                    # bug disini
                                    if float(precent[1:-2]) < -3:
                                        print("closed")
                                        try:
                                            driver.find_element(
                                                "css selector",
                                                "#position-pc > div > div.list-container.css-eaerhv > div.list-auto-sizer > div > div > div > div > div:nth-child(10) > div > div.flex.items-center.space-x-\[8px\].shrink-0.mr-\[8px\] > button.bn-button.bn-button__text.bn-button__text__yellow.data-size-tiny.\!min-w-0.w-\[40px\].truncate.inline-block.text-left.\!typography-caption0.\!px-0.\!min-w-0",
                                            ).click()
                                            print("click closed")
                                            sleep(1)
                                        except:
                                            print("gagal click closed")
                                        cutloss = True
                                        type = ""
                                        break
                                    else:
                                        print("not closed")
                                        sleep(detectSecond)
                                except:
                                    print("not called")
                                    sleep(1)

                        elif data[j - 1] > data[j]:
                            # error disini cek lagi cok
                            print(colored("Price is decreasing", "red"))
                            try:
                                driver.find_element(
                                    "css selector",
                                    "#position-pc > div > div.list-container.css-eaerhv > div.list-auto-sizer > div > div > div > div > div:nth-child(10) > div > div.flex.items-center.space-x-\[8px\].shrink-0.mr-\[8px\] > button.bn-button.bn-button__text.bn-button__text__yellow.data-size-tiny.\!min-w-0.w-\[40px\].truncate.inline-block.text-left.\!typography-caption0.\!px-0.\!min-w-0",
                                ).click()
                                sleep(1)
                                type = ""
                                print("closed order click")
                            except:
                                print("already closed")
                            data.clear()
                            break
                j += 1
                sleep(3)
            print("Price morethan", price)
            break
        else:
            print("Price is", price)
        sleep(3)
    sleep(60)
