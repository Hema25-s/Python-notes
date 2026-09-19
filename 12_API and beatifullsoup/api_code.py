#                WHAT IS API
'''
Application programming interface that allows to share data between two applications

EX:
Browser -> url -> API -> Data base - > Collect and sends to browser

Requests is the module used to take data from a API, 
pip install requests


EX:

import requests
import pandas as pd

url = 'https://jsonplaceholder.typicode.com/todos'

response = requests.get(url)
print(response.text)

unstructured_data = response.json()

titles = []
completed = []

for i in unstructured_data: 
    titles.append(i['title'])
    completed.append(i['completed'])


data = {
    'Title':titles,
    'Completed':completed
}

df = pd.DataFrame(data)
print(df.head())
'''

import requests
import pandas as pd


#   How many values you want to extract from the url
# 10-30
# for 10+1 time with https://jsonplaceholder.typicode.com/comments/1 
# append all the values in list
# convert all the url data into structured format
# a=int(input("Enter the starting value you want to extract from the url:"))
# b=int(input("Enter the ending value you want to extract from the url:"))

# ids=[]    
# names=[]
# emails=[]
# bodys=[]


# for i in range(a,b+1):
#     url=f'https://jsonplaceholder.typicode.com/comments/{i}'
#     response=requests.get(url)
#     data = response.json()
   
#     ids.append(data['id'])
#     names.append(data['name'])
#     emails.append(data['email'])
#     bodys.append(data['body'])
    

# data={
#     'ID':ids,
#     'NAMES':names,
#     'EMAIL':emails,
#     'BODY':bodys

# }
# df = pd.DataFrame(data)
# print(df.head())








import pandas as pd
import requests

first=int(input("Enter the number to start:"))
sec=int(input("Enter the number to stop:"))


albumids=[]
ids=[]
titles=[]
urls=[]
thumbnailUrls=[]


for i in range(first,sec+1):
    url= f'https://jsonplaceholder.typicode.com/photos/{i}'
    res=requests.get(url)
    data=res.json()

    albumids.append(data['albumId'])
    ids.append(data['id'])
    titles.append(data['title'])
    urls.append(data['url'])
    thumbnailUrls.append(data['thumbnailUrl'])


data={
    'Albumids':albumids,
    'Id':ids,
    'Title':titles,
    'URL':urls,
    'ThumbnailUrls':thumbnailUrls
}    
df=pd.DataFrame(data)
print(df.head())