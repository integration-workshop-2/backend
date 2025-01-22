import cv2
from imgbeddings import imgbeddings
from numpy import ndarray
from os import environ
from pathlib import Path
from PIL import Image
from typing import List


environ["TF_ENABLE_ONEDNN_OPTS"] = "0"


class ImageProcessingUtil:
    def get_face_embeddings(self) -> List[List[float]]:
        haarcascade_frontalface_model_path = (
            Path(__file__).resolve().parent.parent.parent.parent
            / "ml_models"
            / "haarcascade_frontalface_default.xml"
        )
        haar_cascade = cv2.CascadeClassifier(haarcascade_frontalface_model_path)

        posted_images_folder = (
            Path(__file__).resolve().parent.parent.parent.parent.parent
            / "image_data"
            / "posted_images"
        )
        posted_images_folder.mkdir(parents=True, exist_ok=True)

        images_list = list(posted_images_folder.glob("*.jpg"))
        detected_faces_list = []
        for image in images_list:
            img = cv2.imread(image, 0)
            gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            detected_face = haar_cascade.detectMultiScale(
                gray_img, scaleFactor=1.3, minNeighbors=1, minSize=(100, 100)
            )
            detected_faces_list.append(detected_face)

        detected_faces_folder = (
            Path(__file__).resolve().parent.parent.parent.parent.parent
            / "image_data"
            / "detected_faces"
        )
        detected_faces_folder.mkdir(parents=True, exist_ok=True)

        i = 1
        for detected_face in detected_faces_list:
            for x, y, w, h in detected_face:
                cropped_image = img[y : y + h, x : x + w]
                img_path = "img" + str(i) + ".jpg"
                cv2.imwrite(
                    str(detected_faces_folder / img_path),
                    cropped_image,
                )
                i += 1

        face_embeddings_list = []
        ibed = imgbeddings()
        saved_detected_faces_list = list(detected_faces_folder.glob("*.jpg"))
        for filename in saved_detected_faces_list:
            img = Image.open(filename)
            embedding = ibed.to_embeddings(img)
            embedding_values: ndarray = embedding[0]
            face_embeddings_list.append(embedding_values.tolist())

        return face_embeddings_list
