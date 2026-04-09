from .get_weather import get_weather_schema, get_weather
from .write_report import write_report_schema, write_report

# Used by agent.runner
schemas = [get_weather_schema, write_report_schema]

# Used by agent.dispatcher
tools = {
    "get_weather": get_weather,
    "write_report": write_report
}