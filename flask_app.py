from googletrans import Translator
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def hello_world():
    if request.method == 'POST':
        source_text = request.form['source_text']
        translator = Translator()
        temp_text = translator.translate(source_text, src='ru', dest='ja').text
        temp_text = translator.translate(temp_text, src='ja', dest='en').text
        result_text = translator.translate(temp_text, src='en', dest='ru').text
        return render_template('home.html', source_text=source_text, result_text=result_text)
    if request.method == 'GET':
        return render_template('home.html', source_text=' ', result_text=' ')

