from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = Options() 
options.add_argument("/Users/pratham/Library/Application\ Support/Google/Chrome/Default")
driver = webdriver.Chrome(options=options)
driver.get("https://web.whatsapp.com/")
time.sleep(2)

chat = driver.find_element_by_xpath("//*[@id='pane-side']/div[1]/div/div/div[4]/div/div/div[2]/div[1]/div[1]/span/span")
chat.click()
time.sleep(1)

message_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
message_box.send_keys('Hey mommy')

send = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span')
send.click()
