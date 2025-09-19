from flask import Blueprint, render_template, redirect, url_for, flash,request
from flask_login import login_user, logout_user, login_required
from myproject.extensions import db
from myproject.models import User
from .forms import LoginForm, RegisterForm

bp = Blueprint("users", __name__, template_folder="templates/users")

@bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash("Logged in successfully!", "success")
            # Handle next URL if user was redirected to login
            next_page = request.args.get("next")
            if not next_page or not next_page.startswith("/"):
                next_page = url_for("projects.dashboard")
            return redirect(next_page)
        else:
            flash("Invalid email or password", "danger")
    return render_template("login.html", form=form)

@bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # Check if email or username already exists
        if User.query.filter_by(email=form.email.data).first():
            flash("Email already registered. Please login or use another email.", "danger")
            return redirect(url_for("users.register"))
        if User.query.filter_by(username=form.username.data).first():
            flash("Username already taken. Choose another one.", "danger")
            return redirect(url_for("users.register"))

        # Create new user
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Registration successful! Please login.", "success")
        return redirect(url_for("users.login"))
    return render_template("register.html", form=form)


@bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for("home"))