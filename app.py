from flask import Flask, render_template, request, redirect, url_for, flash  

                                                                    # flask is the main class used to create the web app
                                                                    # the render_template sends an html file to the browserr
                                                                    #request lets you access data forms from GET and POST
                                                                    #redirect it redirects user to  snother route
                                                                    #url_for safely builds URls for routes
                                                                    #flash sendds temporary message to HTML pages



from auth import create_users_table, register_user, login_user

#this line of code creates user table if it doesnt exist saves a user and check login details.



app = Flask(__name__)   # tells the app where the flask is located 
                        
app.secret_key = "ML1234" #used to encrypt temporary data 





create_users_table()       #creates user taable if it doesnt exist and runs once when app is started and prevents errors
 
@app.route("/register", methods=["GET", "POST"])    # it defines a route at register/ and allows GET and POST
def register():                                     #its a function that runs when /register is accessed 
    print("register route hit:", request.method)    #shows whether the request is GET or POST in terminal 



    if request.method == "POST":               #it runs only when the user submits a form 
        print("FORM DATA:", request.form)      #Prints all submitted form fields for debugging

        first_last = request.form.get("first_last")      #it reads input value from the html form and 
                                                        # .get() prevents crashes if theres a field missing 
        personal_number = request.form.get("PerNum")
        password = request.form.get("Password")
        confirm_password = request.form.get("Confirm_Password")




        print("VALUES:", first_last, personal_number)         #prints to comfirm if value has been recieved

        if not first_last or not personal_number or not password: #checks if any required fields are empty 
            flash("all fields are required")                      #shows an error message and reloads back to reg page
            return render_template("register.html")

        if password != confirm_password:                      #ensures that the user types the same password    
            flash("passwords do not match")                   # displays error if passsowrd does not match and returns to reg page
            return render_template("register.html")



        success = register_user(first_last, personal_number, password)  #calls the function in auth.py and attempts to insert the user details in the database
        print("register user results:", success)

        if success:                                 # runs if user was addded succesfully 
            flash("Registration successful! Please log in now.")    #shows success message and redirects to login 
            return redirect(url_for("login"))
        else:
            flash("user with this personal number already exists, try again") #happens if user already exists and doesnt redirects page just reloads 

    return render_template("register.html")      # shows the registeration page again and requests for GET



 
@app.route("/login", methods=["GET", "POST"])     # in login page shows form and proccss login
def login():
    print("LOGIN ROUTE HIT:", request.method)



    if request.method == "POST":                # runs when login form is submitted 
        personal_number = request.form.get("PerNum")            #gets login credentials 
        password = request.form.get("Password")

        print("LOGIN ATTEMPT:", personal_number)

        if login_user(personal_number, password): #calls the login from auth.py and checks the credentials 
            return redirect(url_for("dashboard"))  #if login is succcess after checking redirects to dahsboard 
        else:
            flash("Invalid user details")    #shows an error message if failed 

    return render_template("login.html")    # reloads back to login page  





@app.route("/dashboard")               # for the future itll show the portal after successful login 
def dashboard():
    return "Welcome to the Student Portal"


if __name__ == "__main__":    #insures it runs directly and isnt imported 
    app.run(debug=True)        #starts the flask development server it auto reloads on changes and shows detailed error pages