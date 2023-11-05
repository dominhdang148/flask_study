from flask import Flask, render_template, url_for
from forms import *

app = Flask(__name__)
app.config['SECRET_KEY'] = '7b53c5999707163a9cfdcb99a2feebf5'


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


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
