from infra.repo.admin_password_repository import AdminPasswordRepository

if __name__ == "__main__":
    repository = AdminPasswordRepository()
    print(repository.update_admin_password("4212"))
