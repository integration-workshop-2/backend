import requests

# requests.post(
#     url="http://10.42.0.1:5000/api/routines",
#     json={
#         "patient_id": "c6c6f3b2-343e-4968-a6a6-9cd8d67e108e",
#         "routine_items_list": [
#             {
#                 "medicine_id": "e088d9d0-262d-46d4-8828-0f58861c76b0",
#                 "medicine_quantity": 1,
#                 "week_day": "Saturday",
#                 "day_time": "15:20",
#             },
#         ],
#     },
# )

# print(
#     requests.get(
#         "http://10.42.0.1:5000/api/list_patient_vital_signs/535c97d7-30f5-494d-9ec6-52898ea41e30"
#     ).json()
# )

requests.get("http://10.42.0.3:5000/api/control_motor/1")
# requests.get("http://10.42.0.3:5000/api/control_motor/2")
# requests.get("http://10.42.0.3:5000/api/control_motor/3")

# requests.post(
#     url="http://10.42.0.1:5000/api/patients", json={"name": "Joao Pedro dos Reis"}
# )

# requests.get("http://10.42.0.1:5000/api/patients")
