import undetected_chromedriver as uc
import time

if __name__ == '__main__':
    options = uc.ChromeOptions()
    #options.headless=True
    #options.add_argument('--headless')
    chrome = uc.Chrome(options=options)
    chrome.get('https://embed.warezcdn.net/filme/tt19704638')
    time.sleep(10)
    chrome.find_element_by_xpath('/html/body/div[1]/div[3]/div[3]/div[1]/div[1]').click()
    chrome.find_element_by_xpath('[@id="preClick"]/div[2]').click()
    time.sleep(10)




    time.sleep(100000)