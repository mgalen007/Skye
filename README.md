# Mini Weather Agent

A simple AI-powered weather agent that uses OpenAI/Groq API to fetch weather data and generate reports.

## Features

- Fetches current weather for any city using latitude and longitude via OpenWeatherMap API
- Generates and writes weather reports to text files
- Interactive chat interface for querying weather information

## Project Structure

- `main.py`: Entry point for the interactive agent
- `agent/`: Core agent logic
  - `dispatcher.py`: Dispatches tool calls
  - `runner.py`: Runs the agent with LLM integration
- `tools/`: Available tools
  - `get_weather.py`: Fetches weather data
  - `write_report.py`: Writes reports to files
- `requirements.txt`: Python dependencies
- `sample.txt`, `sample2.txt`, `test.txt`: Sample files

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

Then enter prompts like:
- "What's the weather in New York?"
- "Write a report for the weather in London"

The agent will use tools to fetch data and respond accordingly.

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
