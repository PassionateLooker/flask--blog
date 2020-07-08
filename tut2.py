from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')
@app.route('/about')
def about():
    location='subhanagar'
    return render_template('about.html',name2=location)

app.run(debug=True)