# Weather Agent Crew 🌤️

A CrewAI-powered weather information system that demonstrates the use of multiple AI agents working together to fetch accurate weather data.

## Overview

This project showcases the implementation of a multi-agent system using CrewAI, where two specialized agents collaborate to provide weather information:

1. **Geocoding Expert**: Converts city names into precise geographical coordinates
2. **Weather Expert**: Uses these coordinates to fetch detailed weather information

The system uses OpenWeatherMap's API for both geocoding and weather data.

## Features

- City name to coordinates conversion (supports city names with country information)
- Detailed weather information including:
  - Temperature (°C)
  - Feels like temperature
  - Humidity
  - Weather conditions
  - Wind speed

## Prerequisites

- Python 3.8+
- OpenWeatherMap API key

## Installation

1. Clone the repository:

```bash
git clone https://github.com/mcallec1/weather-agent-crew.git
cd weather-agent-crew
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set up your environment variables:

```bash
cp .env.example .env
```

Then edit `.env` and add your OpenWeatherMap API key.

## Usage

Run the weather crew:

```bash
python -m src.get_latest_weather.main
```

By default, it will fetch weather for Melbourne, Australia. You can modify the city in `src/get_latest_weather/main.py`.

## Project Structure

```
weather-agent-crew/
├── src/
│   └── get_latest_weather/
│       ├── config/
│       │   ├── agents.yaml    # Agent configurations
│       │   └── tasks.yaml     # Task definitions
│       ├── tools/
│       │   ├── geocoding_tool.py  # City to coordinates conversion
│       │   └── weather_tool.py    # Weather data fetching
│       ├── crew.py           # Main crew implementation
│       └── main.py          # Entry point
├── .env.example
├── requirements.txt
└── README.md
```

## Technical Details

- Built with CrewAI for agent orchestration
- Uses Pydantic for input validation
- Implements proper error handling and API response processing
- Follows best practices for configuration management

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
