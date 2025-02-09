import requests

# requests.delete(
#     url="http://10.42.0.1:5000/api/routines/fa4a665e-21d2-4427-99e5-ef9f0a07d748"
# )

# requests.post(
#     url="http://10.42.0.1:5000/api/routines",
#     json={
#         "patient_id": "4e83bbc2-99fc-47fc-8b1f-d0f771235e61",
#         "routine_items_list": [
#             {
#                 "day_time": "15:07",
#                 "week_day": "Sunday",
#                 "medicine_id": "4c3b5be2-8fb2-4319-9801-e435b8568ed3",
#                 "medicine_quantity": 2,
#             },
#             {
#                 "day_time": "15:07",
#                 "week_day": "Sunday",
#                 "medicine_id": "71432942-482d-4d7b-a876-659573b5c2dc",
#                 "medicine_quantity": 1,
#             },
#         ],
#     },
# )

# requests.delete(
#     url="http://10.42.0.1:5000/api/routines/b8e0b19a-4c6f-45e2-af1f-db248783b098"
# )

# for _ in range(15):
#     requests.get("http://10.42.0.2/capture")

# requests.post(
#     "http://10.42.0.1:5000/api/patients",
#     json={"name": "Viviane"},
# )


# requests.get(
#     "http://10.42.0.1:5000/api/recognize_images/eaf631cf-c0aa-4c6c-b348-58b532a2a515"
# )


# requests.get("http://10.42.0.3:5000/api/control_motor/1")

# requests.get("http://10.42.0.3:5000/api/control_motor/2")

# requests.get("http://10.42.0.3:5000/api/control_motor/3")

while 1:
    print(requests.get(url="http://10.42.0.3:5000/api/vital_signs_sensors").json())
