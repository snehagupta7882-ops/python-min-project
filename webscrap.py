#web scraping 
import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser") #<html>
  #

titles = soup.find_all("a") # headlines like <a> is ke andar jo kuch v hota hai</a>

file = open("headlines.txt", "w")

for i in titles: # headline store in title
    file.write(i.text + "\n")

file.close()

print("done")



#Website
 #    ↓
#r.get()
   #  ↓
#HTML mila
 #    ↓
#BeautifulSoup()
 #    ↓
#HTML read hua
  #   ↓
#find_all("a")
 #    ↓
#Saare <a> tags mile
 #    ↓
#for loop
 #    ↓
#Ek-ek tag ka text nikala
 #    ↓
#headlines.txt me save kar diya