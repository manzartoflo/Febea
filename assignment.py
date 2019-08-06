#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 20:57:05 2019

@author: manzar
"""

from bs4 import BeautifulSoup
from selenium import webdriver

urls = "https://www.febea.fr/en/contactez-nos-entreprises?page="

wb = webdriver.Chrome()

file = open('assignment.csv', 'w')
header = 'Company Name, Email, Telephone, Website\n'
file.write(header)

for i in range(15):
    url = urls + str(i)
    wb.get(url)
    html = wb.execute_script('return document.documentElement.outerHTML')
    soup = BeautifulSoup(html, 'lxml')
    divs = soup.findAll('div', {'class': 'views-row'})
    for div in divs:
        name = div.findAll('div', {'class': 'views-field-title'})[0].span.text
        
        try:
            tel = div.findAll('div', {'class': 'views-field-field-numero-de-telephone'})[0].div.text
        except:
            tel = 'NaN'
            
        try:
            email = div.findAll('div', {'class': 'views-field-field-email-service'})[0].a.attrs['href'].split('mailto:')[1]
        except:
            email = 'NaN'
          
        try:
            web = div.findAll('div', {'class': 'views-field-field-website'})[0].a.attrs['href']
        except:
            web = 'NaN'
            
        print(name, tel, email, web)
        file.write(name.replace(',', '') + ', ' + email + ', ' + tel.replace(',', '') + ', ' + web + '\n')
file.close()
wb.close()