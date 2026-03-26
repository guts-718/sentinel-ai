class NLPExtractor:
    def __init__(self):
        self.keywords = {
            "cone": ["cone", "cones"],
            "tape": ["tape", "caution tape"],
            "barricade": ["barricade", "barrier", "fence"]
        }

    def extract(self, caption):
        caption = caption.lower()

        found = []

        for key, variants in self.keywords.items():
            for v in variants:
                if v in caption:
                    found.append(key)
                    break

        return {
            "safety_measures": list(set(found)),
            "has_safety": len(found) > 0,
            "raw_caption": caption
        }