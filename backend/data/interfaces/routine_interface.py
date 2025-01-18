from abc import ABC, abstractmethod
from datetime import datetime, time
from domain.models.routine_item_model import RoutineItemModel
from domain.models.routine_model import RoutineDataModel, RoutineModel
from typing import List, Literal


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
