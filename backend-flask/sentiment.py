from textblob import TextBlob

def analyze_sentiment(text):
    # Perform sentiment analysis
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity

    # Determine sentiment label based on score
    if sentiment_score > 0.05:
        sentiment_label = "Positive"
    elif sentiment_score < -0.05:
        sentiment_label = "Negative"
    else:
        sentiment_label = "Neutral"
    
    return sentiment_label, sentiment_score
