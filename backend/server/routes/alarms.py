from flask import Blueprint, request, jsonify
from data.use_cases.alarms.create_alarm.use_case import CreateAlarmUseCase
from data.parameters.alarms.create_alarm.parameter import CreateAlarmParameter
from data.use_cases.alarms.list_alarms.use_case import ListAlarmsUseCase
from typing import Dict

alarms_bp = Blueprint("alarms_bp", __name__)


@alarms_bp.route("/alarms", methods=["POST"])
def create_alarm():
    event: Dict = request.json
    use_case = CreateAlarmUseCase()
    parameter = CreateAlarmParameter(
        patient_vital_signs_id=event.get("patient_vital_signs_id")
    )
    response = use_case.execute(parameter=parameter)
    return jsonify(response), 201


@alarms_bp.route("/alarms", methods=["GET"])
def list_alarms():
    use_case = ListAlarmsUseCase()
    response = use_case.execute()
    return jsonify(response), 201
