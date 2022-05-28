from selenium import webdriver
from selenium.webdriver.common.by import By
import time

navegador = webdriver.Chrome()
navegador.get('https://embed.warezcdn.net/filme/tt19704638')

navegador.find_element_by_xpath('/html/body/div[1]/div[3]/div[3]/div[1]/div[1]').click()
time.sleep(1)
navegador.find_element_by_xpath('/html/body/div[2]/div[2]').click()

#navegador.find_element_by_xpath('//*[@id="i0116"]').send_keys('teste@gmail.com')
#time.sleep(1)
#navegador.find_element(By.XPATH,'//*[@id="i0116"]').send_keys('teste@gmail.com')
#time.sleep(1)
#navegador.find_element(By.XPATH,'//*[@id="idSIButton9"]').click()
#time.sleep(1)
#navegador.find_element(By.XPATH,'/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div/div[2]/input').send_keys('teste@gmail.com')
#navegador.find_element(By.XPATH,'//*[@id="idSIButton9"]').click()