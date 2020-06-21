from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/codingthunder'
db = SQLAlchemy(app)

class Contacts(db.Model):
    '''sno name email phone_num mes date '''
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    mes = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12),nullable=True)

@app.route('/')
def default():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact', methods=['GET','POST'])
def contact():
    if request.method=='POST':
        '''Add entry to the database'''
        name=request.form.get('name')
        mail = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        entry=Contacts(name=name, date=datetime.now(), email=mail, phone_num=phone, mes=message)
        db.session.add(entry)
        db.session.commit()

    return render_template("contact.html")

@app.route('/post')
def post():
    return render_template("post.html")

app.run(debug=True)