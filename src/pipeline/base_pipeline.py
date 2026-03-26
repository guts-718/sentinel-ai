import os
import json
from datetime import datetime
from src.models.yolo_detector import YOLODetector
from src.pipeline.ppe_logic import PPELogic
from src.models.vlm_captioner import VLMCaptioner

class BasePipeline:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.detector = YOLODetector()
        self.ppe_logic = PPELogic()
        self.vlm = VLMCaptioner()

    def process_image(self, image_path):
        self.logger.info(f"Processing image: {image_path}")

        detections = self.detector.detect(image_path)
        self.logger.info(f"Detections: {detections}")

        ppe_result = self.ppe_logic.evaluate(detections)
        self.logger.info(f"PPE result: {ppe_result}")
        
        caption = self.vlm.generate_caption(image_path)
        self.logger.info(f"Caption: {caption}")

        result = {
            "image_id": image_path.split("/")[-1],
            "timestamp": datetime.utcnow().isoformat(),
            "status": "processed",
            "detections": detections,
            "ppe_compliance": ppe_result,
            "severity": None,
            "caption": caption,
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