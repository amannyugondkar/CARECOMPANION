import pickle
import pathlib
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from medical_keyword_extractor import MedicalKeywordExtractor  # Correct import

# Fix for Windows compatibility
pathlib.PosixPath = pathlib.WindowsPath

app = Flask(__name__)
CORS(app)
# Load the saved model
with open("medical_keyword_extractor.pkl", "rb") as f:
    keyword_processor = pickle.load(f)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Medical Keyword Extractor API is running!"})

@app.route("/extract_keywords", methods=["POST"])
def extract_keywords():
    data = request.get_json()
    if "text" not in data:
        return jsonify({"error": "No text provided"}), 400

    text = data["text"]
    keywords = keyword_processor.extract_keywords(text)
    return jsonify({"keywords": keywords})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
