import requests

# requests.post(url="http://localhost:5000/api/patients", json={"name": "jose"})

# requests.delete(
#     url="http://localhost:5000/api/routines/935fdcb9-96c3-4e81-a139-cf7d73176154"
# )

# requests.post(
#     url="http://localhost:5000/api/routines",
#     json={
#         "patient_id": "7281b391-0e6d-4e44-93d2-4d849d1e675d",
#         "routine_items_list": [
#             {
#                 "medicine_id": "f9238387-ee87-4bf1-a951-39027859ad9a",
#                 "medicine_quantity": 2,
#                 "week_day": "Monday",
#                 "day_time": "07:00",
#             },
#             # {
#             #     "medicine_id": "df93ed6a-948f-48a9-834b-a7f5097c3ea1",
#             #     "medicine_quantity": 2,
#             #     "week_day": "Monday",
#             #     "day_time": "07:00",
#             # },
#             # {
#             #     "medicine_id": "30a0edd4-7687-4b85-9265-acb0c0a8b144",
#             #     "medicine_quantity": 4,
#             #     "week_day": "Monday",
#             #     "day_time": "09:00",
#             # },
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

# requests.delete(
#     url="http://localhost:5000/api/medicine/f9238387-ee87-4bf1-a951-39027859ad9a"
# )


from data.use_cases.medicine.delete_medicine.use_case import DeleteMedicineUseCase

from data.parameters.medicine.delete_medicine.parameter import DeleteMedicineParameter

use_case = DeleteMedicineUseCase()
parameter = DeleteMedicineParameter(medicine_id="daca1522-1f03-4c3b-9bd1-4ecaab89d3eb")
use_case.execute(parameter=parameter)
