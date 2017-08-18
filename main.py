import os
from flask import *
from functools import wraps

app = Flask(__name__)

app.secret_key = 'elgordo123456789'

users = {'admin':'admin','art':'art'}

@app.route('/register')
def register():
    return render_template('register.html')

def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash("You need to login first.")
            return redirect(url_for('log'))
    return wrap

@app.route("/login", methods=['GET','POST'])
def log():
    error = None
    if request.method == 'POST':
        if request.form['username'] not in users.keys() or request.form['password'] not in users.values() :
            error = 'Invalid Credentials'
        else:
            session['logged_in'] = True
            return redirect(url_for('hello'))
    return render_template('home.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You Were Logged Out !')
    return redirect (url_for('login'))

@app.route('/hello')
@login_required
def hello():
    return render_template('hello.html') 



if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)