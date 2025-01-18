from data.parameters.routine.delete_routine_items import DeleteRoutineItemsParameter
from infra.repo.routine_repository.repository import RoutineRepository
from typing import Dict


class DeleteRoutineItemsUseCase:
    def __init__(self) -> None:
        self.__routine_repository = RoutineRepository()

    def execute(self, parameter: DeleteRoutineItemsParameter) -> Dict:
        routine_items_ids_list = parameter.routine_items_ids_list

        deleted_routine_items_list = []
        for routine_item_id in routine_items_ids_list:
            deleted_routine_item = self.__routine_repository.delete_routine_item(
                id=routine_item_id
            )
            deleted_routine_items_list.append(deleted_routine_item._asdict())

        return {"success": True, "data": deleted_routine_items_list}
