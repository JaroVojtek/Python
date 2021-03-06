import requests
from bs4 import BeautifulSoup

r=requests.get("http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")

c=r.content

soup=BeautifulSoup(c,"html.parser")

page_num=soup.find_all("a",{"class":"Page"})[-1].text

l=[]
base_url="http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/#t=0&s="
for page in range(0,int(page_num)*10,10):
    r=requests.get(base_url+str(page))
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    all=soup.find_all("div",{"class":"propertyRow"})
    for item in all:
        d={}
        d["Address"]=item.find_all("span",{"class":"propAddressCollapse"})[0].text
        try:
            d["Locality"]=item.find_all("span",{"class":"propAddressCollapse"})[1].text
        except:
            d["Locality"]=None
        d["Price"]=item.find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ","")
        try:
            d["Beds"]=item.find("span",{"class":"infoBed"}).find("b").text
        except:
            d["Beds"]=None

        try:
            d["Area"]=item.find("span",{"class":"infoSqFt"}).find("b").text
        except:
            d["Area"]=None

        try:
            d["Full Baths"]=item.find("span",{"class":"infoValueFullBath"}).find("b").text
        except:
            d["Full Baths"]=None

        try:
            d["Half Baths"]=item.find("span",{"class":"infoValueHalfBath"}).find("b").text
        except:
            d["Half Baths"]=None

        for cg in item.find_all("div",{"class":"columnGroup"}):
            for fg, fn in zip(cg.find_all("span",{"class":"featureGroup"}), cg.find_all("span",{"class":"featureName"})):
                #print(fg.text,fn.text)
                if "Lot Size" in fg.text:
                    d["Lot Size"]=fn.text

        l.append(d)
    

import pandas
df=pandas.DataFrame(l)
