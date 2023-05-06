from flask import Flask, jsonify
import mysql


app = Flask(__name__)

@app.route('/users')
def get_users():
    # Connect to database
    cnx = mysql.connector.connect(user='root', password='password',
                                  host='localhost', database='users.sql')
    cursor = cnx.cursor()

    # Execute query
    query = "SELECT id, username, password FROM users"
    cursor.execute(query)

    # Build response
    users = []
    for (id, username, password) in cursor:
        user = {
            'id': id,
            'username': username,
            'password': password
        }
        users.append(user)

    # Clean up resources
    cursor.close()
    cnx.close()

    # Return response
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
