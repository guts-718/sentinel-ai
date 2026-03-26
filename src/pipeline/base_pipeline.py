import os
import json
from datetime import datetime
from src.models.yolo_detector import YOLODetector

class BasePipeline:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.detector = YOLODetector()

    def process_image(self, image_path):
        self.logger.info(f"Processing image: {image_path}")

        detections = self.detector.detect(image_path)
        self.logger.info(f"Detections: {detections}")

        result = {
            "image_id": image_path.split("/")[-1],
            "timestamp": datetime.utcnow().isoformat(),
            "status": "processed",
            "detections": detections,
            "ppe_compliance": None,
            "severity": None
        }

        return result

    def save_output(self, result):
        output_dir = self.config["paths"]["output_dir"]
        os.makedirs(output_dir, exist_ok=True)

        filename = os.path.basename(result["image_id"])
        output_path = os.path.join(output_dir, filename + ".json")

        print(f"Saving output to {output_path}...")
        with open(output_path, "w") as f:
            json.dump(result, f, indent=2)