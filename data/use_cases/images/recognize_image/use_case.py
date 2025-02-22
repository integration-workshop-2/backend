from data.parameters.images.recognize_image.parameter import RecognizeImageParameter
from infra.repo.patient_faces_repository.repository import PatientFacesRepository
from infra.utils.image_processing_util.util import ImageProcessingUtil
from typing import Dict


class RecognizeImageUseCase:
    def __init__(self) -> None:
        self.__image_processing_util = ImageProcessingUtil()
        self.__patient_faces_repository = PatientFacesRepository()

    def execute(self, parameter: RecognizeImageParameter) -> Dict:
        face_embeddings_list = self.__image_processing_util.get_face_embeddings()

        patient_face_embeddings_list = (
            self.__patient_faces_repository.list_patient_faces_by_patient_id(
                patient_id=parameter.patient_id
            )
        )

        for face_embeddings in face_embeddings_list:
            for patient_face_embeddings in patient_face_embeddings_list:
                if self.__image_processing_util.compare_face_embeddings(
                    face_embeddings_list_1=face_embeddings,
                    face_embeddings_list_2=patient_face_embeddings.face_embedding,
                ):

                    self.__image_processing_util.clear_posted_images_folder()
                    return {"success": True}

        self.__image_processing_util.clear_posted_images_folder()

        return {"success": False}
