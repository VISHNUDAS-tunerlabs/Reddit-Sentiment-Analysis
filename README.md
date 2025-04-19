# 🛉 Reddit Data Cleanup & Sentiment Analysis

Welcome to the **Reddit Data Cleanup & Sentiment Analysis** repository!  
This tool helps you analyze the sentiment of Reddit submissions provided in JSON format and outputs a single CSV file summarizing the results — all with a beginner-friendly setup.

---

## 📁 Repository Structure

```
Reddit-Sentiment-Analysis/
├── input/                      # Folder containing input .json files (sample files included)
│   ├── sample1.json
│   └── sample2.json
├── sentimentAnalysis.py       # Python script to perform sentiment analysis
├── output.csv                 # Output CSV (auto-generated after running the script)
└── README.md                  # This file
```

---

## 🔧 Features

- Accepts `.json` files of Reddit submissions placed inside the `input/` folder.
- Performs sentiment analysis using **NLTK's SentimentIntensityAnalyzer**.
- Outputs a single `output.csv` summarizing sentiment scores per day.

---

## 🚀 Getting Started

No prior experience? No worries — follow these steps to set up everything from scratch!

### 1. Clone the Repository

```bash
git clone https://github.com/VISHNUDAS-tunerlabs/Reddit-Sentiment-Analysis
cd reddit-data-cleanup
```

### 2. Set Up a Virtual Environment

It's recommended to use a virtual environment to manage dependencies:

```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> If there's no `requirements.txt`, just run:

```bash
pip install nltk pandas
```

And don't forget to download NLTK resources:

```python
# Run this in a Python shell
import nltk
nltk.download('vader_lexicon')
```

---

## ▶️ Running the Script

Once everything is set up, simply run:

```bash
python sentimentAnalysis.py
```

This will:

- Read all `.json` files in the `input/` folder.
- Perform sentiment analysis on each submission.
- Generate a single `output.csv` file in the root directory.

---

## 📂 Sample Data

We've included a couple of sample `.json` files inside the `input/` folder so you can test the script right away.

---

## 📌 Notes

- Make sure your `.json` files contain a top-level field named `submissions`, where each item has a `created_utc` timestamp and `body` or `text` for sentiment analysis.
- The script assumes the timestamp is in UNIX format and converts it to daily aggregation.

---

## 🤝 Contributing

Feel free to fork the repo and contribute via pull requests. Suggestions and improvements are always welcome!

---

## 📬 Contact

Have questions or need help? Open an issue or reach out!
