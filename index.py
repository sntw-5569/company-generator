import json
import datetime
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index_view():
    return render_template('index.html')

@app.route('/ent')
def ent_view():
    title = 'Company Generator'
    return render_template('ent.html', title=title)

def handler(event, context):
        return render_template('index.html')

if __name__ == "__main__":
    app.run("0.0.0.0", port=5005, debug=True)