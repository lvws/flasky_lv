from flask_wtf import Form

class NameForm(Form):
    name = StringField('what your name?',validators=[Required()])
    submit = SubmitField('submit')
    