# use requests to get data from the API
import requests

url = "https://api.github.com/users/octocat"

response = requests.get (url)

if response.status_code == 200:
    data = response.json()
    print ("search or get all data \n 1 - search \n 2 - get all data")
    choice = input ("Enter your choice: ")
    if choice == "1":
        serch = input ("Enter the search term: ")
        if serch in data:
            print (f"{serch} found in data")
            print (data[serch])
        else:
            print (f"{serch} not found in data")
    elif choice == "2":
        print (data)
    else:
        print ("Invalid choice")
else:
    print (f"Failed to get data from API. Status code: {response.status_code}")