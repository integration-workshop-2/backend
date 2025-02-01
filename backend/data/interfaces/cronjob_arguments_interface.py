from abc import ABC, abstractmethod
from domain.models.cronjob_model import CronJobModel


class CronJobArgumentsInterface(ABC):
    @abstractmethod
    def create_cronjob(cls, execution_pattern: str, argument: str) -> CronJobModel:
        raise Exception("Method not implemented")

    @abstractmethod
    def delete_cronjob(cls, execution_pattern: str) -> CronJobModel:
        raise Exception("Method not implemented")

    @abstractmethod
    def get_cronjob(cls, execution_pattern: str) -> CronJobModel:
        raise Exception("Method not implemented")

    @abstractmethod
    def update_cronjob(cls, execution_pattern: str, argument: str) -> CronJobModel:
        raise Exception("Method not implemented")
