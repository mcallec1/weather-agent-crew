from typing import Any
from langchain.tools import Tool
from langchain.tools.base import ToolException
import requests
import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field

# Load environment variables
load_dotenv()

class GeoCodingInput(BaseModel):
    """Input for the geocoding tool."""
    city: str = Field(..., description="The name of the city to get coordinates for (can include country, e.g. 'Melbourne, Australia')")

def get_coordinates(city: str) -> str:
    """
    Get latitude and longitude coordinates for a city using OpenWeatherMap's Geocoding API
    Args:
        city: Name of the city to get coordinates for (can include country)
    Returns:
        str: Formatted coordinates information
    """
    api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    if not api_key:
        raise ToolException("OpenWeatherMap API key not found in environment variables")
        
    base_url = "http://api.openweathermap.org/geo/1.0/direct"
    
    # Split city and country if provided
    city_parts = [part.strip() for part in city.split(',')]
    city_name = city_parts[0]
    country_code = city_parts[1] if len(city_parts) > 1 else None
    
    params = {
        "q": city,  # Use full city string including country
        "limit": 1,
        "appid": api_key
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        
        if not data:
            return f"Could not find coordinates for city: {city}"
            
        location = data[0]
        return f"Coordinates for {city}:\nLatitude: {location['lat']}\nLongitude: {location['lon']}"
        
    except requests.exceptions.RequestException as e:
        return f"Error fetching coordinates: {str(e)}"

geocoding_tool = Tool(
    name="get_coordinates",
    description="Get latitude and longitude coordinates for a city using OpenWeatherMap's Geocoding API",
    func=get_coordinates,
    args_schema=GeoCodingInput
) 