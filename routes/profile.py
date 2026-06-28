from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from flask_login import login_required
from flask_login import current_user

from models import db
from models.profile import Profile

profile = Blueprint("profile", __name__)

@profile.route("/profile", methods=["GET", "POST"])
@login_required
def profile_page():

    student = Profile.query.filter_by(
        user_id=current_user.id
    ).first()

    if request.method == "POST":

        if student is None:

            student = Profile(
                user_id=current_user.id
            )

            db.session.add(student)

        student.full_name = request.form["full_name"]
        student.phone = request.form["phone"]
        student.college = request.form["college"]
        student.degree = request.form["degree"]
        student.graduation_year = request.form["graduation_year"]
        student.linkedin = request.form["linkedin"]
        student.github = request.form["github"]
        student.bio = request.form["bio"]

        db.session.commit()

        return redirect(url_for("dashboard.dashboard_page"))

    return render_template(
        "profile.html",
        profile=student
    )