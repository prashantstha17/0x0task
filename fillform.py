import requests

url = "http://localhost"

def fillFrom():
    data = {
        "name":"yourname", 
        "email":"youremail@email.com",
        "submit":"Submit"}

    request = requests.post(url, data=data)
    print("Form Submitted")
    # print(request.text)

addHeader = input("Do you want to add custom headers?(y/n): ")
if addHeader == "y":
    headers = {}
    while True:
        header = input("Enter header (format: key:value): ")
        if header == "":
            break
        key, value = header.split(":")
        headers[key] = value
    fillFrom()
else:
    fillFrom()