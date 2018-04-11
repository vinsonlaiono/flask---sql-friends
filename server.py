from flask import Flask, render_template, redirect, request
# import the function connectToMySQL from the file mysqlconnection.py
from mysqlconnection import connectToMySQL
app = Flask(__name__)
# invoke the connectToMySQL function and pass it the name of the database we're using
# connectToMySQL returns an instance of MySQLConnection, which we will store in the variable 'mysql'
mysql = connectToMySQL('friendsdb')
# now, we may invoke the query_db method
print("all the users", mysql.query_db("SELECT * FROM friends;"))

@app.route('/')
def index():
    all_friends = mysql.query_db("SELECT first_name, last_name, occupation FROM friends")
    print("Fetched all friends", all_friends)

    return render_template('index.html', friends = all_friends, friend1 = friend1, friend2 = friend2, friend3=friend3)

@app.route('/create_friend', methods=['POST', 'GET'])
def create():    
    
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(occupation)s, NOW(), NOW());"
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'occupation': request.form['occupation']
           }
    mysql.query_db(query, data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
