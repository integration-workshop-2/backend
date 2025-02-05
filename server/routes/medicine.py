from flask import Blueprint, request, jsonify
from data.use_cases.medicine.create_medicine.use_case import CreateMedicineUseCase
from data.parameters.medicine.create_medicine.parameter import CreateMedicineParameter
from data.use_cases.medicine.delete_medicine.use_case import DeleteMedicineUseCase
from data.parameters.medicine.delete_medicine.parameter import DeleteMedicineParameter
from data.use_cases.medicine.list_available_cylinders.use_case import (
    ListAvailableCylindersUseCase,
)
from data.use_cases.medicine.list_medicine.use_case import ListMedicineUseCase
from data.use_cases.medicine.update_medicine.use_case import UpdateMedicineUseCase
from data.parameters.medicine.update_medicine.parameter import UpdateMedicineParameter
from typing import Dict
from uuid import UUID

medicine_bp = Blueprint("medicine_bp", __name__)


@medicine_bp.route("/medicine", methods=["POST"])
def create_medicine():
    event: Dict = request.json
    use_case = CreateMedicineUseCase()
    parameter = CreateMedicineParameter(
        name=event.get("name"), cylinder_number=event.get("cylinder_number")
    )
    response = use_case.execute(parameter=parameter)
    return jsonify(response), 201


@medicine_bp.route("/medicine/<uuid:medicine_id>", methods=["DELETE"])
def delete_medicine(medicine_id: UUID):
    use_case = DeleteMedicineUseCase()
    parameter = DeleteMedicineParameter(medicine_id=str(medicine_id))
    response = use_case.execute(parameter=parameter)
    return jsonify(response), 200


@medicine_bp.route("/list_available_cylinders", methods=["GET"])
def list_available_cylinders():
    use_case = ListAvailableCylindersUseCase()
    response = use_case.execute()
    return jsonify(response), 200


@medicine_bp.route("/medicine", methods=["GET"])
def list_medicine():
    use_case = ListMedicineUseCase()
    response = use_case.execute()
    return jsonify(response), 200


@medicine_bp.route("/medicine/<uuid:medicine_id>", methods=["PUT"])
def update_medicine(medicine_id: UUID):
    event: Dict = request.json
    use_case = UpdateMedicineUseCase()
    parameter = UpdateMedicineParameter(
        medicine_id=str(medicine_id),
        name=event.get("name"),
        cylinder_number=event.get("cylinder_number"),
    )
    response = use_case.execute(parameter=parameter)
    return jsonify(response), 200
