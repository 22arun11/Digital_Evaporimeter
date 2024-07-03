from django.shortcuts import render
import math
from django.shortcuts import render
import json
import urllib.request 

def index(request): 
	
  api_key = 'df8ee79f2dcd41a3983173032240905'
  city = 'Madukkarai'

  source1 = urllib.request.urlopen(
    'http://api.weatherapi.com/v1/forecast.json?key=' + api_key + '&q=' + city  + '&days=7').read()
  list_of_data = json.loads(source1) 
  print(list_of_data)
  if 'forecast' not in list_of_data:
    print("Error: 'forecast' key not found in API response")
    return
  temperature = list_of_data['current']['temp_c']  # Temperature is already in Celsius
  humidity = list_of_data['current']['humidity'] / 100  # Convert to a ratio
  wind_speed = list_of_data['current']['wind_kph'] / 3.6  # Convert from kph to m/s
  evaporation_rate = (0.6108 * math.exp((17.27 * temperature) / (temperature + 237.3))) * (1 - humidity) * wind_speed
  # data for variable list_of_data 
  data = {
    "icon": list_of_data['current']['condition']['icon'],
    "gust": list_of_data['current']['gust_kph'],
  "forecast": list_of_data['forecast']['forecastday'],
  "country_code": str(list_of_data['location']['country']),
  "coordinate": str(list_of_data['location']['lon']),
  "current_weather": list_of_data['current']['condition']['text'],
  "last_updated": list_of_data['current']['last_updated'],
  "temp_c": list_of_data['current']['temp_c'],
  "pressure_mb": list_of_data['current']['pressure_mb'],
  "pressure_in": list_of_data['current']['pressure_in'],
  "wind_mph": list_of_data['current']['wind_mph'],
  "wind_kph": list_of_data['current']['wind_kph'],
  "wind_degree": list_of_data['current']['wind_degree'],
  "wind_dir": list_of_data['current']['wind_dir'],
  "precip_mm": list_of_data['current']['precip_mm'],
  "precip_in": list_of_data['current']['precip_in'],
  "humidity": list_of_data['current']['humidity'],
  "cloud": list_of_data['current']['cloud'],
  "uv": list_of_data['current']['uv'],
  "evaporation_rate": evaporation_rate
}
  
  return render(request, "index.html", data) 

