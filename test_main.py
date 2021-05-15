from flask import Flask, render_template, flash, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (
                    StringField, 
                    SubmitField, 
                    RadioField,
                    SelectField,
                    BooleanField,
                    TextAreaField,
)

from wtforms.validators import DataRequired

app = Flask(__name__)
#basic security
app.config['SECRET_KEY'] = "mysecretkey"

class InfoForm(FlaskForm):
    #attribute
    breed = StringField("What Breed are you?", validators=[DataRequired()])
    neutered = BooleanField("Have you")
    submit = SubmitField("Submit")
    mood = RadioField("please choose your mood:",
                        choices=[
                                ('mode_one', 'Happy'),
                                ('mode_two', 'Excited')
                                ])   
    food_choice = SelectField("Pick your favorite food:", 
                                choices = [
                                    ('chi', 'Chicken'),
                                    ('bf', 'Beef'),
                                    ('apple', 'Red')
                                    ])
    feedback = TextAreaField()
    submit = SubmitField("submit")
class SimpleForm(FlaskForm):
    breed = StringField("What breed are you?")
    submit = SubmitField("Click Me.")

# @app.route('/', methods=["GET", "POST"])
# def index():
#     breed = False
#     form = InfoForm()
#     if form.validate_on_submit():
#         session['breed'] = form.breed.data
#         session['neutered'] = form.neutered.data
#         session['mood'] = form.mood.data
#         session['food'] = form.food_choice.data
#         session['feedback'] = form.feedback.data

#         breed = form.breed.data
#         form.breed.data = ""
#         return redirect(url_for("thankyou"))
#     return render_template('index.html', form=form, )

@app.route('/', methods=["GET", "POST"])
def index():
    form = SimpleForm()

    if form.validate_on_submit():
        """use flash function, template can use get_flashed_messages()"""
        session['breed'] = form.breed.data
        flash(f'You just changed your breed to : {session['breed']}')
        return redirect(url_for('index'))
    return render_template('index.html', form=form, )

@app.route('/thankyou')
def thankyou():
    return render_template("thankyou.html")

@app.route('/puppy/<name>')
def pup_name(name):
    return render_template('puppy.html',name=name)

if __name__ == '__main__':
    app.run(debug=True)