from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from sys import displayhook
import pandas as pd
import time
import os
start_time = time.time()

##### CONFIG #####
user_login = 'bot4'
user_pass = 'LUCXssW9rVk$15ElaM'
table_name ='table40.xlsx'


options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080");
options.add_argument("--no-sandbox");
options.add_argument("--headless");
options.add_argument("--disable-gpu");
options.add_argument("--disable-crash-reporter");
options.add_argument("--disable-extensions");
options.add_argument("--disable-in-process-stack-traces");
options.add_argument("--disable-logging");
options.add_argument("--disable-dev-shm-usage");
options.add_argument("--log-level=3");
options.add_argument("--output=/dev/null");
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

table = pd.read_excel(table_name)
while True:
    try:
        driver.get('http://localhost/wordpress/wp-login.php?')
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="user_login"]'))).send_keys(user_login)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="user_pass"]'))).send_keys(user_pass)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wp-submit"]'))).click()
        #displayhook(table)
        for imdb in table ['imdb']:
            print(user_login+' : '+imdb+'  Writing post..')
            table = pd.read_excel(table_name)
            #displayhook(table)

            driver.get('http://localhost/wordpress/wp-admin/edit.php?post_type=movies')
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="dbmovies-inp-tmdb"]'))).send_keys(imdb)
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="dbmovies-btn-importer"]'))).click()
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="repeatable-fieldset-one"]/tbody/tr[1]/td[3]/select'))).click()
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="repeatable-fieldset-one"]/tbody/tr[1]/td[3]/select/option[7]'))).click()
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="repeatable-fieldset-one"]/tbody/tr[1]/td[2]/select'))).click()
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="repeatable-fieldset-one"]/tbody/tr[1]/td[2]/select/option[2]'))).click()
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#repeatable-fieldset-one > tbody > tr:nth-child(1) > td:nth-child(4) > input'))).send_keys('https://embed.warezcdn.net/filme/'+imdb)
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/form/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div[2]/input[2]'))).click()
            driver.get('http://localhost/wordpress/wp-admin/edit.php?post_type=movies')
            print(user_login+' : '+imdb+'  Success')

            table = table.drop(0)
            displayhook(table)
            table.to_excel(table_name, index=False)
        print ("time elapsed: {:.2f}s".format(time.time() - start_time))
        driver.quit()
        break
    except Exception as err:
        print(f"Error: {str(err)}, trying again")
        pass