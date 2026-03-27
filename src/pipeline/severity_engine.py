class SeverityEngine:
    def __init__(self):
        pass

    def detect_lighting(self, caption):
        caption = caption.lower()

        if any(word in caption for word in ["night", "dark", "dim"]):
            return "dark"
        return "bright"

    def evaluate(self, caption, nlp_result, ppe_result):
        lighting = self.detect_lighting(caption)
        has_safety = nlp_result["has_safety"]

        if ppe_result["status"] == "no_worker":
            return {
                "severity": "none",
                "lighting": lighting,
                "has_safety": has_safety
            }

        if lighting == "bright" and has_safety:
            severity = "minimal"
        elif lighting == "dark" and has_safety:
            severity = "low"
        elif lighting == "bright" and not has_safety:
            severity = "high"
        else:
            severity = "critical"

        return {
            "severity": severity,
            "lighting": lighting,
            "has_safety": has_safety
        }