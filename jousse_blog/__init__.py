from flask import Flask, session, g, render_template
from flaskext.assets import Environment, Bundle
from jousse_blog.views import general, blog

import websiteconfig as config
import os, sys

app = Flask(__name__)
app.debug = config.DEBUG
app.secret_key = config.SECRET_KEY

assets = Environment(app)
assets.directory = os.path.join(os.path.abspath(os.path.dirname(__file__)),'.','static')

js = Bundle('javascripts/jquery.js', 'javascripts/cufon-yui.js',
            'javascripts/cufon.fonts.js',
            'javascripts/scripts.js',
            filters='jsmin', output='javascripts/packed.js')


css = Bundle('stylesheets/build.css',
            filters='cssmin', output='stylesheets/packed.css')

assets.register('js_all', js)
assets.register('css_all', css)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


app.register_blueprint(general.mod)
app.register_blueprint(blog.mod, url_prefix='/blog')
