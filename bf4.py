import requests
from bs4 import BeautifulSoup

page=requests.get('https://forecast.weather.gov/MapClick.php?lat=36.37410569300005&lon=-119.27022999999997')


soup = BeautifulSoup(page.content,'html.parser')
    
    


week=soup.find(id="seven-day-forecast-body")
tday=week.find(id)
#print(week)
#print(week.find_all(class_="period-name"))
#print(week.find_all(class_="temp temp-high"))
day=[]
temp=[]
descipt=[]

for x in week.find_all(class_="period-name"):
    print(x.get_text())
    day.append(x.get_text())
for x in week.find_all(class_="temp"):
    print(x.get_text())
    temp.append(x.get_text())
print(len(day))
    
for n in range(len(day)):
    print(day[n],"----->",temp[n])
    
    
    
 
    
