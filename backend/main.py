from data.use_cases.admin_password.update_admin_password import (
    UpdateAdminPasswordUseCase,
)
from data.parameters.admin_password.update_admin_password import (
    UpdateAdminPasswordParameter,
)

if __name__ == "__main__":
    use_case = UpdateAdminPasswordUseCase()
    parameter = UpdateAdminPasswordParameter(password="4321")
    print(use_case.execute(parameter=parameter))
