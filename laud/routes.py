from flask import Flask, redirect, url_for, render_template, request, flash, request, abort
from laud import app, db, bcrypt, blast
import os, subprocess
from subprocess import Popen, PIPE
from subprocess import check_output
from laud.models import Metadata
from laud.forms import ChoiceForm
import secrets
from PIL import Image
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime
from sqlalchemy import and_


# set current path
path = os.getcwd()

@app.route("/", methods=["POST","GET"])
def sql():
    form = ChoiceForm()
    if form.validate_on_submit():
        sql_query = "SELECT taxa_name, subject_id FROM dataset WHERE taxa_name = '" + \
        form.species_result.data + "' AND subject_id = '" + form.subject_result.data + "';"

        cursor = db.session.execute(sql_query)
        row = ''
        returnString = str(row)
        row = cursor.fetchone()
        while row is not None:
            returnString += "\n" + str(row)
            row = cursor.fetchone()
        posts = Metadata.query.all()

        return render_template('sql_example.html', title='SQLExample', returnString=returnString,outString=posts)
    return render_template('choose_query.html', title='Choose Query', form=form, legend='Choose Query')

@app.route("/adv_sql", methods=["POST","GET"])
def adv_sql():
    if request.method == "POST":
        if request.form['post']:
            sql_query = request.form["post"]
            cursor = db.session.execute(sql_query)
            row = ''
            returnString = str(row)
            row = cursor.fetchone()
            while row is not None:
                returnString += "\n" + str(row)
                row = cursor.fetchone()
            posts = Metadata.query.all()
            return render_template('sql_example.html', title='SQLExample', returnString=returnString,outString=posts)
    return render_template("adv_sql.html")

@app.route("/blast", methods=["POST","GET"])
def home():
    if request.method == "POST":
        if request.form['post1']:
            with open(os.path.join(path + '\laud', 'query.txt'), 'w') as query: # query output file
                input1 = request.form["post1"]
                query.write(input1)
        if request.form["radiobutton"]:
            option = request.form['radiobutton'] # get value of radio button
            if option == 'option1':
                return redirect(url_for("command_server0", command=command_server0))
            else:
                return redirect(url_for("command_server1", command=command_server1))
    else:
        return render_template("index.html")

def run_command(command):
    return subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read()

@app.route('/command0/<command>')
def command_server0(command):
    return run_command('python ' + path + '/laud/blast.py -d 0')

@app.route('/command1/<command>')
def command_server1(command):
    return run_command('python ' + path + '/laud/blast.py -d 1')

