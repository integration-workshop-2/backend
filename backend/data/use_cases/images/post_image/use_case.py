from data.parameters.images.post_image.parameter import PostImageParameter
from pathlib import Path
from time import time
from typing import Dict


class PostImageUseCase:
    def execute(self, parameter: PostImageParameter) -> Dict:
        timestamp = str(int(time()))

        posted_images_folder = (
            Path(__file__).resolve().parent.parent.parent.parent.parent
            / "image_data"
            / "posted_images"
        )
        posted_images_folder.mkdir(parents=True, exist_ok=True)
        image_path = posted_images_folder / f"posted_image_{timestamp}.jpg"

        with image_path.open(mode="wb") as f:
            f.write(parameter.data)

        return {"success": True, "data": str(image_path)}
