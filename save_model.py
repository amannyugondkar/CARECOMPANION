import pickle
from medical_keyword_extractor import MedicalKeywordExtractor  # Correct import

# Initialize the extractor
keyword_processor = MedicalKeywordExtractor()

# Save it as a pickle file
with open("medical_keyword_extractor.pkl", "wb") as f:
    pickle.dump(keyword_processor, f)

print("Model saved successfully!")
