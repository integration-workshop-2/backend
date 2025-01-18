from data.parameters.admin_password.validate_admin_password import (
    ValidateAdminPasswordParameter,
)
from infra.repo.admin_password_repository.repository import AdminPasswordRepository
from typing import Dict


class ValidateAdminPasswordUseCase:
    def __init__(self) -> None:
        self.__admin_password_repository = AdminPasswordRepository()

    def execute(self, parameter: ValidateAdminPasswordParameter) -> Dict:
        stored_password = self.__admin_password_repository.get_admin_password().password

        if parameter.password == stored_password:
            return {"success": True}

        return {"success": False}
