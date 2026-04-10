# SKYE Weather Agent

A visually appealing AI-powered weather agent that uses the Groq API to fetch weather data and generate structured reports. Features an interactive CLI with a modern interface.

## Features

- Fetches current weather for any location using latitude and longitude via OpenWeatherMap API
- Generates and writes detailed weather reports to text files
- Interactive chat interface with a polished CLI design
- Uses structured JSON output for consistent, formatted weather reports
- Tool-based architecture for extensible functionality

## Project Structure

- `main.py`: Entry point with the interactive CLI interface
- `agent/`: Core agent logic
  - `dispatcher.py`: Dispatches tool calls to appropriate functions
  - `runner.py`: Manages LLM integration with Groq API and response formatting
- `tools/`: Available tools for the agent
  - `get_weather.py`: Fetches weather data from OpenWeatherMap
  - `write_report.py`: Writes formatted reports to files
- `requirements.txt`: Python dependencies
- `.env.example`: Example environment file for API keys (create this file as .env)

## Installation

1. Clone the repository
2. Create a virtual environment: `python -m venv .venv`
3. Activate it: `source .venv/bin/activate` (Linux/Mac) or `.venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`

## Setup

Create a `.env` file in the root directory with your API keys:

```
OPENWEATHER_API_KEY=your_openweather_api_key
GROQ_API_KEY=your_groq_api_key
```

- Get OpenWeatherMap API key from [openweathermap.org](https://openweathermap.org/api)
- Get Groq API key from [groq.com](https://groq.com)

## Usage

Run the agent: `python main.py`

You'll see the SKYE header, then enter your queries. Examples:

- "What's the weather in New York?"
- "Write a report for the weather in London"

The agent will respond with formatted weather information or confirm report writing.

### Example Output

```
╔══════════════════════════════╗
║           SKYE v1.0           ║
╚══════════════════════════════╝

You: What's the weather in Tokyo?
SKYE: Weather Report:
Temperature: 22.5°C
Humidity: 65%
Wind Speed: 3.2 m/s
Description: clear sky
────────────────────────────────────────
```

## Contributing

I'm open to pull requests! Feel free to add new cool tools to expand the agent's capabilities.

### How to Add New Tools

1. Create a new file in `tools/` with your tool function and schema.
2. Update `tools/__init__.py` to import and include your tool in `schemas` and `tools` dict.
3. Ensure the function accepts keyword arguments matching the schema parameters.

## License

MIT License

## Dependencies

- openai: For LLM integration
- requests: For API calls
- python-dotenv: For environment variables

## Notes

- Free OpenWeatherMap tier has rate limits (60 calls/minute)
- Ensure API keys are valid and have sufficient credits
