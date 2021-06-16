from flask import Flask, redirect, url_for, render_template, request
import os, subprocess
from subprocess import Popen, PIPE
from subprocess import check_output
import linux

# set current path
path = os.getcwd()

# output file
#query = open('query.txt', 'w')
#subject = open('subject.txt', 'w')

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def home():
    if request.method == "POST":
        with open('query.txt', 'w') as query:
            input1 = request.form["post1"]
            query.write(input1)
        with open('subject.txt', 'w') as subject:
            input2 = request.form["post2"]
            subject.write(input2)
        return redirect(url_for("command_server", command=command_server))
    else:
        return render_template("index.html")

#@app.route("/<usr>", methods=('GET', 'POST'))
#def user(usr):
#    output.write('string ' + str(usr))
#    return f"<h1>{usr}<h1>"

#@app.route('/', methods=('GET', 'POST'))
#def hello():
#    os.system('mkdir my_directory')
#    return os.system("ls")


def run_command(command):
    return subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read()

@app.route('/<command>')
def command_server(command):
    return run_command('python ' + path + '/linux.py')

#@app.route('/<command>')
#def read_input(command):
#    os.system('echo hello world!!!')


if __name__ == "__main__":
    app.run(debug=True)
