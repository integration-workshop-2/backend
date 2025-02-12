import requests

requests.post(
    url="http://localhost:5000/api/routines",
    json={
        "patient_id": "eaf631cf-c0aa-4c6c-b348-58b532a2a515",
        "routine_items_list": [
            {
                "medicine_id": "4c3b5be2-8fb2-4319-9801-e435b8568ed3",
                "medicine_quantity": 1,
                "week_day": "Monday",
                "day_time": "08:00",
            },
            {
                "medicine_id": "71432942-482d-4d7b-a876-659573b5c2dc",
                "medicine_quantity": 2,
                "week_day": "Tuesday",
                "day_time": "12:00",
            },
        ],
    },
)
