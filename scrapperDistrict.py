from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv
with open("data.csv", "w", newline="") as aa:
	file=csv.writer(aa)
	file.writerow(["District Name","Confirmed","Death","Recovered"])

website=requests.get("https://kathmandupost.com/covid19")

soup = BeautifulSoup(website.content,"html.parser")

table=soup.select(".district-row")

for element in table:
	district_name=element.select(".district-name")[0].get_text()
	
	Confirmed=element.find_all("span")[1].get_text()
	Death=element.find_all("span")[2].get_text()
	Recovered=element.find_all("span")[3].get_text()
	with open("data.csv", "a", newline="") as aa:
		file=csv.writer(aa)
		file.writerow([district_name,Confirmed,Death,Recovered])

	

#df=pd.DataFrame.from_dict(list(data.items()))
#print(df.head())
