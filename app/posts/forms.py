from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

class PostForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired(), Length(min=2, max=150)])
    content = TextAreaField('Зміст', validators=[DataRequired()])
    category = SelectField('Категорія', choices=[
        ('news', 'Новини'),
        ('publication', 'Публікація'),
        ('tech', 'Технології'),
        ('other', 'Інше')
    ])
    submit = SubmitField('Зберегти')