#insert valid api key here maybe mine is not working
import requests

key = "bd5e378503939ddaee76f12ad7a97608"

location  = input("Enter the  location name: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={key}&units=metric"


try :
    response = requests.get (url)
    print(f"Debug: Status Code aaya hai {response.status_code}")
    if response.status_code == 200:
            data = response.json()
            print (f"Temperature in {location} is {data['main']['temp']}°C \n")
            print (f"Weather description: {data['weather'][0]['description']}")
    else :
            print("error try again")
except :
    print("try again next time !")
