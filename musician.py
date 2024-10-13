from pygments.formatters.html import webify
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
import re
import sqlite3
#tạo dataframe rỗng và dictionnary
all_links = []
musician_links = []

conn = sqlite3.connect("Musician_db.db")
c = conn.cursor()
try:
    c.execute('''
        CREATE TABLE Musician (
            name_of_the_band primary key,
            years_active integer
        )
    ''')
except Exception as e:
    print(e)

# Tạo op để chạy chế độ ẩn 
chrome_options = Options()
chrome_options.add_argument("--headless=new")  
chrome_options.add_argument("--disable-gpu")  
chrome_options.add_argument("--no-sandbox")  
chrome_options.add_argument("--disable-dev-shm-usage") 
chrome_options.add_argument("--log-level=3")  
chrome_options.add_argument("--window-size=1920x1080")

#truy cập vô trang web 
driver = webdriver.Chrome(chrome_options)
url = 'https://en.wikipedia.org/wiki/Lists_of_musicians#A'

#mở tràn web
driver.get(url)

#dừng khoảng 2s
time.sleep(2)
def insert_data(name, year):
    ck = sqlite3.connect('Musician_db.db')
    c = ck.cursor()
    c.execute('''
        INSERT INTO Musician(name_of_the_band, years_active)
        VALUES (:name_of_the_band, :years_active)
    ''',
      {
          'name_of_the_band': name,
          'years_active': year,
          
      })
    ck.commit()
    ck.close()
try:
    #lấy tất cả các thẻ ul trong web danh mục
    ul_tags = driver.find_elements(By.TAG_NAME, "ul")
    print(len(ul_tags))

    #chọn ul thứ 22
    ul_musican = ul_tags[21]
    #lấy tất cả link chứa thông tin nhạc sĩ bắt đầu bằng chữ A thuộc ul_musican
    li_tags = ul_musican.find_elements(By.TAG_NAME, "li")
    print(len(li_tags))

    # tạo danh sách các url
    links = [tag.find_element(By.TAG_NAME,"a").get_attribute("href") for tag in li_tags]
    for x in links:
        all_links.append(x)
except:
    print("Error!!!!")
#tat man hinh
driver.quit()

#truy cập vô đường link đầu tiên của all_links
artists_driver = webdriver.Chrome(chrome_options)
artists_driver.get(all_links[0])

#dừng khoảng 2s
time.sleep(2)

try:
     #lấy tất cả các the ul của list of acid rock artists
    ul_artists_tags = artists_driver.find_elements(By.TAG_NAME, "ul")
    print(len(ul_artists_tags))

    #chọn ul thứ 25
    ul_artist = ul_artists_tags[24]
    #lấy tất cả link chứa thông tin thuộc artists
    li_artist = ul_artist.find_elements(By.TAG_NAME, "li")
    print(len(li_artist))

    # tạo danh sách các url của artist
    links_artist = [artist_tag.find_element(By.TAG_NAME,"a").get_attribute("href") for artist_tag in li_artist]
    for x in links_artist:
        musician_links.append(x)
except:
    print("Error!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
artists_driver.quit()

#lấy thông tin của các nhạc sĩ ca sĩ
count = 0
for link in musician_links:
    # if(count >= 2):
    #     break
    # count += 1
    print(link)
    try:
        #khởi tạo webdriver
        driver = webdriver.Chrome(options=chrome_options)
        #mở trang web
        url = link
        driver.get(url)
        #đợi khoảng 2s
        time.sleep(2)
        #lấy tên ban nhạc
        try:
            name_band = driver.find_element(By.TAG_NAME, "h1").text
        except:
            name_band = ""

        #lay năm hoat dong
        try:
            year_active_element = driver.find_element(By.XPATH, value='//span[contains(text(),"Years active")]/parent::*/following-sibling::td')
            year_active = year_active_element.text
            
        except:
            year = ""

        insert_data(name_band,year_active_element)
    except:
        print("Error!!!!!!!!!!!!!!!")
        
