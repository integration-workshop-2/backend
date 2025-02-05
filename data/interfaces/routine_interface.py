from abc import ABC, abstractmethod
from domain.models.routine_model import RoutineModel


class RoutineInterface(ABC):
    @abstractmethod
    def create_routine(cls, patient_id: str) -> RoutineModel:
        raise Exception("Method not implemented")

    @abstractmethod
    def delete_routine(cls, id: str) -> RoutineModel:
        raise Exception("Method not implemented")

    @abstractmethod
    def get_routine(cls, id: str) -> RoutineModel:
        raise Exception("Method not implemented")
