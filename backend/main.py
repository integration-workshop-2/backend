from flask import Flask
from flask_cors import CORS

from server.routes.admin_password import admin_password_bp
from server.routes.alarms import alarms_bp
from server.routes.images import images_bp
from server.routes.medicine import medicine_bp
from server.routes.non_recognized_patients import non_recognized_patients_bp
from server.routes.patient import patient_bp
from server.routes.patients_vital_signs import patients_vital_signs_bp
from server.routes.routine import routine_bp

# from server.routes.vital_signs_sensors import vital_signs_sensors_bp


app = Flask(__name__)
CORS(app, origins="*")

app.register_blueprint(blueprint=admin_password_bp, url_prefix="/api")
app.register_blueprint(blueprint=alarms_bp, url_prefix="/api")
app.register_blueprint(blueprint=images_bp, url_prefix="/api")
app.register_blueprint(blueprint=medicine_bp, url_prefix="/api")
app.register_blueprint(blueprint=non_recognized_patients_bp, url_prefix="/api")
app.register_blueprint(blueprint=patient_bp, url_prefix="/api")
app.register_blueprint(blueprint=patients_vital_signs_bp, url_prefix="/api")
app.register_blueprint(blueprint=routine_bp, url_prefix="/api")
# app.register_blueprint(blueprint=vital_signs_sensors_bp, url_prefix="/api")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
