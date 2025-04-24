'''
Module to define the website endpoints and Flask configuration to run the application
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Final Project')

@app.get('/emotionDetector')
def emotion_detect():
    '''
    Analyze the user input to determine emotion scores and the dominant emotion
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)
    if not result['dominant_emotion']:
        return 'Invalid text! Please try again!'

    message = f"For the given statement, the system response is 'anger': {result['anger']}, "
    message += f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']}, "
    message += f"'sadness': {result['sadness']}. "
    message += f"The dominant emotion is {result['dominant_emotion']}."
    return message

@app.get('/')
def index():
    '''
    Display the index page when you access the website
    '''
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
