from flask import Flask, render_template, request, redirect, session
# import the class from friend.py
from models.count import Count
app = Flask(__name__)
app.secret_key = 'keep it  secret, keep it safe'


@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
        session['actual_count'] = 0
    else:
        session['count'] += 1
        session['actual_count'] += 1
    actual_count = session['actual_count']
    return render_template("index.html", actual_count=actual_count)

@app.route('/add_1', methods=["POST"])
def add_one():
    return redirect('/')

@app.route('/destroy_session')
def clear_session():
    session.clear()
    return redirect('/')

@app.route('/add_2', methods=["POST"])
def add_2_to_count():
    session['count'] += 1
    return redirect('/')

@app.route('/add_num', methods=["POST"])
def add_num():
    num = int(request.form['num'])
    session['count'] += (num - 1)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

