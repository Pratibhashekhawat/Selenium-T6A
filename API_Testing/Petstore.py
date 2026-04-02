import requests

#fetching the data
response= requests.get("https://petstore.swagger.io/v2/store/inventory")

#using the response variable
print(response.status_code)
print(response.text)
responsejson = response.json()
print(responsejson['available'])

expected=200
actual= response.status_code
assert expected==actual ,f'Not Equal {actual}'

