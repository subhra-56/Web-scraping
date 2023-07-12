import requests
import re
from bs4 import BeautifulSoup
import pandas

i=1

url="https://steamcommunity.com/app/438100/reviews/?browsefilter=toprated&snr=1_5_100010_"

while i<10:
    
    i+=1

    result=requests.get(url).text
    doc=BeautifulSoup(result,"html.parser")
    recmds=doc.find_all(class_="vote_header")
    dates=doc.find_all(class_="date_posted")
    comments=doc.find_all(class_="apphub_CardTextContent")
      
  
    for recmd,date,comment in zip(recmds,dates,comments):
        
        print(date.string[8:])
        print(recmd.find(class_="title").string)
        print(recmd.find(class_="hours").string.split('h')[0])
        print(comment.get_text(strip=True).split('Early Access Review')[1])
        print()
    
    try:
        link=doc.find("input", {"name": "userreviewscursor"})["value"]
        url=f"https://steamcommunity.com/app/438100/homecontent/?userreviewscursor={link}&userreviewsoffset={(i-1)*10}&p={i}&workshopitemspage={i}&readytouseitemspage={i}&mtxitemspage={i}&itemspage={i}&screenshotspage={i}&videospage={i}&artpage={i}&allguidepage={i}&webguidepage={i}&integratedguidepage={i}&discussionspage={i}&numperpage=10&browsefilter=toprated&browsefilter=toprated&l=english&appHubSubSection=10&filterLanguage=default&searchText=&maxInappropriateScore=50&forceanon=1"
    except:
        break
      

    




