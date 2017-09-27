from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func

app=Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres123@localhost/height_collector'
app.config['SQLALCHEMY_DATABASE_URI']='postgres://lqqjidqgvwrswm:6ad32067abe7a209768148d56cb17f0335554e42111f2500401546a32a3b19b5@ec2-107-21-108-204.compute-1.amazonaws.com:5432/d4ltu34umqnnn3?sslmode=require'
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(120), unique=True)
    height=db.Column(db.Integer)

    def __init__(self,email,height):
        self.email=email
        self.height=height

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        email=request.form["email_name"]
        height=request.form["height_name"]
        if db.session.query(Data).filter(Data.email==email).count() == 0:
            data=Data(email,height)
            db.session.add(data)
            db.session.commit()
            average_height=db.session.query(func.avg(Data.height)).scalar()
            count=db.session.query(Data.height).count()
            average_height=round(average_height,1)
            #send_email(email, height, average_height, count)
            return render_template("success.html")
    return render_template("index.html", text="Seems like we have got something from that email address already!")

if __name__=='__main__':
    app.run(debug=True)
