# day33_100
I am currently engaged in a 100-day Python Bootcamp, which I am documenting and sharing my progress on GitHub. The boot camp is designed to progressively intensify, allowing me to deepen my understanding and proficiency in Python programming.

Additionally, I have chosen to include the beginner, intermediate and advanced in my documentation to provide a valuable reference for my future growth and development.

-------------------------
# Learning to use API Endpoints with Python
In this project, I've explored using API endpoints to retrieve data and perform actions based on that data. Here's a breakdown of what I've learned and implemented:

1. __Fetching ISS Position Data__
I used the Open Notify API to fetch the current position of the International Space Station (ISS). The API provides the latitude and longitude of the ISS, which I then compared to my location to determine if the ISS is overhead.

2. __Determining Day or Night__
I used the Sunrise-Sunset API to get sunrise and sunset times for my location. By converting these times from UTC to local time and comparing them to the current time, I determined whether it is currently night.

3. __Automating Notifications__
Using the smtplib library, I set up an email notification system. The program checks every minute to see if the ISS is overhead and if it is currently night. If both conditions are met, an email is sent to notify me to look up.
