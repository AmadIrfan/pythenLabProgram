from importlib.resources import path
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
path="C:\Program Files (x86)\chromedriver.exe"

driver=webdriver.Chrome(path)

#driver.get('http://eduko.spikotech.com/Course')
driver.get("https://www.youtube.com/")
content=driver.page_source
soup=BeautifulSoup()
print(driver.title)
driver.quit()