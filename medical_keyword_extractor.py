import spacy
import pickle
import re
from collections import Counter
from typing import List, Dict, Tuple
from sklearn.feature_extraction.text import TfidfVectorizer
from typing import List, Tuple
# Load the SpaCy model
nlp = spacy.load("en_core_web_sm")

class MedicalKeywordExtractor:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.medical_terms = {
            "symptoms": ["pain", "fever", "headache", "nausea", "vomiting", "fatigue", "cough", "shortness of breath"],
            "conditions": ["diabetes", "hypertension", "asthma", "arthritis", "cancer", "infection", "inflammation"],
            "medications": ["antibiotics", "insulin", "antidepressants", "painkillers", "steroids"],
            "procedures": ["surgery", "biopsy", "x-ray", "mri", "ct scan", "blood test"],
            "body_parts": ["heart", "lungs", "brain", "liver", "kidneys", "stomach", "bones"],
            "measurements": ["blood pressure", "temperature", "heart rate", "weight", "height"]
        }

    def preprocess_text(self, text: str) -> str:
        text = text.lower()
        text = re.sub(r"[^\w\s]", " ", text)
        return " ".join(text.split())

    def extract_keywords(self, text: str, top_n: int = 10)-> List[Tuple[str, float]]:
        text = self.preprocess_text(text)


        vectorizer = TfidfVectorizer(
            max_features=100,
            stop_words="english"
            )
        
        tfidf_matrix = vectorizer.fit_transform([text])
        feature_names = vectorizer.get_feature_names_out()
        tfidf_scores = tfidf_matrix.toarray()[0]

        keywords = [(word, score) for word, score in zip(feature_names, tfidf_scores) if score > 0]
        sorted_keywords = sorted(keywords, key=lambda x: x[1], reverse=True)
        return sorted_keywords[:top_n]
