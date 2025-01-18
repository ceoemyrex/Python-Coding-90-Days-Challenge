#Project:
# Create a Python script that fetches data from a public API (e.g., OpenWeatherMap) and displays the weather.


import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

def get_weather(city, api_key):
    """Fetches weather data from OpenWeatherMap API.

    Args:
        city: The name of the city.
        api_key: Your OpenWeatherMap API key.

    Returns:
        A dictionary containing weather data, or None if an error occurs.
        Prints an error message to the console if there is an error.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Use metric units (Celsius)
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        if response.status_code == 404:
            print("City not found. Please check the city name.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def display_weather(weather_data):
    """Displays formatted weather information.
    Args:
        weather_data: The dictionary containing the weather data.
    """
    if weather_data:
        city = weather_data["name"]
        description = weather_data["weather"][0]["description"].capitalize()
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]
        print(f"Weather in {city}:")
        print(f"Description: {description}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("No weather data to display.")

if __name__ == "__main__":
    api_key = os.getenv("OPENWEATHERMAP_API_KEY") # Get API key from environment variable
    if not api_key:
        print("Error: OPENWEATHERMAP_API_KEY environment variable not set.")
        exit()

    try:
        city = input("Enter city name: ")
        weather = get_weather(city, api_key)
        display_weather(weather)
    except EOFError:
        print("\nInput ended.")
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
    except Exception as e:
        print(f"An unexpected error occurred during input: {e}")