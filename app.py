from flask import Flask, render_template, request, redirect, url_for, flash, session
from auth import (
    create_users_table,
    create_courses_table,
    create_enrollments_table,
    enroll_course,
    register_user,
    login_user,
    seed_course
)

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

app.secret_key = "ML1234"


create_users_table()
create_courses_table()
create_enrollments_table()
seed_course()


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        personal_number = request.form.get("PerNum")
        password = request.form.get("Password")

        if login_user(personal_number, password):
            session["user"] = personal_number
            return redirect(url_for("mainpage"))
        else:
            flash("Invalid user details")
            return redirect(url_for("login"))

    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        first_last = request.form.get("first_last")
        personal_number = request.form.get("PerNum")
        password = request.form.get("Password")
        confirm_password = request.form.get("Confirm_Password")

        if not first_last or not personal_number or not password:
            flash("All fields are required")
            return redirect(url_for("register"))

        if password != confirm_password:
            flash("Passwords do not match")
            return redirect(url_for("register"))

        if register_user(first_last, personal_number, password):
            flash("Registration successful! Please log in.")
            return redirect(url_for("login"))   
        else:
            flash("User with this personal number already exists")
            return redirect(url_for("register"))

    return render_template("pages/register.html")





@app.route("/mainpage")
def mainpage():
    if "user" not in session:
        return redirect(url_for("login"))

    return render_template("pages/mainpage.html")





@app.route("/enroll/<int:course_id>")
def enroll(course_id):
    if "user" not in session:
        return redirect(url_for("login"))

    enroll_course(session["user"], course_id)
    return redirect(url_for("mainpage"))





@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))





if __name__ == "__main__":
    app.run(debug=True)
