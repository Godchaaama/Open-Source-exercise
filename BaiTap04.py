from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#khoi tao webdriver
driver = webdriver.Chrome()

for i in range(65, 91):
    url = "https://en.wikipedia.org/wiki/List_of_painters_by_name_beginning_with_%22"+chr(i)+"%22"
    #mo trang web
    driver.get(url)
    try:
        #doi khoang chung 2s
        time.sleep(5)

        #lay ra tat ca the ul
        ul_tags = driver.find_elements(By.TAG_NAME, "ul")

        #chon ul thu 21
        ul_painters = ul_tags[20]

        #lay tat ca the <li> thuoc ul_painters
        li_tags = ul_painters.find_elements(By.TAG_NAME, "li")
        # #tao danh sach cac url
        # links = [tag.find_element(By.TAG_NAME,"a").get_attribute("href") for tag in li_tags]

        #tao danh sach cac title
        titles = [tag.find_element(By.TAG_NAME,"a").get_attribute("title") for tag in li_tags]
        #in ra danh sach
        for title in titles:
            print(title)
   
    except:
        print("Error!!")


#tat man hinh
driver.quit()