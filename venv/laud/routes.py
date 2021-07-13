from flask import Flask, redirect, url_for, render_template, request, flash, request, abort, session, send_file
from laud import app, db, bcrypt, blast
import os, subprocess
from subprocess import Popen, PIPE
from subprocess import check_output
from laud.models import Metadata, _16S
from laud.forms import ChoiceForm, _16SID, ChiForm
import secrets
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime
from sqlalchemy import and_
import csv


# set current path
path = os.getcwd()

@app.route("/", methods = ["GET", "POST"])
def about():
    if request.method == "POST":
        return redirect(url_for("sql"))
    return render_template("about.html")

@app.route("/team")
def team():
    return render_template("team.html")


@app.route("/sql", methods=["POST","GET"])
def sql():
    form = ChoiceForm()
    if form.validate_on_submit():
        sql_query = "SELECT * FROM dataset WHERE taxa_name like '" + \
                form.species_result.data + "' AND event like '" + form.event_result.data + "' AND subject_id like '" + \
                form.subject_result.data + "';"

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
            with open(os.path.join(path + '/laud', 'query.txt'), 'w') as query: # query output file
                input1 = request.form["post1"]
                query.write(input1)
        if request.form["radiobutton"]:
            option = request.form['radiobutton'] # get value of radio button
            if option == 'option0':
                return redirect(url_for("command_server0", command=command_server0))
            elif option == 'option1':
                return redirect(url_for("command_server1", command=command_server1))
            elif option == 'option2':
                return redirect(url_for("command_server2", command=command_server2))
    else:
        return render_template("index.html")

@app.route("/16S", methods=["POST", "GET"])
def _16S_blast_id():
    form = _16SID()
    if form.validate_on_submit():
        sql_query = "SELECT subject_id FROM 16s_to_subj_id WHERE FASTA_ID = '" + form.FASTA_ID.data + "';"
        cursor = db.session.execute(sql_query)
        row = ''
        returnString = str(row)
        row = cursor.fetchone()
        while row is not None:
            returnString += "\n" + str(row)
            row = cursor.fetchone()
        posts = _16S.query.all()
        return render_template('sql_example.html', title='SQLExample', returnString=returnString,outString=posts)
    return render_template("16s_to_sub_id.html", title='16S Subject ID', form=form, legend='16S Subject ID')


@app.route("/chisq_ind", methods = ["POST", "GET"])
def chisq_ind():
    form = ChiForm()
    if form.validate_on_submit():
        session["species"] = form.species_result.data
        session["var"] = form.var.data
        
        sql_query = 'select * from dataset where subject_id like "'+form.subject_filter.data+'" and sample_id like "'+form.sample_filter.data+'" and event like "'+form.event_filter.data+'" and taxa_type like "'+form.type_filter.data+'" and cure_status like "'+form.cure_filter.data+'" and taxa_name like "'+form.species_result.data+'" and taxa_count = "0" union all select * from dataset where subject_id like "'+form.subject_filter.data+'" and sample_id like "'+form.sample_filter.data+'" and event like "'+form.event_filter.data+'" and taxa_type like "'+form.type_filter.data+'" and cure_status like "'+form.cure_filter.data+'" and taxa_name like "'+form.species_result.data+'" and taxa_count = "0";'
        
        connection = db.session.connection()
        posts = connection.execute(sql_query)

        with open("laud/df.csv", "w+") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = ["subject_id", "sample_id", "event", "taxa_type", "taxa_name", "taxa_count", "cure_status"])
            writer.writeheader()
            for row in posts:
                row_data = {
                        "subject_id": row.subject_id,
                        "sample_id": row.sample_id,
                        "event": row.event,
                        "taxa_type": row.taxa_type,
                        "taxa_name": row.taxa_name,
                        "taxa_count": row.taxa_count,
                        "cure_status": row.cure_status,
                        }
                writer.writerow(row_data)
        return redirect(url_for("command_server3", command = command_server3))
    return render_template("chisq_ind.html", title = "Chi-Square Test of Independence", form = form, legend = "Chi-Square Test of Independence")

@app.route("/results")
def results():
    return render_template("results.html", content = session["content"])


@app.route("/test", methods = ["POST", "GET"])
def test():
    return redirect(url_for("command_server4", command = command_server4))


def run_command(command):
    return subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read()

@app.route('/command0/<command>')
def command_server0(command):
    run_command('python3 ' + path + '/laud/blast.py -d 0')
    with open(path + "/laud/16S_blast_result.txt","r") as file:
        content = file.read()
    return render_template("blast_results.html", content = content)

@app.route('/command1/<command>')
def command_server1(command):
    run_command('python3 ' + path + '/laud/blast.py -d 1')
    with open(path + "/laud/wgs_blast_result.txt","r") as file:
        content = file.read()
    return render_template("blast_results.html", content = content)

@app.route('/command2/<command>')
def command_server2(command):
    run_command('python3 ' + path + '/laud/blast.py -d 2')
    with open(path + "/laud/assembled_contig_blast_result.txt","r") as file:
        content = file.read()
    return render_template("blast_results.html", content = content)

@app.route("/command3/<command>")
def command_server3(command):
    run_command("python3 " + path + "/laud/chisq_ind.py " + session["species"] + " " + session["var"])
    with open(path + "/result.txt", "r") as file:
        session["content"] = file.read()
    return redirect(url_for("results"))


@app.route("/command4/<command>")
def command_server4(command):
    return run_command("python3 " + path + "/laud/test.py")


