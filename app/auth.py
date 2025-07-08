from flask import Blueprint, render_template, redirect, url_for, flash, session
from app.forms import LoginForm
from app.models import User


auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            session["user_id"] = user.id
            flash("Logged in successfully.", "success")
            return redirect(url_for("blogs.get_blogs"))
        else:
            flash("Invalid username or password.", "danger")
    return render_template("login.html", form=form)


@auth_bp.route("/logout")
def logout():
    session.pop("user_id", None)
    flash("You have been logged out.", "info")
    return redirect(url_for("blogs.get_blogs"))
