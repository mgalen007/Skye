
get_weather_schema = {
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get the current weather for a city. Use this when the user asks about weather",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "The city name, e.g Kigali"
                }
            },
            "required": ["city"]
        }
    }
}

def get_weather(city: str) -> None:
    return f"Sunny in {city}, 24°C"

    