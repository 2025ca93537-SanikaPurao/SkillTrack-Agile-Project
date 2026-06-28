from flask import Blueprint, render_template
from flask_login import login_required, current_user

from models.profile import Profile
from models.skill import Skill
from models.project import Project

dashboard = Blueprint("dashboard", __name__)

@dashboard.route("/dashboard")
@login_required
def dashboard_page():

    profile = Profile.query.filter_by(
        user_id=current_user.id
    ).first()

    total_skills = Skill.query.filter_by(
        user_id=current_user.id
    ).count()

    total_projects = Project.query.filter_by(
        user_id=current_user.id
    ).count()

    recent_projects = Project.query.filter_by(
        user_id=current_user.id
    ).order_by(Project.id.desc()).limit(5).all()

    return render_template(
        "dashboard.html",
        user=current_user,
        profile=profile,
        total_skills=total_skills,
        total_projects=total_projects,
        recent_projects=recent_projects
    )