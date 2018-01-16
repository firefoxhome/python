#coding=utf-8  
''''' 
Created on 2018-1-10
 
Author: firefoxhome

Theme: Web Crawler

Need : python2.7
sudo pip install beautifulsoup4
'''  
import urllib2   
import re   
from bs4 import BeautifulSoup  
from distutils.filelist import findall 
import time 

while True:
	page = urllib2.urlopen('https://www.kano.is/address.php?a=1HCmGvkbq7ULG5qeKy1wYVZbvKjPf3z26A')   
	contents = page.read()   
	#获得了整个网页的内容也就是源代码  
	#print(contents)
	soup = BeautifulSoup(contents,"html.parser")
	#soup.find_all('div', class_='info')
	m_name = soup.find('body').get_text()   
	print(m_name)

	wline = "Cats are smarter than dogs"
	#print(wline)

	s= '{name}Cats are smarter than dogs'
	b = s.format(name=m_name)
	#print b

	#result = re.search( r'(.*) are (.*?) .*', b, re.M|re.I)
	#result = re.search( r'hashrate5m', b, re.M|re.I)
	result = re.search( r'("hashrate5m": ")(.*?)(T",)', b, re.M|re.I)
	wang = result.group()
	jiang = result.group(2)
	print jiang
	print wang  

	file = open('data.txt','a') 
	line = jiang
	file = file.write(line + '\n')
	time.sleep( 5 )
	#file.close()