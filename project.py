import requests
import bs4
res = requests.get('https://blog.counter-strike.net/index.php/category/updates/')
soup = bs4.BeautifulSoup(res.text, 'lxml')
post = soup.select('div.inner_post')
update = post[0]
info = update.getText()
print (info)
