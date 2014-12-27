from flask import Flask
from flask import request
import sqlite3
from flask import render_template


app = Flask(__name__)


@app.route("/")
def home():
    file_object = open("website.html", "r").read()
    return str(file_object)


@app.route("/search-page/")
def search():
    searchword = request.args.get('search', '')
    db = sqlite3.connect('website.db')
    cursor = db.cursor()
    result = cursor.execute("SELECT url, title FROM website").fetchall()

    return render_template("result.html", links=result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, use_reloader = True)
