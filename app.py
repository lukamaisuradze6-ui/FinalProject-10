from flask import Flask, request, redirect, url_for, flash, send_from_directory
from auth import create_users_table, register_user, login_user
import os

app = Flask(__name__)
app.secret_key = "dev-secret-key"  # fine for small project

# Make sure DB exists
create_users_table()


# Serve HTML files from same folder
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        first_last = request.form.get("first_last")
        personal_number = request.form.get("PerNum")
        password = request.form.get("Password")
        confirm_password = request.form.get("Confirm_Password")

        if password != confirm_password:
            flash("Passwords do not match")
            return send_from_directory(".", "register.html")

        if register_user(first_last, personal_number, password):
            flash("Registration successful! Please log in.")
            return redirect(url_for("login"))
        else:
            flash("User with this personal number already exists")

    return send_from_directory(".", "register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        personal_number = request.form.get("PerNum")
        password = request.form.get("Password")

        if login_user(personal_number, password):
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid credentials")

    return send_from_directory(".", "login.html")


@app.route("/dashboard")
def dashboard():
    return "Welcome to the Student Portal"


if __name__ == "__main__":
    app.run(debug=True)

print("DB FILE USED:", os.path.abspath(DB_NAME))
