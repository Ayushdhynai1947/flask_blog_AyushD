from flask import Flask, render_template



app = Flask(__name__)


posts =[
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content':'First post content',
        'date_poster':'April 20,2018'
    },
    {
        'auther':'Jane Doe',
        'title':'Blog post 2',
        'content':'Second post content',
        'date_poster':'April 21,2018'
    }
]





@app.route("/")
@app.route('/home')
def hello():
    return render_template('home.html',posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')




if __name__ =='__main__':
    app.run(debug=True)