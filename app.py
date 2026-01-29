from flask import Flask, render_template, request, redirect, url_for, flash
from auth import create_users_table, register_user, login_user

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

app.secret_key = "ML1234"

# Create DB table if not exists
create_users_table()


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        personal_number = request.form.get("Username")
        password = request.form.get("Password")

        if login_user(personal_number, password):
            return redirect(url_for("mainpage"))
        else:
            flash("Invalid user details")

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
            return render_template("pages/register.html")

        if password != confirm_password:
            flash("Passwords do not match")
            return render_template("pages/register.html")

        if register_user(first_last, personal_number, password):
            flash("Registration successful! Please log in now.")
            return redirect(url_for("login"))
        else:
            flash("User with this personal number already exists")
            return render_template("pages/register.html")

    return render_template("pages/register.html")


@app.route("/mainpage")
def mainpage():
    return render_template("pages/mainpage.html")


@app.route("/dashboard")
def dashboard():
    return "Welcome to the Student Portal"


if __name__ == "__main__":
    app.run(debug=True)
