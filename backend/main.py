from datetime import time
from infra.repo.admin_password_repository import AdminPasswordRepository
from infra.repo.medicine_repository import MedicineRepository
from infra.repo.non_recognized_patients_repository import (
    NonRecognizedPatientsRepository,
)
from infra.repo.patient_repository import PatientRepository
from infra.repo.patients_vital_signs_repository import PatientsVitalSignsRepository
from infra.repo.alarms_repository import AlarmsRepository
from infra.repo.patient_faces_repository import PatientFacesRepository
from infra.repo.routine_repository import RoutineRepository

if __name__ == "__main__":
    patient_repo = PatientRepository()
    medicine_repo = MedicineRepository()
    routine_repo = RoutineRepository()

    # patient_repo.create_patient("ze")

    # routine_repo.create_routine(
    #     patient_id="4a87c246-bd1e-4086-afb2-84b5e0faba2f",
    #     medicine_id="d0ef1112-f1ba-4684-816f-2bded98f3f53",
    #     medicine_quantity=1,
    #     week_day="Tuesday",
    #     day_time=time(7, 30),
    # )

    # routine_repo.create_routine(
    #     patient_id="4a87c246-bd1e-4086-afb2-84b5e0faba2f",
    #     medicine_id="76486ff1-b4d7-49a7-8f9a-1e4f3f5ace17",
    #     medicine_quantity=2,
    #     week_day="Monday",
    #     day_time=time(9, 30),
    # )

    # routine_repo.create_routine(
    #     patient_id="4a87c246-bd1e-4086-afb2-84b5e0faba2f",
    #     medicine_id="76486ff1-b4d7-49a7-8f9a-1e4f3f5ace17",
    #     medicine_quantity=3,
    #     week_day="Monday",
    #     day_time=time(9, 30),
    # )

    # routine_repo.create_routine(
    #     patient_id="4a87c246-bd1e-4086-afb2-84b5e0faba2f",
    #     medicine_id="76486ff1-b4d7-49a7-8f9a-1e4f3f5ace17",
    #     medicine_quantity=3,
    #     week_day="Tuesday",
    #     day_time=time(11, 30),
    # )

    # routine_repo.update_routine(
    #     id="02c89be0-49ac-4dc9-b95a-c4f504d7c3de",
    #     medicine_id="76486ff1-b4d7-49a7-8f9a-1e4f3f5ace17",
    #     medicine_quantity=10,
    #     week_day="Saturday",
    #     day_time=time(23, 59),
    # )

    # routine_repo.delete_routine_by_patient_id("4a87c246-bd1e-4086-afb2-84b5e0faba2f")
