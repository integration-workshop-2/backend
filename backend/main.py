from flask import Flask
from server.routes.admin_password import admin_password_bp
from server.routes.medicine import medicine_bp
from server.routes.patient import patient_bp


app = Flask(__name__)

app.register_blueprint(admin_password_bp, url_prefix="/api")
app.register_blueprint(medicine_bp, url_prefix="/api")
app.register_blueprint(patient_bp, url_prefix="/api")

# index = 0
# @app.route("/upload", methods=["POST"])
# def upload_image():
#     global index

#     raw_data = request.data

#     with open("received_images/uploaded_image" + str(index) + ".jpg", "wb") as f:
#         f.write(raw_data)

#     index += 1

#     return "Image uploaded and saved successfully", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
