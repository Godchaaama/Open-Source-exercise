from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import re

i = 1
#Truy cap chrome
driver = webdriver.Chrome()
url = 'https://gochek.vn/collections/all'


#mở tràn web
driver.get(url)
time.sleep(3)
#truy cap tung san pham va lay thong tin

products = driver.find_elements(By.CLASS_NAME, "col-md-3.col-sm-4.col-xs-6.pro-loop.col_fix20")
print(len(products))


for product in products: 
    stt = i 
    #tim ten
    try: 
        name_element = product.find_element(By.TAG_NAME, "h3").text
    except:
        print("error")

    #tim gia goc va gia giam
        org_price = product.find_element(By.TAG_NAME, 'p').text
        org_pr,dis_price = org_price.split()
    

df = pd.DataFrame({
    "STT": stt,
    "ten": name_element,
    "gia goc": org_pr,
    "Gia giam": dis_price
})

df.to_excel("danh_sach_sp.xlsx", index= False)

driver.quit()