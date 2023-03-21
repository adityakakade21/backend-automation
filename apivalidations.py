import requests, json

response = requests.get('http://216.10.245.166/Library/GetBook.php', params={'AuthorName':'Rahul Shetty2'},)

dict_response = response.json()

print(dict_response)

for item in dict_response:
    if item['isbn'] == '1259789':
        print(item)
        actual_item = {'book_name': 'Devops', 'isbn': '1259789', 'aisle': '75'}
        break

expected_item = {'book_name': 'Devops', 'isbn': '1259789', 'aisle': '75'}
assert actual_item == expected_item
assert response.status_code == 200
print(response.headers)