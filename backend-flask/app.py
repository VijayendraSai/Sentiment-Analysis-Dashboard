from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from flask_cors import CORS
from db import init_db
from auth import auth_bp
from sentiment import analyze_sentiment
from models import SentimentAnalysis

app = Flask(__name__)

# Enable CORS
CORS(app)

# Initialize JWT manager
app.config["JWT_SECRET_KEY"] = "your_jwt_secret_key"
jwt = JWTManager(app)

# Initialize Database
init_db(app)

# Register Authentication Blueprint
app.register_blueprint(auth_bp, url_prefix='/auth')

# Sentiment Analysis API
@app.route('/analyze', methods=['POST'])
@jwt_required()
def analyze():
    text = request.json.get('text')
    if not text:
        return jsonify({"msg": "Text is required"}), 400
    
    # Get current user
    current_user = get_jwt_identity()
    
    # Perform sentiment analysis
    sentiment_label, sentiment_score = analyze_sentiment(text)
    
    # Save analysis to the database
    SentimentAnalysis.save_analysis(current_user, text, sentiment_label, sentiment_score)
    
    return jsonify({"sentiment": sentiment_label, "confidence": sentiment_score})

# Fetch User's Analysis History
@app.route('/history', methods=['GET'])
@jwt_required()
def history():
    current_user = get_jwt_identity()
    history = SentimentAnalysis.get_user_history(current_user)
    
    return jsonify(history), 200

if __name__ == "__main__":
    app.run(debug=True)
