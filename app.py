from flask import Flask, request, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("form.html")

@app.route('/submit', methods=["POST"])
def submit():
    fullname = request.form['fullname']
    bdate = request.form['bdate']
    date = datetime.strptime(bdate, '%Y-%m-%d')
    today = datetime.today()
    age = today.year - date.year - ((today.month, today.day) < (date.month, date.day))
    return jsonify(fullname=fullname, age=age)

if __name__ == "__main__":
    app.run(debug=True)