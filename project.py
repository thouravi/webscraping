import requests
import bs4
import sys
import os

# os.system('pip install requests bs4 lxml')  # install all dependencies

res = requests.get("https://blog.counter-strike.net/index.php/category/updates/")
soup = bs4.BeautifulSoup(res.text, "lxml")
post = soup.select("div.inner_post")
update = post[0]

# creates new file named output.html and read all lines

fout = open("output.html", "w")
fout.write("%s" % update)  # data
fout.close()

readFile = open("output.html")
lines = readFile.readlines()
readFile.close()

# remove last lines from output.html file

w = open("output.html", "w")
w.writelines([item for item in lines[:-5]])
w.close()

# copy contents of output.html file to string

with open("output.html", "r") as myfile:
    data = myfile.read().replace("\n", "")

# add html tags to output.html file

fout = open("output.html", "w")  # creates new file named final_output.html

fout.write("<html><body>")  # html tags before data
fout.write("%s" % data)  # data
fout.write("</html></body>")  # html tags after data

fout.close()  # close the function

print("\nExport Successful > output.html")
