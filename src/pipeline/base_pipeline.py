import os
import json
from datetime import datetime

class BasePipeline:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger

    def process_image(self, image_path):
        self.logger.info(f"Processing image: {image_path}")

        result = {
            "image_id": os.path.basename(image_path),
            "timestamp": datetime.utcnow().isoformat(),
            "status": "received",
            "detections": None,
            "ppe_compliance": None,
            "severity": None
        }

        return result

    def save_output(self, result):
        output_dir = self.config["paths"]["output_dir"]
        os.makedirs(output_dir, exist_ok=True)

        output_path = os.path.join(
            output_dir,
            result["image_id"] + ".json"
        )

        with open(output_path, "w") as f:
            json.dump(result, f, indent=2)