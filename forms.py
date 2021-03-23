from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm


class SearchForm(FlaskForm):
    """прописываю поля формы"""
    city = StringField('City name')
    submit = SubmitField('Search')
