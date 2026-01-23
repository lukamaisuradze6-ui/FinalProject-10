from flask import Flask, render_template, request, redirect, url_for, flash
from auth import create_users_table, register_user, login_user

app = Flask(__name__)
app.secret_key = "secret123"

# Create table if not exists
create_users_table()

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        first_last = request.form["first_last"]
        personal_number = request.form["PerNum"]
        password = request.form["Password"]
        confirm_password = request.form["Confirm_Password"]

        if password != confirm_password:
            flash("Passwords do not match")
            return render_template("register.html")

        if register_user(first_last, personal_number, password):
            flash("Registration successful! Please log in.")
            return redirect(url_for("login"))
        else:
            flash("A user with this personal number already exists")
    
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        personal_number = request.form["PerNum"]
        password = request.form["Password"]

        if login_user(personal_number, password):
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid credentials")

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return "Welcome to the Student Portal"

if __name__ == "__main__":
    app.run(debug=True)
