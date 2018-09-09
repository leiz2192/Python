#!/usr/bin/python
# -*- coding:utf-8 -*-


from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello Manila World!'


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'Hello User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Hi Post %d' % post_id


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
