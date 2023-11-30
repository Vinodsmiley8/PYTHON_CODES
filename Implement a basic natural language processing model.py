# Simple sentiment analysis using a rule-based approach
def analyze_sentiment(text):
    if "happy" in text:
        return "Positive"
    elif "sad" in text:
        return "Negative"
    else:
        return "Neutral"

# Usage
text = "I feel happy today!"
sentiment = analyze_sentiment(text)
print("Sentiment analysis result:", sentiment)