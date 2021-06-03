from textblob import TextBlob
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('emailanalysis.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = TextBlob(text)
    text_sentiment = processed_text.sentiment[0]
    if text_sentiment <= -.75:
        s = 'really mean'
    elif -.75 < text_sentiment <= -.25:
        s = 'negative'
    elif -.25 < text_sentiment < .25:
        s = 'relatively neutral'
    elif .25 <= text_sentiment < .75:
        s = 'pretty positive'
    elif text_sentiment >= .75:
        s = 'extremely nice'
    return f'You typed "{text}" -- Your text was {s} with an overall sentiment score of {text_sentiment}'
