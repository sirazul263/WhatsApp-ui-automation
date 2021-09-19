from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from config import CHROME_DATA_PATH
from time import sleep
import os
from selenium.webdriver.common.keys import Keys
import pandas as pd

# os.system("taskkill /im chrome.exe /f")
option = webdriver.ChromeOptions()
option.add_argument(CHROME_DATA_PATH)

driver = webdriver.Chrome(executable_path='chromedriver.exe',options=option)
driver.get("https://web.whatsapp.com/")
sleep(20)

def send_message(number, msg):
    search_box = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    search_box.send_keys(number)
    sleep(2)

    try:
        driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[11]').click()
    except:
        try:
            driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[8]').click()
        except:
            print("Xpath error")
              
    sleep(2)

    msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]')
    msg_box.send_keys(msg)
    msg_box.send_keys(Keys.ENTER)
    return "sent"


df = pd.read_excel('number.xlsx',header=None,names=["number","status"])
number = "+"+str(df["number"][0])

df["status"][0] = send_message(number,"Hello dear...")
print(df)
writer = pd.ExcelWriter('number.xlsx')

df.to_excel(writer, index=False, header=False)
writer.save()