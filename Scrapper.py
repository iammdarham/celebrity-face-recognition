from csv import writer
import csv
from google_play_scraper import Sort, reviews


result, continuation_token = reviews(
    'com.supercell.clashofclans',
    lang='en', 
    country='in', 
    sort=Sort.NEWEST, 
    count=500,
)

result, _ = reviews(
    'com.supercell.clashofclans',
    continuation_token=continuation_token 
)
print(result)
fields = ['UserName','Ratings','Reviews']
list1 = []
for i in result:
    list1.append([i['userName'],i['score'],i['content']])
print(list1)

with open('C:/Users//moham/Desktop/Project/data1.csv','w',encoding='UTF-8',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(fields)
    writer.writerows(list1)

