from flask import Flask, request

index = 0

app = Flask(__name__)


@app.route("/upload", methods=["POST"])
def upload_image():
    global index

    raw_data = request.data

    with open("received_images/uploaded_image" + str(index) + ".jpg", "wb") as f:
        f.write(raw_data)

    index += 1

    return "Image uploaded and saved successfully", 200


if __name__ == "__main__":
    app.run(host="10.42.0.1", port=5000)
