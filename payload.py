from utilities.configurations import *


def add_payload(isbn):
    body ={
    "name": "Devopsbasics",
    "isbn": isbn,
    "aisle": "75",
    "author": "Aditya Kakade"
    }

    return body

def buildPayloadFromDB(query):
    addbody = {}
    tp = getQuery(query)
    addbody['name']= tp[0]
    addbody['isbn']= tp[1]
    addbody['aisle']= tp[2]
    addbody['author']= tp[3]
    return addbody
