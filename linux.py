import os

# set path
path = os.getcwd()

os.system('blastn -query ' + path + '\\query.txt' +  ' -subject ' + path + '\\subject.txt')
