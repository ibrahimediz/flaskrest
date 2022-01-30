from flask import Flask
from flask import render_template
app = Flask(__name__)


from app import routes

@app.route('/')
@app.route('/index')
def index():

    return render_template("index.html",mesaj="orkun incili")