from flask import Blueprint, flash, request, render_template, redirect, url_for

from app.models import Blog, User

from . import db

routes_bp = Blueprint("blogs", __name__)


@routes_bp.route("/new", methods=["GET", "POST"])
def create_blog():
    if request.method == "GET":
        return render_template("create_blog.html")
    user = User.query.first()

    blog = Blog(
        title=request.form.get("title"),
        content=request.form.get("content"),
        author_id=user.id,
    )

    db.session.add(blog)
    db.session.commit()

    data = blog.to_dict()

    flash("Blog created successfully", "success")
    return render_template("blog_details.html", blog=data)


@routes_bp.route("/", methods=["GET"])
def get_blogs():
    blogs = Blog.query.all()
    blogs = [blog.to_dict() for blog in blogs]
    return render_template("index.html", blogs=blogs)


@routes_bp.route("/<int:blog_id>", methods=["GET"])
def get_blog(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    data = blog.to_dict()
    return render_template("blog_details.html", blog=data)


@routes_bp.route("/delete/<int:blog_id>", methods=["POST"])
def delete_blog(blog_id):
    blog = Blog.query.get_or_404(blog_id)

    db.session.delete(blog)
    db.session.commit()

    flash("Blog deleted successfully", "success")
    return redirect(url_for("blogs.get_blogs"))


@routes_bp.route("/edit/<int:blog_id>", methods=["POST", "GET"])
def update_blog(blog_id):
    blog = Blog.query.get_or_404(blog_id)

    if request.method == "POST":
        blog.title = request.form.get("title")
        blog.content = request.form.get("content")

        db.session.commit()

        flash("Blog updated successfully", "success")
        return redirect(url_for("blogs.get_blog", blog_id=blog.id))
    return render_template("update_blog.html", blog=blog.to_dict())
