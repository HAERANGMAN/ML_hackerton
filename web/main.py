from flask import Flask, render_template, request, flash, redirect, url_for
from flask_migrate import Migrate

app = Flask(__name__)
migrate = Migrate(app, db)
app.secret_key = 'super secret key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/check", methods=['POST'])
def login():     
    request.method = 'POST'      
    if request.form["_username"] == "ubion" and request.form["_password"] == "tkdlek7":
        flash("환영합니다!")
        return redirect(url_for("main"))
    else:
        flash("다시 입력해주세요!")            
        return redirect(url_for("index"))

@app.route('/main', methods=["GET"])
def main():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug = True, port=8080)