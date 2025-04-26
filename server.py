from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
import json

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the label and score from the response
    joy = response['joy']
    fear = response['fear']
    disgust = response['disgust']
    anger = response['anger']
    sadness = response['sadness']
    domain_emotion = response['domain_emotion']

    # Return a formatted string with the sentiment label and score

    if domain_emotion is None:
        return  "Invalid text! Please try again!"

    else:
        return f"For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, and 'sadness': {sadness}. The dominant emotion is {domain_emotion}."


@app.route("/")
def render_index_page():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)