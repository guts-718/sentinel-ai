import requests

TOKEN = "8656007370:AAE5SINe0dLpcjoHChNH0nJdk8MsdW3iHI8"

url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
print(requests.get(url).json())