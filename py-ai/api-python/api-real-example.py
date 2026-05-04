import requests

def get_weather(city_lat, city_lon, city_name):
    url = "https://api.open-meteo.com/v1/forecast"
    
    params = {
        "latitude": city_lat,
        "longitude": city_lon,
        "current_weather": True
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()  # Check if the request was successful
        
        data = response.json()
        weather = data["current_weather"]
        
        # Transform the weather data into a more readable format
        weather_code = {
            0: "Clear sky",
            1: "Mainly clear",
            2: "Partly cloudy",
            3: "Overcast",
            61: "Slight rain",
            63: "Moderate rain",
        }
        
        condition = weather_code.get(weather["weathercode"], "Unknown")
        temperature = weather["temperature"]
        wind_speed = weather["windspeed"]
        
        report = {
            "city": city_name,
            "temperature": temperature,
            "condition": condition,
            "wind_speed": wind_speed
        }
        return report
    
    except requests.exceptions.RequestException as e:
        print(f"Error obteniendo clima de {city_name}: {e}")
        return None

    
def main():
    
    cities = [
        {"name": "Lima", "lat": -12.0333, "lon": -77.0333},
        {"name": "Trujillo", "lat": -8.1091, "lon": -79.0215},
        {"name": "Arequipa", "lat": -16.4090, "lon": -71.5375}
    ]

    cities_weather = []

    hottest = None

    for city in cities:
        weather_report = get_weather(city["lat"], city["lon"], city["name"])
        if weather_report is None:
            continue # Skip this city if there was an error getting the weather report
        cities_weather.append(weather_report) 
        if ( hottest is None ) or ( weather_report["temperature"] > hottest["temperature"] ):
            hottest = weather_report

    return cities_weather, hottest

if __name__ == "__main__":
    results, hottest = main()
    
    for result in results:
        print(f"{result['city']:<12} → {result['temperature']}°C, {result['condition']}")

    print(f"\n🏆 Hottest City: {hottest['city']} ({hottest['temperature']}°C)")
