
import requests,json

apikey = "dd519b0eb51b2d09fb2e49bc0d7b6b5a"

baseURL = "https://api.openweathermap.org/data/2.5/weather?q="

cityName = input("Enter your city : ")

completeURL = baseURL + cityName + "&appid=" + apikey

response = requests.get(completeURL)

data = response.json



print("Current Temperature", data ["main"]["tepm"])

print("Current Temperature Feels like", data["main"]["Fells_like"])

print("Maximum Temperature", data)["main"]["tepm_max"]

print("Minimum Temperature", data)["main"]["tepm_min"]





import json, sys,requests

if len(sys.argv) < 2:
    print("Usage:weather_api.py location")
    sys.exit()

location = ''.json(sys.argv[1:])

url = "http://www.weatherapi.com/data/2.5/weather?q=%s&appid=7904e6fcc5784660811122649230910" % location


response = requests.get(url)
response.raise_for_status()


weatherDAta = json.load(response.text)


data = weatherDAta['weather']
print('Current weather in %s:' % (location))
print(data[0]['main'],"-",data[0]['description'])

temp = weatherDAta['main']
print('Temperature')