import urllib2
from selenium import webdriver
import dryscrape
from bs4 import BeautifulSoup

# This is for test python function

# my_url = 'https://www.doordash.com/cart/j16vxhGiOy1oyrw/'
# my_url = 'https://www.doordash.com/cart/nPHxISXFV7voIgV/'
my_url = 'https://drd.sh/cart/kjbIUL/'
# res = urllib2.urlopen('https://www.doordash.com/cart/j16vxhGiOy1oyrw/')
res = urllib2.urlopen(my_url)
html = res.read()
soup = BeautifulSoup(html, 'html.parser')
print soup.title.string.split('Delivery')[0]
# print html
# driver = webdriver.PhantomJS()
# options = webdriver.ChromeOptions()
# options.add_argument('headless')

# driver = webdriver.Chrome(chrome_options=options)
# driver.get(url)
# p_element = driver.find_element_by_id(id_='inro')
# print p_element.text
# # html = res.read()




# session = dryscrape.Session()
# session.visit(my_url)
# response = session.body()
# soup = BeautifulSoup(response)
# soup.find(id="intro-text")

# print html