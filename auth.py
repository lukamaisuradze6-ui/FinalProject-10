import sqlite3         #use SQL to sav intp database
import bcrypt          #used to hash password for hackers not to inercept 
import os              #allows operating ssystem featuress for fiile path
 


DB_NAME = "student_portal.db"                        # The SQL database file where users will be stored
print("PATH OF DATABASE:", os.path.abspath(DB_NAME)) # this line of code prints the path of the database for us to aces it 



def create_users_table():                            #creates a table if there isnt
    conn = sqlite3.connect(DB_NAME)                  #it connects the sql browser with the database
    cursor = conn.cursor()                           # object to SQL execute commands
    cursor.execute("""                               
                   
        create the table if not exists users (
                   
            ID INTEGER PRIMARY KEY AUTOINCREMENT,         
            first_last TEXT NOT NULL,
            personal_number TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    """)                                               # the triple quotes allow us to write multiple strings 
                                                       # genertes ID that is unique for every user
                                                       # the first and last name should be a text and cant leave it empty
                                                       # the personal number should be unique for every user
                                                       # password doesnt need to be unique because its hashed


    conn.commit()                                      # it saves changes in the database
    conn.close()                                       # closes the connection 
 



def register_user(first_last, personal_number, password):     #this is a function to add a new user
    password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()      #the bcrypt hashes the password and the 
                                                                                     #encode converts it into bytes 
                                                                                     #decode converts hash back into strings to store it in the database
    
    conn = sqlite3.connect(DB_NAME)                                                  #connects to the Database
    cursor = conn.cursor()




    try:
        cursor.execute(
            "insert into users (first_last, personal_number, password_hash) VALUES (?, ?, ?)", # the question marks are placeholder used to prevent sql injections  
            (first_last, personal_number, password_hash)                                      
        )


        conn.commit()              #saves changes
        return True                # returns true if registeration is a success
    except sqlite3.IntegrityError: #it catches errorrs if there are any duplicates
        return False               # it returns false if the registeration isnt a success
    finally:
        conn.close()        # it ensures that database connection is always closed even if there are errors 





def login_user(personal_number, password):     #checks if user can login
    conn = sqlite3.connect(DB_NAME)            # connects to database
    cursor = conn.cursor()

    cursor.execute(
        "select password_hash from users where personal_number = ?",
        (personal_number,)             #gets the hashed password for the given personal number
    )
    result = cursor.fetchone()         # fetches 1 row or none if not found
    conn.close()                       # ensures database connection is closed



    if not result:
        return False                   # if the user doesnt exist it returns false

    return bcrypt.checkpw(password.encode(), result[0].encode())   #it compares the entered passowrd with the stored hashed password 
                                                                   # itll return true if it matches and false if it doesnt
