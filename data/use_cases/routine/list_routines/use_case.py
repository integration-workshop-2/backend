from data.parameters.routine.list_routines.parameter import ListRoutinesParameter
from datetime import datetime, time
from domain.models.routine_item_model import RoutineItemDataModel
from infra.repo.routine_items_repository.repository import RoutineItemsRepository
from typing import Dict, List, Tuple, TypedDict


class ListRoutinesUseCase:
    def __init__(self) -> None:
        self.__routine_items_repository = RoutineItemsRepository()

    def execute(self, parameter: ListRoutinesParameter) -> Dict:
        routine_items_data_list = self.__routine_items_repository.list_routine_items(
            patient_name=parameter.patient_name,
            routine_description=parameter.routine_description,
        )

        return {
            "sucess": True,
            "data": self.__group_routine_items(
                routine_items_data_list=routine_items_data_list
            ),
        }

    def __group_routine_items(
        self, routine_items_data_list: List[RoutineItemDataModel]
    ) -> Dict:

        class PatientRoutineData(TypedDict):
            patient_name: str
            routine_id: str
            routine_descriptions: List[str]

        patients_routine_descriptions_dict: Dict[str, PatientRoutineData] = {}

        for routine_item_data in routine_items_data_list:
            if not patients_routine_descriptions_dict.get(routine_item_data.patient_id):
                patients_routine_descriptions_dict[routine_item_data.patient_id] = {
                    "patient_name": routine_item_data.patient_name,
                    "routine_id": routine_item_data.routine_id,
                    "routine_descriptions": [routine_item_data.routine_description],
                }
            else:
                patients_routine_descriptions_dict[routine_item_data.patient_id].get(
                    "routine_descriptions"
                ).append(routine_item_data.routine_description)

        result: List[Dict] = []
        for (
            patient_id,
            patient_routine_data,
        ) in patients_routine_descriptions_dict.items():
            result.append(
                {
                    "patient_id": patient_id,
                    "patient_name": patient_routine_data["patient_name"],
                    "routine_id": patient_routine_data["routine_id"],
                    "routine_descriptions": self.__sort_routine_descriptions(
                        patient_routine_data["routine_descriptions"]
                    ),
                }
            )

        return result

    def __sort_routine_descriptions(self, routine_descriptions) -> Tuple[int, time]:
        def __sort_key(entry: str):
            week_order = {
                "Seg": 0,
                "Ter": 1,
                "Qua": 2,
                "Qui": 3,
                "Sex": 4,
                "Sáb": 5,
                "Dom": 6,
            }
            parts = entry.split(" ", 2)
            weekday = week_order[parts[0]]
            time = datetime.strptime(parts[1], "%H:%M").time()
            return (weekday, time)

        return sorted(routine_descriptions, key=__sort_key)
