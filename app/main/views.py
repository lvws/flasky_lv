from datetime import datetime
from flask import render_template,session,redirect,url_for,current_app
from . import main
from .forms import NameForm
from .. import db
from ..models import User
from ..email import send_email

@main.route('/',methods=['GET','POST'])
def index():
    form = NameForm
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.add(user)
            db.commit()
            session['known'] = False
            if current_app['FLASK_ADMIN']:
                send_em