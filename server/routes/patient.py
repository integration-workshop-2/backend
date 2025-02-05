from flask import Blueprint, request, jsonify
from data.use_cases.patient.create_patient.use_case import CreatePatientUseCase
from data.parameters.patient.create_patient.parameter import CreatePatientParameter
from data.use_cases.patient.delete_patient.use_case import DeletePatientUseCase
from data.parameters.patient.delete_patient.parameter import DeletePatientParameter
from data.use_cases.patient.get_patient.use_case import GetPatientUseCase
from data.parameters.patient.get_patient.parameter import GetPatientParameter
from data.use_cases.patient.list_patients.use_case import ListPatientsUseCase
from data.parameters.patient.list_patients.parameter import ListPatientsParameter
from data.use_cases.patient.update_patient.use_case import UpdatePatientUseCase
from data.parameters.patient.update_patient.parameter import UpdatePatientParameter
from typing import Dict
from uuid import UUID

patient_bp = Blueprint("patient_bp", __name__)


@patient_bp.route("/patients", methods=["POST"])
def create_patient():
    event: Dict = request.json
    use_case = CreatePatientUseCase()
    parameter = CreatePatientParameter(name=event.get("name"))
    response = use_case.execute(parameter=parameter)
    return jsonify(response), 201


@patient_bp.route("/patients/<uuid:patient_id>", methods=["DELETE"])
def delete_patient(patient_id: UUID):
    use_case = DeletePatientUseCase()
    parameter = DeletePatientParameter(patient_id=str(patient_id))
    response = use_case.execute(parameter=parameter)
    return jsonify(response), 200


@patient_bp.route("/patients/<uuid:patient_id>", methods=["GET"])
def get_patient(patient_id: UUID):
    use_case = GetPatientUseCase()
    parameter = GetPatientParameter(patient_id=str(patient_id))
    response = use_case.execute(parameter=parameter)
    return jsonify(response), 200


@patient_bp.route("/patients", methods=["GET"])
def list_patients():
    use_case = ListPatientsUseCase()
    parameter = ListPatientsParameter(patient_name="")
    response = use_case.execute(parameter=parameter)
    return jsonify(response), 200


@patient_bp.route("/patients/<uuid:patient_id>", methods=["PUT"])
def update_patient(patient_id: UUID):
    event: Dict = request.json
    use_case = UpdatePatientUseCase()
    parameter = UpdatePatientParameter(
        patient_id=str(patient_id), name=event.get("name")
    )
    response = use_case.execute(parameter=parameter)
    return jsonify(response), 200
