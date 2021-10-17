import pyrebase

firebaseConfig = {
  'apiKey': "AIzaSyCWX3ruZgLg3ZOrR4iOjI6KJUQ7C0cyqko",
  'authDomain': "learningfirebase-c7efc.firebaseapp.com",
  'databaseURL': "https://learningfirebase-c7efc-default-rtdb.firebaseio.com",
  'projectId': "learningfirebase-c7efc",
  'storageBucket': "learningfirebase-c7efc.appspot.com",
  'messagingSenderId': "208359091768",
  'appId': "1:208359091768:web:a896ea2c442abba13e80cd",
  'measurementId': "G-ZTCGWXZZBS"
}

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
auth = firebase.auth()
storage = firebase.storage()


def login():

    email = input("Input your email: ")
    password = input("Input your password: ")

    try:
        result = auth.sign_in_with_email_and_password(email, password)
        print("Logged in!")
    except:
        print("Invalid username or password")

def sign_up():

    email = input("Input your email: ")
    password = input("Input your password: ")
    confirm_password = input("Confirm your password: ")

    if password == confirm_password:

        try:
            auth.create_user_with_email_and_password(email, password)
            print("Success!")

        except:
            print("Email already linked to an account")


def main():

    print("Input options: ")
    print("1) Login")
    print("2) Sign up")

    choice = input("\n\nWhat is your choice: ")

    try:
        choice = int(choice)

        if choice == 1:
            login()
        elif choice == 2:
            sign_up()
        else:
            raise

    except:
        print("Invalid input")


def code_write():
    ...

if __name__ == "__main__":
    # main()
    code_write()

