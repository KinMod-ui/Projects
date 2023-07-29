from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


from apiclient.discovery import build

youtube = build('youtube' , 'v3' , developerKey=api_key)

req = youtube.search().list(q = 'david dobrik' , part='snippet' , type='video' , order='viewCount')

res = req.execute()

print(res['items'][0])

