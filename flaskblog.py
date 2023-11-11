from flask import Flask, render_template, url_for, flash, redirect
from forms import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = '7b53c5999707163a9cfdcb99a2feebf5'

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)


posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog 1',
        'content': 'First content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog 2',
        'content': 'Second content',
        'date_posted': 'April 2, 2018'
    }

]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts,)


@app.route("/about")
def about():
    return render_template('about.html', title="About")


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == 'password':
            flash('You have been logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
