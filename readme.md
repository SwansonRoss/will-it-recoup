# Project Overview
will-it-recoup is a web application that predicts whether or not a movie will make back it's budget.  
  
The predictions are made by querying two classifier models, one using AdaBoost and the other using Gradient Boosting. Originally, a third bagging classifier was used, but this file was too large to upload to GitHub, so for now it has been removed.  
  
# How does it work  
To query the model, the user inputs the director, producer, four leading actors (and their genders), the genre, the budget, and the production company. Once these inputs are submitted, the flask server calls the will-it-recoup function, which queries each models and returns the total number of yes votes, as well as an array of each vote.  
  
A page is then generated, telling the user what the model predicted and how each classifier voted.

# What's included in this repo  
Below is a quick tour of the files and directories in this repo:  
+ app.py  
    - This file handles routing and calling the functions in the model.py file  
+ data/  
    - These files are used in other places, but are mostly large lists, so I wanted to abstract them out into thier own files
    - columns.py contains a list of all the columns in the models. This is used to build queries.
    - all other files contain tuples used to create choices for the form field
+ models/
    - ab_model.pkl - pickled AdaBoost model
    - bagging_model.pkl - pickled bagging model (currently gitignored because it is too large)
    - gb_model.pkl - pickled Gradient Boosting model
    - model.py - contains functions to query the model: queryBuilder - reformats user input to the format the models accept, voteRecoup - queries the models and totals the votes, willItRecoup - interacts with the router, taking in inputs and returning outputs.
+ static/
    - This directory contains the css styles and some json files that are as of now, unused.
    - style.css - css file containing styles used in the site
    - various JSON files, todo: change dropdown fields to forced choice textfields, automatically fill in correct gender for actors
+ templates/
    - This directory holds the various HTML files 
    - forms/form.html - contains the form used to make queries
    - template-parts/ - contains re-usable html elements
    - _formhelpers.html - handles errors with form submission
    - index.html - home page
    - will_it.html - results page
# How to start the flask app
> $ export FLASK_APP=app.py  
> $ export FLASK_ENV=development  
> $ flask run  


