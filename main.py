from flask import Flask, render_template,request,url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/bytewalker'
db = SQLAlchemy(app)



@app.route("/")
def home():
    print("home")
    return render_template('index.html')


@app.route("/about")
def about():
    print("about")
    return render_template('about.html')


@app.route("/contact",methods=['POST','GET'])
def contact():
    print("contact")
    print("raviiiiiii",request.method == 'POST')
    if(request.method == 'POST'):
        print("request.method")
        #user = request.form['name']
        Name =request.form["name1"]
        email=request.form["email"]
        Phone=request.form["phone"]
        Message=request.form["message"]
        print(Name,email,Message,Phone)
        entry=contact(name=Name,email=email,phone_num=Phone,message=Message,date=datetime.now())         #left side name is database name & right is fun name
        db.session.add(entry)
        db.session.commit()

    return render_template('contact.html')


class contact(db.Model):
    print("-----------------blank-----------")
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text,nullable=False)
    email = db.Column(db.Text,nullable=False)
    message = db.Column(db.Text,nullable=False)
    date = db.Column(db.DateTime,nullable=False)
    phone_num = db.Column(db.Integer, nullable=False)
    print(sno,name,email,message,date,phone_num)


@app.route("/post")
def post():
    return render_template('post.html')



app.run(debug=True)
