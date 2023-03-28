import requests
from payload import *
import configparser
from utilities.configurations import *
from utilities.resources import *

url = getConfig()['API']['endpoint']
header={"Content-Type": "application/json"}
query = 'select * from Books'
addbook_response = requests.post(url+ApiResources.addBook,json=buildPayloadFromDB(query),headers=header,)

print(addbook_response.json())


response_json = addbook_response.json()
#print(type(response_json))
book_id = response_json['ID']
print(book_id)

# delete book

deletebook_response = requests.post(url+ApiResources.deleteBook, json={"ID": book_id}, headers=header,)

assert deletebook_response.status_code == 200
del_res = deletebook_response.json()
print(del_res["msg"])

assert del_res["msg"] == "book is successfully deleted"

# Authentication

se = requests.session()
se.auth = auth=('adityakakade21',getPassword())
url = "https://api.github.com/users"
github_response = se.get(url,verify=False)

print(github_response.json())
print(github_response.status_code)

# file upload

url = "https://httpbin.org/post"
files = {'file': open('sample.json')}
fileupload_response = requests.post(url, files=files)

print(fileupload_response.status_code)
