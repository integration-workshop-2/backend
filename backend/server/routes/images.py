from flask import Blueprint, request, jsonify
from data.use_cases.images.post_image.use_case import PostImageUseCase
from data.parameters.images.post_image.parameter import PostImageParameter
from data.use_cases.images.recognize_image.use_case import RecognizeImageUseCase
from data.parameters.images.recognize_image.parameter import RecognizeImageParameter
from uuid import UUID

images_bp = Blueprint("images_bp", __name__)


@images_bp.route("/images", methods=["POST"])
def post_image():
    """Frontend will request ESP32 for an image, then,
    the microcontroller will send the raw data to this endpoint.
    Finally, RPI will save the image in a folder"""

    event: bytes = request.data
    use_case = PostImageUseCase()
    parameter = PostImageParameter(data=event)
    response = use_case.execute(parameter=parameter)
    return jsonify(response), 200


@images_bp.route("/recognize_images/<uuid:patient_id>", methods=["GET"])
def recognize_images(patient_id: UUID):
    use_case = RecognizeImageUseCase()
    parameter = RecognizeImageParameter(patient_id=str(patient_id))
    response = use_case.execute(parameter=parameter)

    if response.get("success"):
        return jsonify(response), 200

    return jsonify(response), 403
