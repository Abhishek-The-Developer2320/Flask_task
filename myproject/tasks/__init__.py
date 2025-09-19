from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from myproject.extensions import db
from myproject.models import Project, Task
from myproject.tasks.forms import TaskForm

bp = Blueprint("tasks", __name__, template_folder="templates/tasks")

@bp.route("/<int:project_id>/tasks")
@login_required
def task_list(project_id):
    project = Project.query.get_or_404(project_id)
    tasks = project.tasks
    return render_template("tasks.html", project=project, tasks=tasks)

@bp.route("/<int:project_id>/tasks/create", methods=["GET", "POST"])
@login_required
def create_task(project_id):
    project = Project.query.get_or_404(project_id)
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(
                title=form.title.data,
                description=form.description.data,
                is_done=form.is_done.data,
                project_id=project.id,
                user_id=current_user.id
        )
        db.session.add(task)
        db.session.commit()
        flash("Task added!")
        return redirect(url_for("tasks.task_list", project_id=project.id))
    return render_template("task_detail.html", form=form, project=project)
@bp.route("/<int:task_id>/toggle", methods=["POST"])
@login_required
def toggle_task(task_id):
    task = Task.query.get_or_404(task_id)
    # Only the task owner or project owner can update
    if task.user_id != current_user.id and task.project.owner_id != current_user.id:
        flash("You are not allowed to update this task.")
        return redirect(url_for("tasks.task_list", project_id=task.project_id))
    
    task.is_done = not task.is_done  # Toggle status
    db.session.commit()
    return redirect(url_for("tasks.task_list", project_id=task.project_id))

