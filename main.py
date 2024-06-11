import requests
from datetime import datetime, timedelta
import smtplib
import time

MY_EMAIL="alvinchinuk@gmail.com"
MY_PASSWORD= ""
MY_LATITUDE = 1.357107
MY_LONGITUDE = 103.8194992

def is_iss_overhead():
    # The end point
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    # # https://www.webfx.com/web-development/glossary/http-status-codes/
    response.raise_for_status()

    iss_latitude = float(response.json()["iss_position"]["latitude"])
    iss_longitude = float(response.json()["iss_position"]["longitude"])

    iss_position = (iss_latitude, iss_longitude)
    print(iss_position)

    # Compare the ISS position against ours. If +5 -5 degree from mine, then visible
    if MY_LATITUDE-5 <= iss_latitude <= MY_LATITUDE+5 and MY_LONGITUDE-5 <= iss_longitude <= MY_LONGITUDE+5:
        return True


def is_night():
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
    sunrise_hour = int(sunrise_time_local.isoformat().split("T")[1].split(":")[0])
    sunset_hour = int(sunset_time_local.isoformat().split("T")[1].split(":")[0])

    print(sunrise_hour)
    print(sunset_hour)

    time_now = datetime.now()
    print(time_now.hour)

    if time_now >= sunset_time or time_now <= sunrise_time:
        return True # it's dark

# If the ISS is close to my current position,
# and it is currently dark
# then email me to tellme to look up
# BONUS: run the code every 60 seconds

# We set an infinite loop, by conditioning to always True
while True:
    time.sleep(60)  # using the time module refresh every minute
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smpt.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject: ISS Notification \n\n The ISS is above you in the sky"
        )

