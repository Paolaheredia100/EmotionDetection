from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    return "Emotion Detection Application"

@app.route("/emotionDetector")
def detect_emotion():
    text_to_analyze = request.args.get('textToAnalyze')

    if text_to_analyze is None or text_to_analyze.strip() == "":
        return "Invalid text! Please try again."

    response = emotion_detector(text_to_analyze)

    if response is None:
        return "Error processing request."

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']}, "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
