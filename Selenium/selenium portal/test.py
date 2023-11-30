from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from time import sleep
import requests
from bs4 import BeautifulSoup
import xlwt
from xlwt import Workbook
import math

search_name = '4560AF7B7C37C8113CB25EB3FC2E5CF15D960ADF7568CF717EEFBA16ACAC6A7E'

url_original = 'https://portal-nc.tylertech.cloud/app/RegisterOfActions/#/'
driver = webdriver.Chrome()
driver.set_window_size(1920, 1080)

driver.get(url_original + search_name)

content = driver.page_source
sleep(1)
# print(driver.get)
# driver.close()
# https://www.xing.com/

# https://crowdworks.jp/

# https://www.peopleperhour.com/
driver.get(url_original + 'asdf')
sleep(1000)
# driver.page_source = ''
# driver.page_source = content
# sleep(50)
# sleep(50)
# url = driver.current_url
# new_url = url.replace(search_name, 'aaa')
# print(new_url)
# driver.execute_script(f"window.location.href='{new_url}'")
# total_users_text = driver.find_element_by_xpath('//').text
# total_users_text = total_users_text.strip().replace(' users', '').strip()
# total_users = int(float(total_users_text.replace(',', '')))
# if total_users < 1000:
#     end_page = math.ceil(total_users / 10)

# for i in range(start_page, end_page):
#     driver.get(url_original + str(i) + '&q=fullname%3A' + search_name)
#     sleep(5)

#     print('------- ' + search_name + '-- ' + str(i) + '/' + str(end_page) + ' -----')
#     log_file = open("logs.txt", "w")
#     log_file.write('------- ' + search_name + '-- ' + str(i) + ' -----')
#     log_file.close()

#     temps = driver.find_elements_by_class_name('user-list-item')
#     for temp in temps:
#         user_link = temp.find_element_by_css_selector('a.mr-1').get_attribute('href')
#         print(user_link)
# val.append((url_original))

#     val = []

# start_page = 1