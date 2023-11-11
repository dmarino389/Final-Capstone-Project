from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo


class DestinationForm(FlaskForm):
    title = StringField('Destination Name', validators = [DataRequired()])
    img_url = StringField('Destination Image', validators=[DataRequired()])
    description = StringField('Destination Description')



class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min = 5, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min = 8, max = 1000)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired(), Length(min = 5, max=20)])
    password = PasswordField("Password", [DataRequired()])
    submit = SubmitField("Login")

class PostForm(FlaskForm):
    title = StringField(label='Title', validators=[DataRequired()])
    img_url = StringField("Image URL", [DataRequired()])
    description = StringField('Destination Description')
    submit = SubmitField()
