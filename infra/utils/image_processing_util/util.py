from deepface import DeepFace
from numpy import ndarray
from pathlib import Path
from scipy.spatial.distance import cosine
from typing import List


class ImageProcessingUtil:
    def __init__(self) -> None:
        self.__posted_images_folder = (
            Path(__file__).resolve().parent.parent.parent.parent
            / "image_data"
            / "posted_images"
        )
        self.__posted_images_folder.mkdir(parents=True, exist_ok=True)

    def get_face_embeddings(self) -> List[List[float]]:
        images_list = list(self.__posted_images_folder.glob("*.jpg"))

        face_embeddings_list = []

        for image in images_list:
            try:
                face_embeddings_data = DeepFace.represent(img_path=image)

                if len(face_embeddings_data) == 1:
                    face_embeddings_list.append(face_embeddings_data[0]["embedding"])

            except:
                pass

        return face_embeddings_list

    def compare_face_embeddings(
        self, face_embeddings_list_1: List[float], face_embeddings_list_2: List[float]
    ) -> bool:
        threshold = 0.35

        similarity_score = cosine(face_embeddings_list_1, face_embeddings_list_2)

        if similarity_score < threshold:
            return True
        else:
            return False

    def clear_posted_images_folder(self) -> None:
        for file in self.__posted_images_folder.iterdir():
            file.unlink()
