
import time

# Constants
API_KEY = 'YOUR_API_KEY'
BASE_URL = 'http://api.weatherapi.com/v1/'

# Function to get weather by city name
def get_weather_by_city(city):
    try:
        url = f'{BASE_URL}current.json?key={API_KEY}&q={city}'
        response = requests.get(url)
        data = response.json()
        if 'error' in data:
            print(f"Error: {data['error']['message']}")
        else:
            print(f"Weather in {city}:")
            print(f"Condition: {data['current']['condition']['text']}")
            print(f"Temperature: {data['current']['temp_c']}°C")
            print(f"Pressure: {data['current']['pressure_mb']} hPa")
            print(f"Humidity: {data['current']['humidity']}%")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Main loop
while True:
    print("Weather Checking Application")
    print("1. Check Weather by City")
    print("2. Add City to Favorites")
    print("3. Remove City from Favorites")
    print("4. List Favorite Cities")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        city = input("Enter city name: ")
        get_weather_by_city(city)
    # Add more functionality for CRUD operations on favorite cities here
    # Add code for auto-refresh as well

    elif choice == '5':
        print("Exiting the application.")
        break
    else:
        print("Invalid choice. Please try again.")

    time.sleep(15)  # Add code for auto-refresh interval