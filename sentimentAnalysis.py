import os
import json
import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Ensure VADER is available
nltk.download('vader_lexicon')

# Initialize sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    scores = analyzer.polarity_scores(text)
    return scores["pos"], scores["neg"], scores["compound"]

def process_json_files(input_folder, output_csv):
    results = []
    
    for filename in os.listdir(input_folder):
        if filename.endswith(".json"):
            file_path = os.path.join(input_folder, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                for entry in data:
                    date = entry["date"]
                    submissions = entry["submissions"]
                    
                    pos_scores, neg_scores, comp_scores = [], [], []
                    for submission in submissions:
                        pos, neg, comp = analyze_sentiment(submission)
                        pos_scores.append(pos)
                        neg_scores.append(neg)
                        comp_scores.append(comp)
                    
                    results.append({
                        "date": date,
                        "positive": sum(pos_scores) / len(pos_scores) if pos_scores else 0,
                        "negative": sum(neg_scores) / len(neg_scores) if neg_scores else 0,
                        "compound": sum(comp_scores) / len(comp_scores) if comp_scores else 0,
                    })
    
    # Convert results to DataFrame and save as CSV
    df = pd.DataFrame(results)
    df.to_csv(output_csv, index=False)

# Define input folder and output CSV path
input_folder = "input"  # Change this to your actual folder path
output_csv = "sentiment_analysis.csv"

process_json_files(input_folder, output_csv)
print(f"Sentiment analysis saved to {output_csv}")
