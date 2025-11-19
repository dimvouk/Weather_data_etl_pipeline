import requests

api_key = '00e5c8b3458ae3178545a8a073848a3e' 
 
lat = '55.6761' # Use the latitude of your desired location
lon = '12.5683' # Use the longitude of your desired location

url = 'https://api.openweathermap.org/data/2.5/weather' # Current weather data
complete_url = f"{url}?lat={lat}&lon={lon}&appid={api_key}&units=metric"
response = requests.get(complete_url)
    
# Read response:
if response.status_code == 200:
    response_json = response.json()
    print(response_json)
else:
    print(f"Error: Unable to fetch data. Status code {response.status_code}")
    raise requests.exceptions.HTTPError(response.text)