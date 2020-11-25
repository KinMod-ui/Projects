from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get('https://www.youtube.com/channel/UCtHaxi4GTYDpJgMSGy7AeSw/videos')
# Michael Reeves
time.sleep(3)


page = driver.find_element_by_xpath("//*[@class='yt-simple-endpoint style-scope ytd-grid-video-renderer']")


title = 'I Hate Your Robot Ideas'
video_title =  page.get_attribute('title')
if (video_title == title):
	driver.quit()
else:
	title = video_title
	page.click()
	time.sleep(3)
	try :
		
		skip_ad = driver.find_element_by_xpath("//*[@class='ytp-ad-text ytp-ad-skip-button-text']")
		time.sleep(6)
		if (skip_ad):
			skip_ad.click()
	except:
		pass


actions = ActionChains(driver)
actions.send_keys('t')
actions.perform()

driver.maximize_window()
time .sleep(20)
try:
	button = driver.find_elements_by_tag_name('button')	
	for i in button:
		if i.get_attribute('class') == 'ytp-ad-overlay-close-button':
			i.click()
			break
except:
	pass


	





  


