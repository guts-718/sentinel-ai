from ultralytics import YOLO

class YOLODetector:
    def __init__(self, model_path="yolov8n.pt"):
        self.model = YOLO(model_path)

    def detect(self, image_path):
        results = self.model(image_path)

        detections = []

        for r in results:
            for box in r.boxes:
                cls_id = int(box.cls[0])
                conf = float(box.conf[0])
                label = self.model.names[cls_id]
                xyxy = box.xyxy[0].tolist()

                detections.append({
                    "class": label,
                    "confidence": conf,
                    "bbox": xyxy
                })

        return detections