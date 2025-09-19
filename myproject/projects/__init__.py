from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from myproject.extensions import db
from myproject.models import Project
from .forms import ProjectForm

bp = Blueprint("projects", __name__, template_folder="templates/projects")

@bp.route("/dashboard")
@login_required
def dashboard():
    projects = current_user.projects
    return render_template("dashboard.html", projects=projects)

@bp.route("/create", methods=["GET", "POST"])
@login_required
def create_project():
    form = ProjectForm()
    if form.validate_on_submit():
        project = Project(title=form.title.data, description=form.description.data, owner=current_user)
        db.session.add(project)
        db.session.commit()
        flash("Project created!")
        return redirect(url_for("projects.dashboard"))
    return render_template("project_detail.html", form=form)
