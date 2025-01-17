from abc import ABC, abstractmethod
from datetime import datetime
from domain.models.routine_model import RoutineDataModel, RoutineModel
from typing import List, Literal


class RoutineInterface(ABC):
    @abstractmethod
    def create_routine(
        cls,
        patient_id: str,
        medicine_id: str,
        medicine_quantity: int,
        week_day: Literal[
            "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
        ],
        day_time: datetime,
    ) -> RoutineModel:
        raise Exception("Method not implemented")

    @abstractmethod
    def delete_routine(cld, id: str) -> RoutineModel:
        raise Exception("Method not implemented")

    @abstractmethod
    def get_routine(cls, id: str) -> RoutineModel:
        raise Exception("Method not implemented")

    @abstractmethod
    def list_routines(
        cls, patient_name: str = "", routine_description: str = ""
    ) -> List[RoutineDataModel]:
        raise Exception("Method not implemented")

    @abstractmethod
    def update_routine(
        cls,
        id: str,
        medicine_id: str,
        medicine_quantity: int,
        week_day: Literal[
            "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
        ],
        day_time: datetime,
    ) -> RoutineModel:
        raise Exception("Method not implemented")
