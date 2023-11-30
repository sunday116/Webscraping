from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from time import sleep
import requests
from bs4 import BeautifulSoup
import xlwt
from xlwt import Workbook
import math

sql = "INSERT INTO user_links (username, added) VALUES (%s, %s)"
search_names = ['TOM', 'CALVIN', 'ALEX', 'JON', 'RONNIE', 'BILL', 'LLOYD',
                'TOMMY', 'LEON', 'DEREK', 'WARREN', 'DARRELL', 'JEROME', 'FLOYD', 'LEO', 'ALVIN', 'TIM', 'WESLEY', 'GORDON', 'DEAN', 'GREG', 'JORGE', 'DUSTIN',
                'PEDRO', 'DERRICK', 'DAN', 'LEWIS', 'ZACHARY', 'COREY', 'HERMAN', 'MAURICE', 'VERNON', 'ROBERTO', 'CLYDE', 'GLEN', 'HECTOR', 'SHANE'
                'RICARDO', 'SAM', 'RICK', 'LESTER', 'BRENT', 'RAMON', 'CHARLIE', 'TYLER', 'GILBERT', 'GENE', 'MARC', 'REGINALD', 'RUBEN', 'BRETT', 'ANGEL',
                'NATHANIEL', 'RAFAEL', 'LESLIE', 'EDGAR', 'MILTON', 'RAUL', 'BEN', 'CHESTER', 'CECIL', 'DUANE', 'FRANKLIN', 'ANDRE', 'ELMER', 'BRAD', 'GABRIEL',
                'RON', 'MITCHELL', 'ROLAND', 'ARNOLD', 'HARVEY', 'JARED', 'ADRIAN', 'KARL', 'CORY', 'CLAUDE', 'ERIK', 'DARRYL', 'JAMIE', 'NEIL', 'JESSIE', 'CHRISTIAN',
                'JAVIER', 'FERNANDO', 'CLINTON', 'TED', 'MATHEW', 'TYRONE', 'DARREN', 'LONNIE', 'LANCE', 'CODY', 'JULIO', 'KELLY', 'KURT', 'ALLAN', 'NELSON', 'GUY',
                'CLAYTON', 'HUGH', 'MAX', 'DWAYNE', 'DWIGHT', 'ARMANDO', 'FELIX', 'JIMMIE', 'EVERETT', 'JORDAN', 'IAN', 'WALLACE', 'KEN', 'BOB', 'JAIME', 'CASEY', 'ALFREDO',
                'ALBERTO', 'DAVE', 'IVAN', 'JOHNNIE', 'SIDNEY', 'BYRON', 'JULIAN', 'ISAAC', 'MORRIS', 'CLIFTON', 'WILLARD', 'DARYL', 'ROSS', 'VIRGIL', 'ANDY', 'MARSHALL',
                'PERRY', 'KIRK', 'SERGIO', 'MARION', 'TRACY', 'SETH', 'KENT', 'TERRANCE', 'RENE', 'EDUARDO', 'TERRENCE', 'ENRIQUE', 'FREDDIE', 'WADE']

url_original = 'https://github.com/search?l=JavaScript&ref=advsearch&type=Users&utf8=%E2%9C%93&p='
driver = webdriver.Chrome()
driver.set_window_size(1920, 1080)

index = 0
val = []

start_page = 56
end_page = 100

try:
    for search_name in search_names:
        driver.get(url_original + str(1) + '&q=fullname%3A' + search_name)
        sleep(50)
        # total_users_text = driver.find_element_by_xpath('//*[@id="js-pjax-container"]/div/div[3]/div/div[1]/h3').text
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
            # for temp in temps:
            #     user_link = temp.find_element_by_css_selector('a.mr-1').get_attribute('href')
            #     print(user_link)
            #     val.append((user_link.replace('https://github.com/', '').replace('/', ''), '1'))

            # val = []

        # start_page = 1
except:
    driver.close()

driver.close()