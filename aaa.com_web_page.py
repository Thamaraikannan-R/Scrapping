import csv
import requests
from bs4 import BeautifulSoup
items_name=[]
des=[]
zip_code=str(32708)
url='https://www.aaa.com/autorepair/locations/'+zip_code+'?radius=50&itemcategory=&napalocations='
response=requests.get(url)
content=response.content
soup=BeautifulSoup(content,"html.parser")
name=[]
address=[]
address2=[]
zip1=[]
parent=soup.find_all("div",attrs={"class":"aar-detail-wrapper"})
for item in parent:
    i=item.find_all("span",attrs={"class":"b3 regularText aar-title dl-item-name"})
    j=i[0].getText()
    name.append(j)
for item in parent:
    i=item.find_all("span",attrs={"class":"blk5 regularText aar-address1"})
    j=i[0].getText()
    address.append(j)
for item in parent:
    i=item.find_all("span",attrs={"class":"blk5 regularText aar-address2"})
    j=i[0].getText().replace("\n",' ').replace("\t",'').replace("  ",'').replace(","," ")
    address2.append(j)
#print(parent[0])
for item in parent:
    i=item.find_all("span",attrs={"class":"blk3 aaa-miles"})
    j=i[0].getText().__add__(" miles")
    zip1.append(j)
try:
    with open('C:/Users/lotus/Desktop/new/employee_file.csv', mode='w',newline='') as cs:
        fb = csv.writer(cs, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        fb.writerow(['Name','Address','distance from zip-'+zip_code])
        for (i, j, k, l) in zip(name, address, address2, zip1):
            fb.writerow([i,j+k, l])
        print("success...check your location")
except:
    print("Somthing went wrong... please check your destination file should be closed.")