import requests
from datetime import datetime, timedelta

MY_LATITUDE = 1.357107
MY_LONGITUDE = 103.8194992

parameters = {
        "lat": MY_LATITUDE,
        "lng": MY_LONGITUDE,
        "formatted": 0,
    }
sun_API = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
sun_API.raise_for_status()
data = sun_API.json()
sunrise_time = data["results"]["sunrise"]
sunset_time = data["results"]["sunset"]

# Convert the times to datetime objects
sunrise_time_utc = datetime.fromisoformat(sunrise_time)
sunset_time_utc = datetime.fromisoformat(sunset_time)

# Calculate the local time offset (Singapore is UTC+8)
time_offset = timedelta(hours=8)

# Apply the time offset to convert to local time
sunrise_time_local = sunrise_time_utc + time_offset
sunset_time_local = sunset_time_utc + time_offset

# Format the times to only show the hour
sunrise_hour = sunrise_time_local.isoformat().split("T")
sunset_hour = sunset_time_local.isoformat().split("T")

print(sunrise_hour)
print(sunset_hour)

time_now = datetime.now()
print(time_now)