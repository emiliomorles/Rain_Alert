import requests  # Import data from an API
from twilio.rest import Client


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"  # I copied everything before the ? symbol
# https://api.openweathermap.org/data/2.5/weather?lat=15.78&lon=-86.76&appid=6d19077dc346ca9de467fbee1a94e551
api_key = "OPENWEATHERMAP_API_KEY"  # This is my API key from openweathermap.org

account_sid = "TWILIO_ACCOUNT_SID"  # This is my account_sid from twilio.com
auth_token = "TWILIO_AUTH_TOKEN"  # This is my auth_token from twilio.com


weather_params = {
    "lat": 41.32,
    "lon": 19.81,
    "appid": api_key,
    "cnt": 4,  # Only have 4 timestamps
}

response = requests.get(OWM_Endpoint, params=weather_params)
# print(response.status_code)  # If I get a 200 response, it means everything is OK. 🆗👍

# print(response.json())
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
        # print("Bring the Umbrella with you")

if will_rain:
    # print("Bring the Umbrella with you")
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="Remember to bring an Umbrella. Today it is going to rain ☔",
            from_="PHONE PROVIDED BY TWILIO",
            to="MY PHONE"
        )
    print(message.status)
