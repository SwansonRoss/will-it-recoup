from flask import Flask, render_template, request
from wtforms import Form, SelectField, validators, SelectMultipleField, widgets
from data import choices, actor1, actor2, actor3, actor4, directors, producers, prodCos
from models import model

app = Flask(__name__)

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class MovieForm(Form):
        director =  SelectField(label='Director', choices=directors.values)
        producer =  SelectField(label='producer', choices=producers.values)
        act1 = SelectField(label='Actor 1', choices=actor1.values)
        act1g = SelectField(label='gender', choices=choices.GENDERS)
        act2 = SelectField(label='Actor 2', choices=actor2.values)
        act2g = SelectField(label='gender', choices=choices.GENDERS)
        act3 = SelectField(label='Actor 3', choices=actor3.values)
        act3g = SelectField(label='gender', choices=choices.GENDERS)
        act4 = SelectField(label='Actor 4', choices=actor4.values)
        act4g = SelectField(label='gender', choices=choices.GENDERS)
        genres = MultiCheckboxField(label='Genres', choices=choices.GENRES)
        budget =  SelectField(label='Budget', choices=choices.BUDGET)
        prodCo = SelectField(label='Production Company', choices=prodCos.values)
        

@app.route('/')
def index():
    form = MovieForm(request.form)
    return render_template('index.html', form=form)

@app.route('/will-it', methods=['POST'])
def willIt():
    form = MovieForm(request.form)
    if request.method == 'POST' and form.validate():
        fields = [[request.form['genres']], request.form['director'], request.form['producer'], request.form['act1'], request.form['act1g'], request.form['act2'], request.form['act2g'], request.form['act3'], request.form['act3g'], request.form['act4'], request.form['act4g'], request.form['prodCo'], request.form['budget']]
        total, votes = model.willItRecoup(fields)
        return render_template('will_it.html', total=total, votes=votes)
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)