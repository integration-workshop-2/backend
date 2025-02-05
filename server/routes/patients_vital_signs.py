from flask import Blueprint, request, jsonify
from data.use_cases.patients_vital_signs.create_patient_vital_signs.use_case import (
    CreatePatientVitalSignsUseCase,
)
from data.parameters.patients_vital_signs.create_patient_vital_signs.parameter import (
    CreatePatientVitalSignsParameter,
)
from data.use_cases.patients_vital_signs.get_patient_vital_signs.use_case import (
    GetPatientVitalSignsUseCase,
)
from data.parameters.patients_vital_signs.get_patient_vital_signs.parameter import (
    GetPatientVitalSignsParameter,
)
from data.use_cases.patients_vital_signs.list_patient_vital_signs.use_case import (
    ListPatientVitalSignsUseCase,
)
from data.parameters.patients_vital_signs.list_patient_vital_signs.parameter import (
    ListPatientVitalSignsParameter,
)
from typing import Dict
from uuid import UUID

patients_vital_signs_bp = Blueprint("patients_vital_signs_bp", __name__)


@patients_vital_signs_bp.route("/patient_vital_signs", methods=["POST"])
def create_patient_vital_signs():
    event: Dict = request.json
    use_case = CreatePatientVitalSignsUseCase()
    parameter = CreatePatientVitalSignsParameter(
        patient_id=event.get("patient_id"),
        bpm=event.get("bpm"),
        oxygenation_percentage=event.get("oxygenation_percentage"),
    )
    response = use_case.execute(parameter=parameter)
    return jsonify(response), 201


@patients_vital_signs_bp.route(
    "/patient_vital_signs/<uuid:patient_vital_signs_id>", methods=["GET"]
)
def get_patient_vital_signs(patient_vital_signs_id: UUID):
    use_case = GetPatientVitalSignsUseCase()
    parameter = GetPatientVitalSignsParameter(id=str(patient_vital_signs_id))
    response = use_case.execute(parameter=parameter)
    return jsonify(response), 200


@patients_vital_signs_bp.route(
    "/list_patient_vital_signs/<uuid:patient_vital_signs_id>", methods=["GET"]
)
def list_patient_vital_signs(patient_vital_signs_id: UUID):
    use_case = ListPatientVitalSignsUseCase()
    parameter = ListPatientVitalSignsParameter(patient_id=str(patient_vital_signs_id))
    response = use_case.execute(parameter=parameter)
    return jsonify(response), 200
