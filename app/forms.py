from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError, validators, PasswordField
from app.models import db, User
import sqlalchemy as sa


class RegistrationForm(FlaskForm):
    name = StringField(
        "Name",
        validators=[validators.InputRequired(), validators.Length(min=2, max=25)],
    )
    email = StringField(
        "Email",
        validators=[
            validators.Email("This Field require a valid Email address"),
            validators.InputRequired(),
        ],
    )
    password = PasswordField(
        "New Password",
        validators=[validators.InputRequired()],
    )
    confirm_password = PasswordField(
        "Repeat password",
        validators=[validators.InputRequired(), validators.EqualTo("password")],
    )
    submit = SubmitField("Register")

    def validate_email(self, email):
        user = db.session.scalar(sa.select(User).where(User.email == email.data))
        if user is not None:
            raise ValidationError("This Email already exists")


class LoginForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[
            validators.Email("This Field require a valid Email address"),
            validators.InputRequired(),
        ],
    )
    password = PasswordField("Password", validators=[validators.InputRequired()])
    submit = SubmitField("Sign In")
