from deepface import DeepFace

img1_path = ""
img2_path = ""

result = DeepFace.verify(
    img1_path, img2_path, model_name="Facenet", enforce_detection=False
)

print(result)
