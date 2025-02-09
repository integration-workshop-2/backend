from flask import Blueprint, request, jsonify
from data.use_cases.admin_password.update_admin_password.use_case import (
    UpdateAdminPasswordUseCase,
)
from data.parameters.admin_password.update_admin_password.parameter import (
    UpdateAdminPasswordParameter,
)
from data.use_cases.admin_password.validate_admin_password.use_case import (
    ValidateAdminPasswordUseCase,
)
from data.parameters.admin_password.validate_admin_password.parameter import (
    ValidateAdminPasswordParameter,
)
from typing import Dict

admin_password_bp = Blueprint("admin_password_bp", __name__)


@admin_password_bp.route("/admin_password", methods=["PUT"])
def update_admin_password():
    event: Dict = request.json
    use_case = UpdateAdminPasswordUseCase()
    parameter = UpdateAdminPasswordParameter(password=event.get("password"))
    response = use_case.execute(parameter=parameter)
    return jsonify(response), 200


@admin_password_bp.route("/validate_admin_password", methods=["POST"])
def validate_admin_password():
    event: Dict = request.json
    use_case = ValidateAdminPasswordUseCase()
    parameter = ValidateAdminPasswordParameter(password=event.get("password"))
    response = use_case.execute(parameter=parameter)

    if response.get("success"):
        status = 200
    else:
        status = 403

    return jsonify(response), status
