from bs4 import BeautifulSoup
import requests

url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
site = requests.get(url)
text = site.text
cookies = site.cookies
cont = site.content

print(cont)

print(cookies)

code = int(site.status_code)
print(code)

soup = BeautifulSoup(text, 'html.parser')

paragraph = soup.find_all('p')

print(paragraph)

f = open("siteparagraph.txt", "w")

for each in paragraph:
    f.write(str(each) + '\n')

f.close()



