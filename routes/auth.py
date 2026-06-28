from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required

from models import db
from models.user import User

auth = Blueprint("auth", __name__)

#register route
@auth.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]

        email = request.form["email"]

        password = request.form["password"]

        confirm = request.form["confirm"]

        if password != confirm:
            flash("Passwords do not match")
            return redirect(url_for("auth.register"))

        user = User.query.filter_by(email=email).first()

        if user:
            flash("Email already exists")
            return redirect(url_for("auth.register"))

        hashed = generate_password_hash(password)

        new_user = User(
            username=username,
            email=email,
            password=hashed
        )

        db.session.add(new_user)
        db.session.commit()

        flash("Registration Successful")

        return redirect(url_for("auth.login"))

    return render_template("register.html")


#login route

@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]

        password = request.form["password"]

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):

            login_user(user)

            return redirect(url_for("dashboard.dashboard_page"))

        flash("Invalid Credentials")

    return render_template("login.html")


#logout route
@auth.route("/logout")
@login_required
def logout():

    logout_user()

    return redirect("/")