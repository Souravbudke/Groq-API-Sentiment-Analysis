from flask import Flask, request, jsonify
import pandas as pd
import os
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

app = Flask("senti")

# Initialize Groq client with the API key
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
@app.route('/analyze', methods=['POST'])
def analyze():
    # Check if a file was uploaded
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']

    # Check if the file is a valid Excel or CSV file
    if not file.filename.endswith(('.xlsx', '.xls', '.csv')):
        return jsonify({"error": "File must be in XLSX, XLS, or CSV format"}), 400

    # Read the uploaded file based on its format
    if file.filename.endswith('.csv'):
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)

    # Check if the required column exists
    if "review" not in df.columns and "Review" not in df.columns:
        return jsonify({"error": "File must contain 'review' column"}), 400

    # Extract reviews from the DataFrame
    reviews = df["review"].tolist() if "review" in df.columns else df["Review"].tolist()

    results = []

    # Analyze each review using the Groq API and log each sentiment result
    for i, review in enumerate(reviews):
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"Analyze the sentiment of this review: {review}",
                }
            ],
            model="mixtral-8x7b-32768",
        )
        sentiment = chat_completion.choices[0].message.content
        results.append(sentiment)

        # Print the review and the sentiment result for debugging purposes
        print(f"Review {i+1}: {review}")
        print(f"Sentiment: {sentiment}")
        print("-" * 50)

    # Custom logic to classify sentiments based on results (only 1 sentiment per review)
    positive_score = 0
    negative_score = 0
    neutral_score = 0

    for result in results:
        result_lower = result.lower()
        # Adjust positive/negative classifications to be more strict
        if 'positive' in result_lower or 'great' in result_lower or 'fantastic' in result_lower:
            positive_score += 1
        elif 'negative' in result_lower or 'bad' in result_lower or 'terrible' in result_lower:
            negative_score += 1
        else:
            # Expanded list of neutral indicators
            neutral_keywords = ["okay", "average", "nothing special", "mediocre", "moderate", "no complaints", "fine", "not bad", "neutral", "ordinary"]
            if any(keyword in result_lower for keyword in neutral_keywords):
                neutral_score += 1
            else:
                neutral_score += 1  # Default to neutral for any ambiguity

    # Ensure no review is counted multiple times and the total count adds up to the number of reviews
    total_reviews = len(reviews)
    classified_reviews = positive_score + negative_score + neutral_score

    print(f"Total reviews: {total_reviews}")
    print(f"Classified reviews: {classified_reviews} (should match total reviews)")

    return jsonify({
        "positive": positive_score,
        "negative": negative_score,
        "neutral": neutral_score
    })

if __name__ == '__main__':
    app.run(debug=True)
