from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)

bootstrap = Bootstrap(app)

@app.route('/bootstrap')
def bootstrap():
    author={
        'name':'kikay',
        'age':20,
        'friends':[
            {'name':'Andy_who','age':60},
            {'name':'Tom\\Mark','age':29},
            {'name':u'小花','age':18}
        ]
    }
    return render_template('bootstrap.html',
                           author=author,
                           title='Bootstrap')


@app.route('/user/<path:name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name


if __name__ == '__main__':
    app.run(debug=True)