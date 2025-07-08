from flask import Blueprint, request, flash
from app import db
from app.models import Blog, User


routes_bp = Blueprint("", __name__)


@routes_bp.route("/new", methods=["POST"])
def create_blog():
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
    return data


@routes_bp.route("/", methods=["GET"])
def get_blogs():
    blogs = Blog.query.all()

    data = {
        "blogs": [blog.to_dict() for blog in blogs],
        "total": len(blogs),
    }

    return data


@routes_bp.route("/<int:blog_id>", methods=["GET"])
def get_blog(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    data = blog.to_dict()
    return data


@routes_bp.route("/delete/<int:blog_id>", methods=["POST"])
def delete_blog(blog_id):
    blog = Blog.query.get_or_404(blog_id)

    db.session.delete(blog)
    db.session.commit()

    flash("Blog deleted successfully", "success")
    return


@routes_bp.route("/edit/<int:blog_id>", methods=["POST"])
def update_blog(blog_id):
    blog = Blog.query.get_or_404(blog_id)

    blog.title = request.form.get("title")
    blog.content = request.form.get("content")

    db.session.commit()

    data = blog.to_dict()

    flash("Blog updated successfully", "success")
    return data
