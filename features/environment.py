import requests

from utilities.resources import ApiResources


def after_scenario(context, scenario):
    print('After scenario executed')

    if "library" in scenario.tags:
        deletebook_response = requests.post(context.url + ApiResources.deleteBook, json={"ID": context.book_id},
                                            headers=context.header, )
        assert deletebook_response.status_code == 200
        del_res = deletebook_response.json()
        print(del_res["msg"])

        assert del_res["msg"] == "book is successfully deleted"

