from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import re
import sqlite3

#tao db

conn = sqlite3.connect("Product.db")
c = conn.cursor()
try:
    c.execute('''
        CREATE TABLE Product (
            name primary key,
            Gia_Goc text,
            Gia_Giam text
        )
    ''')
except Exception as e:
    print(e)

#Truy cap chrome
driver = webdriver.Chrome()
url = 'https://gochek.vn/collections/all'

def add_data(a,b,c):
    # Kết nối và lấy dữ liệu
    conn = sqlite3.connect('Product.db')
    c = conn.cursor()
    #thực hiện câu lệnh thêm
    c.execute('''
        INSERT INTO 
        Product (name, Gia_Goc, Gia_Giam)
        VALUES 
        (:name, :Gia_Goc, :Gia_Giam)
    ''',{
        'name' : a,
        'Gia_Goc' : b,
        'Gia_Giam': c,
      }
    )
    conn.commit()
    conn.close()

#mở tràn web
driver.get(url)
time.sleep(3)
#truy cap tung san pham va lay thong tin

products = driver.find_elements(By.CLASS_NAME, "col-md-3.col-sm-4.col-xs-6.pro-loop.col_fix20")
print(len(products))

for product in products: 
    #tim ten
    try: 
        name_element = product.find_element(By.TAG_NAME, "h3").text
    except:
        print("error")

    #tim gia goc va gia giam
    try:
        org_price = product.find_element(By.TAG_NAME, 'p').text
        org_pr,dis_price = org_price.split()
        add_data(name_element, org_pr, dis_price)
        print(org_pr, "|", dis_price)
        print("org_prc", type(org_pr))

    except:
        org_pr = org_price.split()
        true_org_prc = org_pr[0]
        dis_price = "NULL"
        #them vao database
        add_data(name_element, true_org_prc, dis_price)


driver.quit()