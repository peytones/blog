from datetime import datetime
from flask import render_template, session, redirect, url_for
from .forms import NameForm
from . import main

@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        return redirect(url_for('.index'))
    return render_template('base.html', form=form, name=session.get('name'), known=session.get('known', False))
