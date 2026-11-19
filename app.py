import sqlite3

from flask import Flask, request

app = Flask(__name__)


@app.route("/users")
def users():
    name = request.args.get("name")
    connection = sqlite3.connect("users.db")
    return str(connection.execute("SELECT * FROM users WHERE name = '" + name + "'").fetchall())
