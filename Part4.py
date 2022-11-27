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
df=pd.DataFrame({"CourseCode","Title","Description","CLO1","CLO2","ClO3","CLO4","TextBook1","TextBook2","Instructor","Semester"})
df.to_csv('Data.csv', index=False, encoding='utf-8')
driver.quit()

driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\chromedriver.exe')
products=[] #List to store name of the product
prices=[] #List to store price of the product 
ratings=[] #List to store rating of the product 
driver.get("https://www.flipkart.com/gaming-laptops-store?otracker=nmenu_sub_Electronics_0_Gaming%20Laptops&otracker=nmenu_sub_Electr onics_0_Gaming%20Laptops")
content = driver.page_source
soup = BeautifulSoup(content)

for a in soup.findAll('div',class_={'class':'_37K3-p'}):
    print (a)
    name=a.find('a', attrs={'class':'s1Q9rs'})
    price=a.find('div',attrs={'class':'_30jeq3'})
    rating=a.find('div',attrs={'class':'_3LWZlK'})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text)

df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings})
df.to_csv('products.csv', index=False, encoding='utf-8')
driver.quit()


