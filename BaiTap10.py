from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#tạo url
url = 'http://pythonscraping.com/pages/javascript/ajaxDemo.html'

#truy cập
driver.get(url)

# #In ra nội dung của tràn web
# print("Before: ========================================/n")
# print(driver.page_source)

#tạm dừng khoảng 3s
time.sleep(3)

# #In lại
# print("\n\n\nAfter: ========================================/n")
# print(driver.page_source)

#tìm phần tử body của trang để gửi phím mũi tên xuống
body = driver.find_element(By.TAG_NAME, "body")

#nhấn mũi tên xuống nhiều lần để cuộn xuống từ từ
for i in range(30):
    body.send_keys()
# Đóng browser
driver.quit()