# Overview

This is my experimentation of Google Firebase. I am using this to prepare for making an app called
Love Tap. Currently, this software allows a person to create an account, as well as login. All of 
this done remotely through the terminal.

[Software Demo Video](https://youtu.be/vxWPMw6ubaI)

# Cloud Database

For this project, I am using Firebase's realtime database. This database
is split into the following structure:

{an individual connection (ID)} 
    {Messages}
        {an individual message}
            {the actual message}
            {user views}
                user1 (boolean of if they have seen it)
                user2 (boolean of if they have seen it)
    {users}
        {A list of user UID's that are in this connection}


# Development Environment


I used PyCharm as my IDE, and I used the pyrebase4 module. This was all written in Python as well. 


# Useful Websites


* [Web Site Name](https://firebase.google.com/docs/database/security)
* [Web Site Name](https://firebase.google.com/docs/firestore/query-data/listen#java)

# Future Work


* I need to make it so that users can add to their messages, but ONLY their messages