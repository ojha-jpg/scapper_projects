from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

website=requests.get("https://www.imdb.com/search/title/?title_type=feature&num_votes=100,&countries=np&languages=ne&sort=user_rating,desc")


soup=BeautifulSoup(website.content,"html.parser")

data={}

movies=soup.find_all("div",class_="lister-item mode-advanced")
for movie in movies:
	movie_name=movie.find_all("a")[1].get_text()
	movie_rating=movie.find_all("strong")[0].get_text()
	data[movie_name]=movie_rating

df = pd.DataFrame(list(data.items()) ,columns = ['Movie','Rating']) 

df.to_csv("rating.csv",index=False)



