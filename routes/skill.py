from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user

from models import db
from models.skill import Skill

skill = Blueprint("skill", __name__)
#add skill route
@skill.route("/skills", methods=["GET", "POST"])
@login_required
def skills():

    if request.method == "POST":

        skill_name = request.form["skill"]

        new_skill = Skill(
            user_id=current_user.id,
            skill_name=skill_name
        )

        db.session.add(new_skill)
        db.session.commit()

        return redirect(url_for("skill.skills"))

    all_skills = Skill.query.filter_by(
        user_id=current_user.id
    ).all()

    return render_template(
        "skills.html",
        skills=all_skills
    )


#Delete skill route
@skill.route("/delete_skill/<int:id>")
@login_required
def delete_skill(id):

    item = Skill.query.get_or_404(id)

    db.session.delete(item)

    db.session.commit()

    return redirect(url_for("skill.skills"))