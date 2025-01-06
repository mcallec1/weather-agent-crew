from typing import Any
from langchain.tools import Tool
from langchain.tools.base import ToolException
import requests
import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field

# Load environment variables
load_dotenv()

class WeatherInput(BaseModel):
    """Input for the weather tool."""
    lat: float = Field(..., description="The latitude of the location")
    lon: float = Field(..., description="The longitude of the location")

def get_weather(lat: float, lon: float) -> str:
    """
    Get current weather for coordinates using OpenWeatherMap API
    Args:
        lat: Latitude of the location
        lon: Longitude of the location
    Returns:
        str: Formatted weather information
    """
    api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    if not api_key:
        raise ToolException("OpenWeatherMap API key not found in environment variables")
        
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key,
        "units": "metric"  # Use metric units for temperature
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        
        weather_info = {
            "location": data["name"],
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "conditions": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"]
        }
        
        return f"""Current weather in {weather_info['location']}:
Temperature: {weather_info['temperature']}°C
Feels like: {weather_info['feels_like']}°C
Humidity: {weather_info['humidity']}%
Conditions: {weather_info['conditions'].capitalize()}
Wind Speed: {weather_info['wind_speed']} m/s"""
        
    except requests.exceptions.RequestException as e:
        return f"Error fetching weather data: {str(e)}"

weather_tool = Tool(
    name="get_weather",
    description="Get current weather information for a location using latitude and longitude coordinates",
    func=get_weather,
    args_schema=WeatherInput
) 