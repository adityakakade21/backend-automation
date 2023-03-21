import requests

url = 'http://rahulshettyacademy.com'
cookie = {'visit-month':'February'}

cookie_response =requests.get(url,allow_redirects=False,cookies=cookie)

#print(cookie_response.history)
print(cookie_response.status_code)

se = requests.session()
se.cookies.update({'visit-year':'2022'})

res = se.get('https://httpbin.org/cookies',cookies=cookie,timeout=1)

print(res.text)

#Attachments
url = 'https://petstore.swagger.io/v2/pet/9843217/uploadImage'
files = {'file': open('sample.json','rb')}
fileupload_response = requests.post(url, files=files)
print(fileupload_response.status_code)
print(fileupload_response.text)