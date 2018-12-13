import requests
from bs4 import BeautifulSoup
response=requests.get('https://www.dominos.co.in/store-location/bangalore')
content=response.content
soup=BeautifulSoup(content,"html.parser")
parent=soup.find_all("div",attrs={"class":"panel panel-default custom-panel"})
address=[]
for item in parent:
    address.append(item.find_all("div", attrs={"class": "media-body"}))
area=[]
for link in address:
    i=link[0].find_all("p",attrs={"class":"city-main-sub-title"})
    j=i[0].getText()
    area.append(j)
add=[]
for link in address:
    i=link[0].find_all("p",attrs={"class":"grey-text mb-0"})
    j=i[0].getText()
    add.append(j)
for (i,j) in zip(area,add):
    print(i,"\n\t\tAddress: ",j)
    print('')