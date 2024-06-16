from flask import Flask, render_template,url_for
from my_blog import RegistrationForm ,LoginForm



"""talkieTime"""
app = Flask(__name__)
app.config['SECRET_KEY'] = '0839e7253dfb7c08d6fc59d8ef127f22'

posts =[
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content':'First post content',
        'date_poster':'April 20,2018'
    }
     ,
    {
        'auther':'Jane Doe',
        'title':'Blog post 2',
        'content':'Second post content',
        'date_poster':'April 21,2018'
    }
]


@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='About')


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html',title='Regsiter', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html',title='Login', form=form)







if __name__ =='__main__':
    app.run(debug=True)