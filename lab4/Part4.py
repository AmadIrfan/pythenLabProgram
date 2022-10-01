from bs4 import BeautifulSoup
from selenium import webdriver 
import pandas as pd
import requests

path="C:\Program Files (x86)\chromedriver.exe"

driver=webdriver.Chrome(path)

edu=driver.get("http://eduko.spikotech.com/Course")
print(driver.title)
driver.quit()
