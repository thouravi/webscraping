import requests
import bs4
import sys
import os

# os.system('pip install requests bs4 lxml')  # install all dependencies

res = requests.get("https://blog.counter-strike.net/index.php/category/updates/")
soup = bs4.BeautifulSoup(res.text, "lxml")
post = soup.select("div.inner_post")
update = post[0]

fout = open("output.html", "w")
fout.write("%s" % update)
fout.close()

readFile = open("output.html")
lines = readFile.readlines()
readFile.close()

w = open("output.html", "w")
w.writelines([item for item in lines[:-5]])
w.close()

with open("output.html", "r") as myfile:
    data = myfile.read()

readFile = open("output.html")
lines = readFile.readlines()
readFile.close()

w = open("output.html", "w")
w.writelines([item for item in lines[3:]])
w.close()

with open("output.html", "r") as myfile:
    data = myfile.read()
    
fout = open("output.html", "w")
fout.write("<html><body>")
fout.write("%s" % data)
fout.write("</html></body>")

fout.close()

print("\nExport Successful > output.html")
