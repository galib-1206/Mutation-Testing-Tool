# coding=utf-8

from flask_wtf import FlaskForm
import wtforms
from wtforms.validators import DataRequired, Optional


class CreateProjectForm(FlaskForm):
    name = wtforms.StringField('name', validators=[DataRequired()])
    workdir = wtforms.StringField('workdir', validators=[DataRequired()])
    build_command ="make"
    test_command = "ctest"
    test_timeout = wtforms.FloatField('test_timeout', validators=[Optional()])


class CreateFileForm(FlaskForm):
    filename = wtforms.StringField('filename', validators=[DataRequired()])


class SetConfirmationForm(FlaskForm):
    confirmation = wtforms.RadioField('comfirmation', choices=[('unknown', 'unknown'),
                                                               ('confirmed', 'confirmed'),
                                                               ('ignored', 'ignored')])
