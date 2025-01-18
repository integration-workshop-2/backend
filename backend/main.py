from data.use_cases.admin_password.validate_admin_password import (
    ValidateAdminPasswordUseCase,
)
from data.parameters.admin_password.validate_admin_password import (
    ValidateAdminPasswordParameter,
)

if __name__ == "__main__":
    use_case = ValidateAdminPasswordUseCase()
    parameter = ValidateAdminPasswordParameter(password="4321")
    print(use_case.execute(parameter=parameter))
