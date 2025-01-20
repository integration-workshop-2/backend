# importing the cv2 library
import cv2

# loading the haar case algorithm file into alg variable
alg = "haarcascade_frontalface_default.xml"
# passing the algorithm to OpenCV
haar_cascade = cv2.CascadeClassifier(alg)
# loading the image path into file_name variable - replace <INSERT YOUR IMAGE NAME HERE> with the path to your image
file_name = "i4.jpg"
# reading the image
img = cv2.imread(file_name, 0)
# creating a black and white version of the image
gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
# detecting the faces
faces = haar_cascade.detectMultiScale(
    gray_img, scaleFactor=1.3, minNeighbors=1, minSize=(100, 100)
)

i = 0
# for each face detected
for x, y, w, h in faces:
    # crop the image to select only the face
    cropped_image = img[y : y + h, x : x + w]
    # loading the target image path into target_file_name variable  - replace <INSERT YOUR TARGET IMAGE NAME HERE> with the path to your target image
    target_file_name = "stored-faces/" + str(i) + ".jpg"
    cv2.imwrite(
        target_file_name,
        cropped_image,
    )
    i = i + 1


#######################
import os
from PIL import Image
from imgbeddings import imgbeddings


saved_info = []
for filename in os.listdir("stored-faces"):
    # opening the image
    img = Image.open("stored-faces/" + filename)
    # loading the `imgbeddings`
    ibed = imgbeddings()
    # calculating the embeddings
    embedding = ibed.to_embeddings(img)
    saved_info.append(embedding[0].tolist())


# loading the face image path into file_name variable
file_name = "i2.jpg"  # replace <INSERT YOUR FACE FILE NAME> with the path to your image
# opening the image
img = Image.open(file_name)
# loading the `imgbeddings`
ibed = imgbeddings()
# calculating the embeddings
embedding = ibed.to_embeddings(img)


from scipy.spatial.distance import cosine

# Example: Compare the extracted embeddings
threshold = 0.2  # Adjust based on your needs (lower means stricter match)

similarity_score = cosine(saved_info[0], embedding[0])

if similarity_score < threshold:
    print("Same person (Similarity Score:", similarity_score, ")")
else:
    print("Different people (Similarity Score:", similarity_score, ")")
