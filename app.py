from flask import Blueprint,render_template,request,session
from werkzeug.security import generate_password_hash,check_password_hash
from models import db, User 

auth=Blueprint('auth',__name__)

@auth.route('/register',methods=["GET,"POST"])
def register():
    if request.method=="POST":
       email=request.form["email"]
       password=generate_password_hash(request.form['password'])
       user=User(email=email,password=password)
       db.session.add(user)
       db.session.commit()
       return redirect("/login")
    return render_template("register.html")


    