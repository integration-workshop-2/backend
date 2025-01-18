from data.parameters.admin_password.update_admin_password import (
    UpdateAdminPasswordParameter,
)
from infra.repo.admin_password_repository.repository import AdminPasswordRepository
from typing import Dict


class UpdateAdminPasswordUseCase:
    def __init__(self) -> None:
        self.__admin_password_repository = AdminPasswordRepository()

    def execute(self, parameter: UpdateAdminPasswordParameter) -> Dict:
        response = self.__admin_password_repository.update_admin_password(
            password=parameter.password
        )
        return {"success": True, "data": response._asdict()}
