from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Final Project')

@app.get('/emotionDetector')
def emotion_detect():
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)
    message = f"For the given statement, the system response is 'anger': {result['anger']}, "
    message += f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']}, "
    message += f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    return message

@app.get('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
