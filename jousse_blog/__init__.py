from flask import Flask, session, g, render_template
from jousse_blog.views import general

import websiteconfig as config

app = Flask(__name__)
app.debug = config.DEBUG
app.secret_key = config.SECRET_KEY

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


app.register_blueprint(general.mod)
