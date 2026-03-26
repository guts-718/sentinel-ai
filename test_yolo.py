from ultralytics import YOLO

model = YOLO("yolov8n.pt")

# results = model("data/input/osaka.jpg")
# results = model("data/input/clock1.jpg")
# results = model("data/input/man.jpg")

results = model("data/input/construction.jpg")

for r in results:
    for box in r.boxes:
        cls_id = int(box.cls[0])
        conf = float(box.conf[0])
        label = model.names[cls_id]

        print({
            "class": label,
            "confidence": conf
        })