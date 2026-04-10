from dotenv import load_dotenv
import os, requests
load_dotenv()

get_weather_schema = {
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get the current weather for a city. Use this when the user asks about weather, make sure to use the latitude and longitude of the city, not the name.",
        "parameters": {
            "type": "object",
            "properties": {
                "lat": {
                    "type": "string",
                    "description": "The latitude of the city in context"
                },
                "lon": {
                    "type": "string",
                    "description": "The longitude of the city in context"
                }
        },
            "required": ["lat", "lon"]
        }
    }
}

def get_weather(lat: str, lon: str) -> str:
    key = os.getenv("OPENWEATHER_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}&units=metric"

    response = requests.get(url)

    if response.status_code == 429:
        return "API exhausted, try again after some time"
    elif not response.status_code == 200:
        return "Error: failed to retrieve weather data"
    else:
        data = response.json()

    return f"{data}"

    