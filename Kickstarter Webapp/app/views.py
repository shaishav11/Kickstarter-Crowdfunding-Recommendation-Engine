from app import app
from random import randint
from time import strftime
import csv
from flask import Flask, render_template, flash, request
import pandas as pd
from joblib import load
from app.demo import ReusableForm

def get_time():
    time = strftime("%Y-%m-%dT%H:%M")
    return time

def write_to_disk(name, email):
    data = open('file.log', 'a')
    timestamp = get_time()
    data.write('DateStamp={}, Name={}, Email={} \n'.format(timestamp, name, email))
    data.close()

def model_run(data):
    x_tst = pd.DataFrame(data)
    clf = load("rf_final.joblib")
    y_pred = clf.predict(x_tst)

    return y_pred

@app.route("/", methods=['GET', 'POST'])
def index():

    return render_template('index.html')

@app.route("/demo", methods=['GET', 'POST'])
def demo():
    
    form = ReusableForm(request.form)

    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        category = request.form['category']
        subcategory = request.form['subcategory']
        state = request.form['state']
        goal = request.form['goal']
        updates = request.form['updates']
        duration = request.form['duration']
        level = request.form['level']
        name = request.form['name']
        location = request.form['location']
        email = request.form['email']

        if form.validate():

            write_to_disk(name, email)

            data = {'updates': [int(updates)], 'subcategory': [int(subcategory)], 'state': [int(state)], 'goal': [float(goal)], 'levels': [int(level)],
                    'duration': [float(duration)]}
            
            y_pred = model_run(data)

            data_csv = [[title, description, category, subcategory, state, goal, updates, duration, level, y_pred]]
            with open('data_storage.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerows(data_csv)
                flash('Csv file written')
                f.close()

            if (y_pred == 1):
                flash('Congratulations, Your project might be successful with 80% accuracy')
            elif (y_pred == 0):
                flash('Sorry to inform you but your project might be a failure')

            else:
                flash('No record found...Try Again!')

        else:
            flash('Error: All Fields are Required')

    return render_template('demo.html', form=form)
