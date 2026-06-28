from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user

from models import db
from models.project import Project

project = Blueprint("project", __name__)

#add projects
@project.route("/projects", methods=["GET", "POST"])
@login_required
def projects():

    if request.method == "POST":

        new_project = Project(
            user_id=current_user.id,
            project_name=request.form["project_name"],
            technology=request.form["technology"],
            description=request.form["description"],
            github_link=request.form["github_link"],
            demo_link=request.form["demo_link"]
        )

        db.session.add(new_project)
        db.session.commit()

        return redirect(url_for("project.projects"))

    all_projects = Project.query.filter_by(
        user_id=current_user.id
    ).all()

    return render_template(
        "projects.html",
        projects=all_projects
    )

#delete projects
@project.route("/delete_project/<int:id>")
@login_required
def delete_project(id):

    project_item = Project.query.filter_by(
        id=id,
        user_id=current_user.id
    ).first_or_404()

    db.session.delete(project_item)
    db.session.commit()

    return redirect(url_for("project.projects"))