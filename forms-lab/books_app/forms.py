from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, TextAreaField
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.validators import DataRequired, Length
from books_app.models import Audience, Book, Author, Genre

class BookForm(FlaskForm):
    """Form to create a book."""
    title = StringField('Book Title', validators=[DataRequired(), Length(min=3, max=80)])
    publish_date = DateField('Date Published')
    author = QuerySelectField('Author', query_factory=lambda: Author.query, allow_blank=False)
    audience = SelectField('Audience', choices=Audience.choices())
    genres = QuerySelectMultipleField('Genres', query_factory=lambda: Genre.query)
    submit = SubmitField('Submit')


class AuthorForm(FlaskForm):
    """Form to create an author."""
    # - the author's name
    author_name = StringField("Author Name", validators=[DataRequired(), Length(min=3, max=80)])
    # - the author's biography (hint: use a TextAreaField)
    biography = TextAreaField("Biography")
    # - a submit button
    submit = SubmitField('Submit')

    # STRETCH CHALLENGE: Add more fields here as well as in `models.py` to
    # collect more information about the author, such as their birth date,
    # country, etc.
    pass


class GenreForm(FlaskForm):
    """Form to create a genre."""

    name = StringField('Genre', validators=[DataRequired(), Length(min=3, max=80)])
    submit = SubmitField('Submit')

    # TODO: Fill out the fields in this class for:
    # - the genre's name (e.g. fiction, non-fiction, etc)
    # - a submit button
    pass
