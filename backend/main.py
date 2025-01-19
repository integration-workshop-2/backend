from flask import Flask
from server.routes.admin_password import admin_password_bp
from server.routes.alarms import alarms_bp
from server.routes.medicine import medicine_bp
from server.routes.non_recognized_patients import non_recognized_patients_bp
from server.routes.patient import patient_bp
from server.routes.patients_vital_signs import patients_vital_signs_bp


app = Flask(__name__)

app.register_blueprint(blueprint=admin_password_bp, url_prefix="/api")
app.register_blueprint(blueprint=alarms_bp, url_prefix="/api")
app.register_blueprint(blueprint=medicine_bp, url_prefix="/api")
app.register_blueprint(blueprint=non_recognized_patients_bp, url_prefix="/api")
app.register_blueprint(blueprint=patient_bp, url_prefix="/api")
app.register_blueprint(blueprint=patients_vital_signs_bp, url_prefix="/api")

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
