from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\chromedriver.exe')

driver.get('http://eduko.spikotech.com/Course')


context=driver.page_source
soup=BeautifulSoup(context,'html.parser')
print(soup)
for i in soup.find_all("div",id_={"id":"courseData"}):
    print(i)
df=pd.DataFrame({"CourseCode""Title""Description""CLO1""CLO2""ClO3""CLO4""TextBook1""TextBook2""Instructor""Semester"})
df.to_csv('Data.csv', index=False, encoding='utf-8')
driver.quit()