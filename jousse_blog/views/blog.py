from flask import Blueprint, render_template, abort, request, \
     session, flash, redirect, url_for
from jinja2 import TemplateNotFound
import websiteconfig as config

from jousse_blog import model

mod = Blueprint('blog', __name__)


@mod.route('/')
def index():
    try:
        return render_template('blog/index.html')
    except TemplateNotFound:
        abort(404)
 

@mod.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        if request.form['username'] != config.USERNAME:
            error = 'Invalid username'
        elif request.form['password'] != config.PASSWORD:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('.admin'))

    return render_template('blog/login.html', error=error)


@mod.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect(url_for('.index'))


@mod.route('/admin')
def admin():
    if(session['logged_in']):
        return render_template('blog/admin.html')
    else:
        abort(401)
