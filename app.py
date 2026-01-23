from flask import Flask, render_template, request, redirect, url_for, flash
from auth import create_users_table, register_user, login_user

# ------------------ FLASK SETUP ------------------ #
# template_folder="." allows Flask to access index.html in root
# static_folder="." allows CSS/images in style/ and pics/
app = Flask(
    __name__,
    template_folder="templates",  # HTML files here
    static_folder="static"        # CSS/images served from here
)


app.secret_key = "ML1234"

# Create database table if it doesn't exist
create_users_table()


# ------------------ ROUTES ------------------ #

@app.route("/", methods=["GET", "POST"])
def login():
    """Render and process login using index.html as login page."""
    if request.method == "POST":
        personal_number = request.form.get("PerNum")
        password = request.form.get("Password")

        if login_user(personal_number, password):
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid user details")

    return render_template("index.html")  # login page is index.html in root


@app.route("/register", methods=["GET", "POST"])
def register():
    """Render and process registration form."""
    if request.method == "POST":
        first_last = request.form.get("first_last")
        personal_number = request.form.get("PerNum")
        password = request.form.get("Password")
        confirm_password = request.form.get("Confirm_Password")

        # Check required fields
        if not first_last or not personal_number or not password:
            flash("All fields are required")
            return render_template("pages/register.html")

        # Check passwords match
        if password != confirm_password:
            flash("Passwords do not match")
            return render_template("pages/register.html")

        # Register user
        if register_user(first_last, personal_number, password):
            flash("Registration successful! Please log in now.")
            return redirect(url_for("login"))
        else:
            flash("User with this personal number already exists")
            return render_template("pages/register.html")

    return render_template("pages/register.html")


@app.route("/dashboard")
def dashboard():
    """Dashboard after successful login."""
    return "Welcome to the Student Portal"


if __name__ == "__main__":
    app.run(debug=True)
