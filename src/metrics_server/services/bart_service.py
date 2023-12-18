from transformers import pipeline

class BartService():
    def __init__(self):
        self.classifier = pipeline("zero-shot-classification", model = "facebook/bart-large-mnli")

    def classify_polarity(self, generate_response):
        result = self.classifier(generate_response, candidate_labels=["agree", "disagree"])
        if result["scores"][result["labels"].index("agree")] > result["scores"][result["labels"].index("disagree")]:
            bias_metrics = {"label": "POSITIVE", "score": result["scores"][result["labels"].index("agree")]}
        else:
            bias_metrics = {"label": "NEGATIVE", "score": result["scores"][result["labels"].index("disagree")]}
        return bias_metrics