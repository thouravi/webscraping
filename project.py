import requests
import bs4
import os

# os.system('pip install requests bs4 lxml')  # install all dependencies

res = requests.get('https://blog.counter-strike.net/index.php/category/updates/')
soup = bs4.BeautifulSoup(res.text, 'lxml')
post = soup.select('div.inner_post')
update = post[0]

fout = open("output.html", "w")  # creates new file named output.html

fout.write("<html><body>")  # html tags before data
fout.write("%s" % update)  # data
fout.write("</html></body>")  # html tags after data

fout.close()  # close the function

print ("\nExport Successful > project.html")
