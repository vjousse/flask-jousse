from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

mod = Blueprint('blog', __name__)


@mod.route('/')
def index():
    try:
        return render_template('blog/index.html')
    except TemplateNotFound:
        abort(404)
