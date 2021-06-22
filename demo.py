from flask import Flask, redirect, url_for, render_template, request
import os, subprocess
from subprocess import Popen, PIPE
from subprocess import check_output
import blast

# set current path
path = os.getcwd()


app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def home():
    if request.method == "POST":
        if request.form['post1']:
            with open('query.txt', 'w') as query: # query output file
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
    return run_command('python ' + path + '/blast.py -d 0')

@app.route('/command1/<command>')
def command_server1(command):
    return run_command('python ' + path + '/blast.py -d 1')



if __name__ == "__main__":
    app.run(debug=True)
