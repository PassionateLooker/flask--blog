from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/code_with_daya'   #connect to DB
db = SQLAlchemy(app)   #initialize
class Contacts(db.Model):
    # sno name phone mess date email
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False,nullable=False)
    phone = db.Column(db.String(12),nullable=False)
    mess = db.Column(db.String(30),nullable=False)
    date = db.Column(db.String(12),nullable=True)
    email = db.Column(db.String(20),nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post')
def post():
    return render_template('post.html')

@app.route('/contact',methods=['GET','POST'])
def contact():
    if(request.method=='POST'):
        # add entry to DB
        name1=request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')


        entry=Contacts(name=name1,phone=phone,mess=message, email=email)
        db.session.add(entry)
        db.session.commit()
    return render_template('contact.html')




app.run(debug=True)