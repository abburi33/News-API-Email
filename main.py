import os
import requests
from send_mail import send_mail

api_key = os.getenv("NEWS_API_KEY")
topic = "Machine Learning"
url = f"https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      f"from=2023-03-26&" \
      f"sortBy=popularity&" \
      f"language=en&" \
      f"apiKey={api_key}"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

body = ""
for article in content["articles"][:5]:
    if article['title'] is not None:
        body = f"Subject: {topic} News \n" \
               + body \
               + article['title'] + "\n" \
               + article['description'] + "\n" \
               + article['url'] + 2*"\n"

body = body.encode('utf-8')
send_mail(body)
