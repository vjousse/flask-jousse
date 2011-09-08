from flask import Flask

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return 'Index page'

@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/user/<username>')
def user_profile(username):
    return 'Hi {0}'.format(username)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post id {0}'.format(post_id)

if __name__ == '__main__':
    app.run()
