import requests

requests.put(
    "http://10.42.0.1:5000/api/patients/22178df7-6f2b-4a10-aae5-aef77d821d84",
    json={"name": "joao henrique"},
)

# while 1:
#     print(requests.get(url="http://10.42.0.3:5000/api/vital_signs_sensors").json())

# for _ in range(20):
#     requests.get("http://10.42.0.2/capture")

# requests.get(
#     "http://10.42.0.1:5000/api/recognize_images/22178df7-6f2b-4a10-aae5-aef77d821d84"
# )

# requests.post("http://10.42.0.1:5000/api/patients", json={"name": "joao h"})
