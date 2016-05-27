from dbhelper import DBHelper
from flask import Flask
from flask import render_template
from flask import request

import logging

app = Flask(__name__)
DB = DBHelper()

logging.basicConfig(filename='/var/www/crimemap/crimemap.log', level=logging.DEBUG)

@app.route("/")
def home():
    try:
        data = DB.get_all_inputs()
    except Exception as e:
        print e
        data = None
    return render_template("home.html", data=data)

@app.route("/add", methods= ["POST"])
#@app.route("/add")
def add():
    try:
        data = request.form.get("userinput")
	#data = request.args.get("userinput")
	logging.debug(data)
        DB.add_input(data)
    except Exception as e:
        print e
    return home()

@app.route("/clear")
def clear():
    try:
        DB.clear_all()
    except Exception as e:
        print e
    return home()

if __name__ == '__main__':
    app.run(port=5000, debug=True)


