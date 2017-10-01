import requests
from bs4 import BeautifulSoup 
import os
def clear():
    os.system( 'clear' )

url = "http://www.cricbuzz.com/live-cricket-scores/16854/eng-vs-wi-3rd-test-west-indies-tour-of-england-2017"
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
#print(soup)

g_data = soup.find_all(class_="cb-col cb-col-67 cb-scrs-wrp")

for item in g_data:
	print(item.text.replace("\n" , " ").strip())

#clear()