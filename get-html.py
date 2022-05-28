import re
import requests
import pandas as pd
from signal import SIGTERM
from traceback import print_list
from turtle import st
from xml.etree.ElementTree import tostring

from bs4 import BeautifulSoup

lista_links = []
response = requests.get('https://warezcdn.com/listing.php?type=movies')
content = response.content
soup = BeautifulSoup(content, 'html.parser')

table = soup.findAll('table', attrs={'id': 'example'})

html_string = []

for x in table:
       html_string.append(str(x))

with open('table.html', 'a',encoding='utf-8') as file:
    try:
        html_string = re.sub('(?s)<div.*?<\/div>', '', str(html_string))
        html_final = (("%s\n" % str(html_string).strip('\n').replace('\\n','')[2:-2]).replace('<a class="btn" href="','')).replace('" target="_BLANK">Abrir</a>','')
        file.write(html_final)
    except Exception as err:
        file.write('an ERROR occured: ' + str(err) + '\n')