from flask import Blueprint, request, jsonify
from data.use_cases.non_recognized_patients.create_non_recognized_patient.use_case import (
    CreateNonRecognizedPatientUseCase,
)
from data.parameters.non_recognized_patients.create_non_recognized_patient.parameter import (
    CreateNonRecognizedPatientParameter,
)
from data.use_cases.non_recognized_patients.list_non_recognized_patients.use_case import (
    ListNonRecognizedPatientsUseCase,
)
from typing import Dict

non_recognized_patients_bp = Blueprint("non_recognized_patients_bp", __name__)


@non_recognized_patients_bp.route("/non_recognized_patients", methods=["POST"])
def create_non_recognized_patient():
    event: Dict = request.json
    use_case = CreateNonRecognizedPatientUseCase()
    parameter = CreateNonRecognizedPatientParameter(patient_id=event.get("patient_id"))
    response = use_case.execute(parameter=parameter)
    return jsonify(response), 201


@non_recognized_patients_bp.route("/non_recognized_patients", methods=["GET"])
def list_non_recognized_patients():
    use_case = ListNonRecognizedPatientsUseCase()
    response = use_case.execute()
    return jsonify(response), 200
