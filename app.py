# create a simple flask app
import flask
import openai
from flask import Flask, render_template, request
from dotenv import dotenv_values

config = dotenv_values(".env")
openai.api_key = config['OPEN_API_KEY']

app = Flask(__name__,
            template_folder='templates')

@app.route('/inspiration')
def inspiration():
    for quoteText in openai.Completion.create(
        model="text-davinci-003",
        prompt="Give me a really long inspiration quote: ",
        max_tokens=250,
        temperature=0,
        stream=True,
    ):
        print(quoteText.choices[0].text, end="", flush=True)
    return render_template('index.html')
    #return response["choices"][0]["text"]
    #return render_template('index.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/palette', methods=['POST'])
def palette():
    # OPEN AI Completion call
    return "will return color palette from openai"
    #Return list of colors





@app.route('/hello/<name>')
def hello(name):
    return "hello from " + name + "!"
if __name__ == '__main__':
    app.run(debug=True)