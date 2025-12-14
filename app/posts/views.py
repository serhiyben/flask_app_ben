from flask import render_template, redirect, url_for, flash
from . import posts_bp
from app import db
from .models import Post
from .forms import PostForm

@posts_bp.route('/', methods=['GET'])
def list_posts():
    """Відображення всіх постів"""
    posts = Post.query.order_by(Post.posted.desc()).all()
    return render_template('posts/posts.html', posts=posts)

@posts_bp.route('/create', methods=['GET', 'POST'])
def create_post():
    """Створення нового поста"""
    form = PostForm()

    if form.validate_on_submit():
        post = Post(
            title=form.title.data,
            content=form.content.data,
            category=form.category.data
        )
        db.session.add(post)
        db.session.commit()
        
        flash('Пост успішно створено!', 'success')
        return redirect(url_for('posts.list_posts'))

    return render_template('posts/create_post.html', form=form, title="Створити пост")

@posts_bp.route('/<int:id>')
def post_detail(id):
    """Перегляд одного поста"""
    # get_or_404 автоматично віддасть помилку 404, якщо id не існує
    post = db.get_or_404(Post, id)
    return render_template('posts/detail_post.html', post=post)

@posts_bp.route('/<int:id>/update', methods=['GET', 'POST'])
def update_post(id):
    """Редагування поста"""
    post = db.get_or_404(Post, id)
    
    # obj=post автоматично заповнює форму даними з бази
    form = PostForm(obj=post)

    if form.validate_on_submit():
        # Оновлюємо поля поста даними з форми
        form.populate_obj(post)
        db.session.commit()
        flash('Пост успішно оновлено!', 'success')
        return redirect(url_for('posts.post_detail', id=post.id))

    return render_template('posts/create_post.html', form=form, title="Редагувати пост")

@posts_bp.route('/<int:id>/delete', methods=['POST'])
def delete_post(id):
    """Видалення поста"""
    post = db.get_or_404(Post, id)
    
    db.session.delete(post)
    db.session.commit()
    
    flash('Пост видалено!', 'info')
    return redirect(url_for('posts.list_posts'))