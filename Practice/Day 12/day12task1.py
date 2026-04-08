""" Task1 : Perform API Testing for the ShopperStack
1. Post a request to register a user
2. Post a request to login the user
3. Get a request to get the user  """
import requests
#session is used to save time
session= requests.Session()
# post request to register a user
def register():
    payload = {
    "city": "Jaipur",
    "country": "India",
    "email": "pratibhaa10@gmail.com",
    "firstName": "Drashti",
    "gender": "FEMALE",
    "lastName": "Verma",
    "password": "1234",
    "phone": 9876543234,
    "state": "Rajasthan",
    "zoneId": "ALPHA"
    }

    response = session.post("https://www.shoppersstack.com/shopping/shoppers", json=payload,verify=False) # verify = False to pass SSl certificate
    print(response.text)
    assert response.status_code==201, "Register failed"
    print("User Registered with status code 201")
    return response.json()['data']['userId'] # returning the userId

userId = register()

# post request to login
def login():
    payload = {
    "email": "pratibhaa10@gmail.com",
    "password": "1234",
    "role": "SHOPPER"
    }
    # making the request
    response = session.post("https://www.shoppersstack.com/shopping/users/login", json=payload,verify=False)
    print(response.text)
    # checking the status code
    assert response.status_code==200, "login Failed"
    return response.json()['data']['jwtToken'] # returning the jwtToken

Token = login()

#setting up the bearer token for authorization
headers = {
    "Authorization": "Bearer " + Token
}

# get request to fetch user
# making the request
response = requests.get("https://www.shoppersstack.com/shoppers/userId",headers=headers,verify=False)
print(response.text)
assert response.status_code==200, "Failed"