from flask import redirect, render_template, request, url_for, flash
import sqlalchemy as sa
from app import app, db
from app.models import Contractor, User
from app.forms import LoginForm, RegistrationForm
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/home", methods=["GET"])
@login_required
def home_page():
    contractors_list = Contractor.query.filter_by(user_id=current_user.id)
    return render_template("home_page.html", contractors_list=contractors_list)


@app.route("/contractor", methods=["POST", "GET"])
@login_required
def contractor():
    if request.method == "GET":
        return render_template("contractor_details.html")
    contractor = Contractor(
        user_id=current_user.id,
        name=request.form["name"],
        occupation=request.form["occupation"],
        salary=request.form["salary"],
        payout_at=request.form["payout_on"],
    )
    db.session.add(contractor)
    db.session.commit()
    return redirect("/")


@app.route("/contractor/<contractor_id>", methods=["POST"])
@login_required
def delete_contractor(contractor_id):
    contractor = Contractor.query.filter_by(
        id=contractor_id, user_id=current_user.id
    ).first_or_404()
    db.session.delete(contractor)
    db.session.commit()
    return redirect(url_for("home_page"))


@app.route("/register", methods=["POST", "GET"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home_page"))
    form = RegistrationForm()
    if request.method == "POST" and form.validate():
        user = User(name=form.name.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Congratulations, you are now a registered user!", "message")
        return redirect(url_for("login"))
    return render_template("register.html", form=form, title="Sign In", page="login")


@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home_page"))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(sa.Select(User).where(User.email == form.email.data))
        if user is None:
            flash("Invalid username or password", "error")
            return redirect(url_for("login"))
        login_user(user)
        return redirect(url_for("home_page"))
    return render_template("login.html", form=form, title="Sign Up", page="register")


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))
