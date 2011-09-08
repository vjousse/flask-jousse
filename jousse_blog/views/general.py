from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

mod = Blueprint('general', __name__)


@mod.route('/', defaults={'page': 'index'})
@mod.route('/<page>')
def show(page):
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)
