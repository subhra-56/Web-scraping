import requests
from bs4 import BeautifulSoup
import re

username=[]
rating=[]
reviews=[]
detailed_reviews=[]
url="https://www.commonsensemedia.org/app-reviews/khan-academy-kids/user-reviews/adult"
result=requests.get(url).text
doc=BeautifulSoup(result,"html.parser")

user_reviews=doc.find_all(class_="user-generated-content")
for user_review in user_reviews:
    name=user_review.find_all(class_="user-summary__name")
    username.append(name[0].a.string)
    rate=user_review.find_all(class_="rating__score")
    ratings=rate[0].find_all(class_="active")
    rating.append(len(ratings)-1)
    rvw=user_review.find_all(class_="user-generated-content__title")
    if(rvw==[]):
        reviews.append("N.A.")
    else:
        reviews.append(rvw[0].string)
        rvw=user_review.find_all(class_="user-generated-content__title")
    drvw=user_review.find_all(class_="reveal__content collapse")
    if(drvw==[]):
        detailed_reviews.append("N.A.")
    else:
        detailed_reviews.append(drvw[0].string.strip())
print(username)
print(rating)
print(reviews)
print(detailed_reviews)
