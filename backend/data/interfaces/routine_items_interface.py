from abc import ABC, abstractmethod
from datetime import time
from domain.models.routine_item_model import RoutineItemDataModel, RoutineItemModel
from typing import List, Literal


class RoutineItemsInterface(ABC):
    @abstractmethod
    def create_routine_item(
        cls,
        routine_id: str,
        medicine_id: str,
        medicine_quantity: int,
        week_day: Literal[
            "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
        ],
        day_time: time,
    ) -> RoutineItemModel:
        raise Exception("Method not implemented")

    @abstractmethod
    def get_routine_item(cls, id: str) -> RoutineItemModel:
        raise Exception("Method not implemented")

    @abstractmethod
    def list_routine_items(
        cls,
        patient_name: str = "",
        routine_description: str = "",
    ) -> List[RoutineItemDataModel]:
        raise Exception("Method not implemented")
