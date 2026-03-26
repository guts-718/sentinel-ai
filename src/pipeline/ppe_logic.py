class PPELogic:
    def evaluate(self, detections):
        person_count = sum(1 for d in detections if d["class"] == "person")

        if person_count == 0:
            return {
                "status": "no_worker",
                "person_count": 0
            }

        return {
            "status": "unknown",
            "person_count": person_count
        }