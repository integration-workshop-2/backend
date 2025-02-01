import requests

# requests.post(url="http://localhost:5000/api/patients", json={"name": "jose"})

# requests.delete(
#     url="http://localhost:5000/api/routines/935fdcb9-96c3-4e81-a139-cf7d73176154"
# )

# requests.put(
#     url="http://localhost:5000/api/routines/25ca3abb-fa76-4e25-912b-a6b3c3c51129",
#     json={
#         "patient_id": "7281b391-0e6d-4e44-93d2-4d849d1e675d",
#         "routine_items_list": [
#             {
#                 "medicine_id": "b712f1bb-8bc3-4ee4-bd33-3bad145f5eda",
#                 "medicine_quantity": 2,
#                 "week_day": "Monday",
#                 "day_time": "07:00",
#             },
#             {
#                 "medicine_id": "3398eb4a-c531-4fea-b743-763ab57f6b9b",
#                 "medicine_quantity": 2,
#                 "week_day": "Monday",
#                 "day_time": "07:00",
#             },
#             {
#                 "medicine_id": "3398eb4a-c531-4fea-b743-763ab57f6b9b",
#                 "medicine_quantity": 4,
#                 "week_day": "Monday",
#                 "day_time": "09:00",
#             },
#             # {
#             #     "medicine_id": "df93ed6a-948f-48a9-834b-a7f5097c3ea1",
#             #     "medicine_quantity": 3,
#             #     "week_day": "Monday",
#             #     "day_time": "09:00",
#             # },
#         ],
#     },
# )


# requests.post(
#     url="http://localhost:5000/api/medicine",
#     json={"name": "codein", "cylinder_number": 2},
# )

requests.delete(
    url="http://localhost:5000/api/patients/7281b391-0e6d-4e44-93d2-4d849d1e675d"
)

# requests.delete(
#     url="http://localhost:5000/api/routines/e9cda783-a671-47eb-84f9-1cd27adfe321"
# )
