from socket import IP_ADD_MEMBERSHIP
from sys import displayhook
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument("--headless")

navegador = driver = webdriver.Chrome(chrome_options=options)
navegador.get('http://localhost/wordpress/wp-login.php?')
navegador.find_element_by_xpath('//*[@id="user_login"]').send_keys('jrschmidtt')
navegador.find_element_by_xpath('//*[@id="user_pass"]').send_keys('LUCXssW9rVk$15ElaM')
navegador.find_element_by_xpath('//*[@id="wp-submit"]').click()
time.sleep(1)

tabela = pd.read_excel('table.xlsx')
displayhook(tabela)

for imdb in tabela ['imdb']:
    inserindo = 'ISERINDO DADOS DO FILME : '+imdb+'  !!'
    f = open("bot_1.txt", "a")
    f.write("\n"+inserindo)
    f.close()
    print(inserindo)

    navegador.get('http://localhost/wordpress/wp-admin/edit.php?post_type=movies')
    time.sleep(1)
    navegador.find_element_by_xpath('//*[@id="dbmovies-inp-tmdb"]').send_keys(imdb)
    time.sleep(2)
    navegador.find_element_by_xpath('//*[@id="dbmovies-btn-importer"]').click()
    time.sleep(5)
    navegador.find_element_by_xpath('//*[@id="repeatable-fieldset-one"]/tbody/tr[1]/td[3]/select').click()
    navegador.find_element_by_xpath('//*[@id="repeatable-fieldset-one"]/tbody/tr[1]/td[3]/select/option[7]').click()
    navegador.find_element_by_xpath('//*[@id="repeatable-fieldset-one"]/tbody/tr[1]/td[2]/select').click()
    navegador.find_element_by_xpath('//*[@id="repeatable-fieldset-one"]/tbody/tr[1]/td[2]/select/option[2]').click()
    navegador.find_element_by_css_selector('#repeatable-fieldset-one > tbody > tr:nth-child(1) > td:nth-child(4) > input').send_keys('https://embed.warezcdn.net/filme/'+imdb)
    time.sleep(5)
    navegador.find_element_by_xpath('//*[@id="publish"]').click()
    time.sleep(2)
    navegador.get('http://localhost/wordpress/wp-admin/edit.php?post_type=movies')

    logtxt = 'FILME: '+imdb+' SUCESSO !!'
    f = open("bot_1.txt", "a")
    f.write("\n"+logtxt)
    f.close()
    print(logtxt)

