import requests

for _ in range(5):
    requests.get("http://10.42.0.2:80/capture")
