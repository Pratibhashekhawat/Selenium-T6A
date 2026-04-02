import requests

payload = {
    "id": 1045,
    "category": {
        "id": 15,
        "name": "string"
    },
    "name": "doggie",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 0,
            "name": "string"
        }
    ],
    "status": "available"
}
currId = 0

def post():

    response = requests.post('https://petstore.swagger.io/v2/pet', json=payload)
    global currId
    currId = response.json()['id']

#to post data

# #payload data
# expected=200
# actual=response.status_code
# assert actual==expected ,"not equal"
# print(response.json())

def delete():
    response1 = requests.delete(f'https://petstore.swagger.io/v2/pet/{currId}', json=payload)
    print(response1.status_code)
    print(response1.json())


def get():
    response2 = requests.get(f'https://petstore.swagger.io/v2/pet/{currId}')
    print(response2.status_code)
    print(response2.json())

print(post())
get()
delete()







