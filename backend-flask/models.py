from db import mongo

class SentimentAnalysis:
    @staticmethod
    def save_analysis(username, text, sentiment_label, sentiment_score):
        mongo.db.analysis.insert_one({
            "username": username,
            "text": text,
            "sentiment_label": sentiment_label,
            "sentiment_score": sentiment_score
        })

    @staticmethod
    def get_user_history(username):
        history = mongo.db.analysis.find({"username": username})
        return list(history)
