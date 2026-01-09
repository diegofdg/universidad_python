from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

class CursoForm(FlaskForm):
    nombre = StringField("Nombre del Curso", validators=[
        DataRequired(),
        Length(min=3, max=100, message="El nombre debe tener entre 3 y 100 caracteres")
    ])
    instructor = StringField("Instructor", validators=[
        DataRequired(),
        Length(min=3, max=100, message="El nombre del instructor debe tener entre 3 y 100 caracteres")
    ])
    duracion = DecimalField("Duración (horas)", validators=[
        DataRequired(),
        NumberRange(min=1, max=999, message="Debe ser un número entre 1 y 999 horas")
    ])
    submit = SubmitField("Guardar")
