from abc import ABC, abstractmethod
from domain.models.alarms_model import AlarmsModel
from typing import List


class AlarmsInterface(ABC):
    @abstractmethod
    def create_alarm(cls, patient_vital_signs_id: str) -> AlarmsModel:
        raise Exception("Method not implemented")

    @abstractmethod
    def list_alarms(cls) -> List[AlarmsModel]:
        raise Exception("Method not implemented")
