import requests
from behave import *

from payload import *
from utilities.configurations import *
from utilities.resources import *


@given('the book details which need to be added in the Library')
def step_impl(context):
    context.url = getConfig()['API']['endpoint']
    context.header = {"Content-Type": "application/json"}
    context.addpayload = add_payload("gig8righ", 678)

@given('the book details with {isbn} and {aisle}')
def step_impl(context, isbn, aisle):
    context.url = getConfig()['API']['endpoint']
    context.header = {"Content-Type": "application/json"}
    context.addpayload = add_payload(isbn, aisle)


@when('when we execute AddBook PostAPI method')
def step_impl(context):
    context.response = requests.post(context.url + ApiResources.addBook, json=context.addpayload, headers=context.header, )


@then('book is successfully added')
def step_impl(context):
    print(context.response.json())
    response_json = context.response.json()
    context.book_id = response_json['ID']
    print(context.book_id)
    assert response_json["Msg"] == "successfully not added"


@given('I have GitHub credentials')
def step_impl(context):
    context.se = requests.session()
    context.se.auth = auth = ('adityakakade21', getPassword())



@when('I hit getRepo api of github')
def step_impl(context):
    context.url = ApiResources.github_url
    context.response = context.se.get(context.url, verify=False)



@then("Status code of response should be {statusCode:d}")
def step_impl(context, statusCode):
    print(context.response.status_code)
    assert context.response.status_code == statusCode
