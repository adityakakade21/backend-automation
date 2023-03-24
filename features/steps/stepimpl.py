import requests
from behave import *

from payload import *
from utilities.configurations import *
from utilities.resources import *


@given('the book details which need to be added in the Library')
def step_impl(context):
    context.url = getConfig()['API']['endpoint']
    context.header = {"Content-Type": "application/json"}
    context.addpayload = add_payload("gighrigh")




@when('when we execute AddBook PostAPI method')
def step_impl(context):
    context.addbook_response = requests.post(context.url + ApiResources.addBook, json=context.addpayload, headers=context.header, )


@then('book is successfully added')
def step_impl(context):
    print(context.addbook_response.json())
    response_json = context.addbook_response.json()
    book_id = response_json['ID']
    print(book_id)
    assert response_json["Msg"] == "successfully added"
