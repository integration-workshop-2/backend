from flask import Blueprint, request, jsonify
from data.use_cases.images.post_image.use_case import PostImageUseCase
from data.parameters.images.post_image.parameter import PostImageParameter


images_bp = Blueprint("images_bp", __name__)


@images_bp.route("/images", methods=["POST"])
def post_image():
    event: bytes = request.data
    use_case = PostImageUseCase()
    parameter = PostImageParameter(data=event)
    response = use_case.execute(parameter=parameter)
    return jsonify(response), 200
