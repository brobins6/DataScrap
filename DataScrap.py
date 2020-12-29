# from urllib.request import Request, urlopen 
import requests
from bs4 import BeautifulSoup as soup 


uClient = requests.get("https://scholar.google.com/scholar?hl=en&as_sdt=0%2C6&q=covid+19+pandemic&oq=covid+19+violence")
# raw_html = urlopen(uClient).read()

page_soup = soup(uClient.content, "html.parser")
containers = page_soup.find_all("div", {"class":"gs_r gs_or gs_scl"})
fileName = "covid.csv"
f = open(fileName, "w", encoding="utf-8")
headers = "title, author date location, summary, cited number\n"
f.write(headers)
for container in containers:
    title = container.find_all("h3")[0].a.text
    author = container.find_all("div",{"class": "gs_a"})[0].text
    summary = container.find_all("div", {"class":"gs_rs"})[0].text
    for elem in container.find_all('a',href=True):
        if "cites" in elem['href']:
            numCited = elem.text


    f.write(title.replace(",", " ") + "," + author.replace(",", " ") + "," + summary.replace(",", " ") + "," + numCited + "\n")
f.close()  

