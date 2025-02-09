from flask import Blueprint, request, jsonify
from data.use_cases.routine.create_routine.use_case import CreateRoutineUseCase
from data.parameters.routine.create_routine.parameter import (
    CrateRoutineItemParameter,
    CreateRoutineParameter,
)
from data.use_cases.routine.delete_routine.use_case import DeleteRoutineUseCase
from data.parameters.routine.delete_routine.parameter import DeleteRoutineParameter
from data.use_cases.routine.list_routines.use_case import ListRoutinesUseCase
from data.use_cases.routine.update_routine.use_case import UpdateRoutineUseCase
from data.parameters.routine.update_routine.parameter import (
    UpdateRoutineItemParameter,
    UpdateRoutineParameter,
)
from datetime import time
from typing import Dict
from uuid import UUID

routine_bp = Blueprint("routine_bp", __name__)


@routine_bp.route("/routines", methods=["POST"])
def create_routine():
    event: Dict = request.json

    routine_items_list = []
    for routine_item in event.get("routine_items_list"):
        day_time: str = routine_item["day_time"]
        hour = int(day_time.split(":")[0])
        minute = int(day_time.split(":")[1])

        routine_items_list.append(
            CrateRoutineItemParameter(
                medicine_id=routine_item["medicine_id"],
                medicine_quantity=routine_item["medicine_quantity"],
                week_day=routine_item["week_day"],
                day_time=time(hour=hour, minute=minute),
            )
        )

    use_case = CreateRoutineUseCase()
    parameter = CreateRoutineParameter(
        patient_id=event.get("patient_id"),
        routine_items_list=routine_items_list,
    )
    response = use_case.execute(parameter=parameter)
    return jsonify(response), 201


@routine_bp.route("/routines/<uuid:routine_id>", methods=["DELETE"])
def delete_routine(routine_id: UUID):
    use_case = DeleteRoutineUseCase()
    parameter = DeleteRoutineParameter(routine_id=str(routine_id))
    response = use_case.execute(parameter=parameter)
    return jsonify(response), 200


@routine_bp.route("/list_routines", methods=["GET"])
def list_routines():
    use_case = ListRoutinesUseCase()
    response = use_case.execute()
    return jsonify(response), 200


@routine_bp.route("/routines/<uuid:routine_id>", methods=["PUT"])
def update_routine(routine_id: UUID):
    event: Dict = request.json

    routine_items_list = []
    for routine_item in event.get("routine_items_list"):
        day_time: str = routine_item["day_time"]
        hour = int(day_time.split(":")[0])
        minute = int(day_time.split(":")[1])

        routine_items_list.append(
            UpdateRoutineItemParameter(
                medicine_id=routine_item["medicine_id"],
                medicine_quantity=routine_item["medicine_quantity"],
                week_day=routine_item["week_day"],
                day_time=time(hour=hour, minute=minute),
            )
        )

    use_case = UpdateRoutineUseCase()
    parameter = UpdateRoutineParameter(
        patient_id=event.get("patient_id"),
        routine_id=str(routine_id),
        routine_items_list=routine_items_list,
    )
    response = use_case.execute(parameter=parameter)
    return jsonify(response), 200
