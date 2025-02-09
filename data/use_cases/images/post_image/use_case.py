from data.parameters.images.post_image.parameter import PostImageParameter
from pathlib import Path
from typing import Dict
from uuid import uuid4


class PostImageUseCase:
    def execute(self, parameter: PostImageParameter) -> Dict:
        posted_images_folder = (
            Path(__file__).resolve().parent.parent.parent.parent.parent
            / "image_data"
            / "posted_images"
        )
        posted_images_folder.mkdir(parents=True, exist_ok=True)
        image_path = posted_images_folder / f"{str(uuid4())}.jpg"

        with image_path.open(mode="wb") as f:
            f.write(parameter.data)

        return {"success": True, "data": str(image_path)}
