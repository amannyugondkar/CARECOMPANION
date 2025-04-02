import spacy
import re
from typing import List, Tuple
from sklearn.feature_extraction.text import TfidfVectorizer

class MedicalKeywordExtractor:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        
    def preprocess_text(self, text: str) -> str:
        text = text.lower()
        text = re.sub(r'[^\w\s]', ' ', text)
        return ' '.join(text.split())

    def extract_keywords(self, text: str, top_n: int = 10) -> List[Tuple[str, float]]:
        text = self.preprocess_text(text)
        vectorizer = TfidfVectorizer(max_features=100)
        tfidf_matrix = vectorizer.fit_transform([text])
        feature_names = vectorizer.get_feature_names_out()
        tfidf_scores = tfidf_matrix.toarray()[0]

        keywords = {word: score for word, score in zip(feature_names, tfidf_scores) if score > 0}
        sorted_keywords = sorted(keywords.items(), key=lambda x: x[1], reverse=True)
        return sorted_keywords[:top_n]
