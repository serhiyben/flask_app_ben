from flask import render_template, redirect, url_for, flash
from . import posts_bp
from app import db
from .models import Post
from .forms import PostForm


@posts_bp.route("/", methods=["GET"])
def list_posts():
    """Відображення всіх постів"""

    posts = Post.query.order_by(Post.posted.desc()).all()
    return render_template("posts/posts.html", posts=posts)


@posts_bp.route("/create", methods=["GET", "POST"])
def create_post():
    """Створення нового поста"""
    form = PostForm()

    if form.validate_on_submit():

        post = Post(
            title=form.title.data,
            content=form.content.data,
            category=form.category.data,
        )

        db.session.add(post)
        db.session.commit()

        flash("Пост успішно створено!", "success")
        return redirect(url_for("posts.list_posts"))

    return render_template("posts/create_post.html", form=form)
