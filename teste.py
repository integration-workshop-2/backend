from deepface import DeepFace
from scipy.spatial.distance import cosine

# embedding_objs1 = DeepFace.represent(
#     img_path="image_data/posted_images/f6e511f8-f542-4c18-a7b8-0c4bda7e03f1.jpg"
# )

# embedding_objs2 = DeepFace.represent(
#     img_path="image_data/posted_images/6ddd9e75-cbbe-4b36-9cc6-6e261e76cd95.jpg"
# )

# similarity_score = cosine(
#     embedding_objs1[0]["embedding"], embedding_objs2[0]["embedding"]
# )

# threshold = 0.6

# print(similarity_score)

# if similarity_score < threshold:
#     print("igual")
# else:
#     print("errado")


embedding_objs = DeepFace.represent(
    img_path="image_data/posted_images/0ffeb076-86b6-4210-9cff-89400d9121e3.jpg"
)

print(embedding_objs)

print(len(embedding_objs))
