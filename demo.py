from flask import Flask, redirect, url_for, render_template, request
import os, subprocess
from subprocess import Popen, PIPE
from subprocess import check_output
import linux

# set current path
path = os.getcwd()


app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def home():
    if request.method == "POST":
        with open('query.txt', 'w') as query: # query output file
            input1 = request.form["post1"]
            query.write(input1)
        with open('subject.txt', 'w') as subject: # subject output file
            input2 = request.form["post2"]
            subject.write(input2)
        return redirect(url_for("command_server", command=command_server))
    else:
        return render_template("index.html")


def run_command(command):
    return subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read()

@app.route('/<command>')
def command_server(command):
    return run_command('python ' + path + '/blast.py')



if __name__ == "__main__":
    app.run(debug=True)
