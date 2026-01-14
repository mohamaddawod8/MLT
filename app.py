from flask import Flask, render_template, request, session, redirect, url_for
import pandas as pd
import os
from src.data_cleaning import run_cleaning
from src.ml_model import get_feature_importance
from src.recommender import get_recommendations

app = Flask(__name__)
app.secret_key = "super_secret_key"

df = run_cleaning('Data/data_all.xltx')
weights = get_feature_importance(df)

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'current_path' not in session:
        session['current_path'] = []
    
    if request.method == 'POST' and 'country' in request.form:
        session['selected_country'] = request.form.get('country')
        session['selected_solution'] = request.form.get('solution')

    country = session.get('selected_country', sorted(df['Country'].unique())[0])
    solution = session.get('selected_solution', sorted(df['Solution'].unique())[0])

    c, s, cs, dynamic = get_recommendations(df, weights, country, solution, session['current_path'])

    countries = sorted(df['Country'].unique())
    solutions = sorted(df['Solution'].unique())
    all_actions = sorted(df['Action'].unique())

    return render_template('index.html', 
                           countries=countries, 
                           solutions=solutions, 
                           all_actions=all_actions,
                           selected_country=country, 
                           selected_solution=solution,
                           by_country=c[:4], 
                           by_solution=s[:4], 
                           by_both=cs[:4],
                           dynamic=dynamic[:4], 
                           current_path=session['current_path'])

@app.route('/add_action', methods=['POST'])
def add_action():
    action = request.form.get('action_to_add')
    if action:
        path = session.get('current_path', [])
        path.append(action)
        session['current_path'] = path
        session.modified = True
    return redirect(url_for('index'))

@app.route('/reset', methods=['POST'])
def reset():
    session['current_path'] = []
    session.pop('selected_country', None)
    session.pop('selected_solution', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)