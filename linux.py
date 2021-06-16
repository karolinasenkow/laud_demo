import os

# set path
path = os.getcwd()

# open sequence file
#file = open('new.txt').read()
#os.system('blastn -query ' + path + '\\query.txt' +  ' -subject ' + path + '\\subject.txt' + ' -max_target_seqs 10 -outfmt "10 qacc sacc pident send sstart length"')
os.system('blastn -query ' + path + '\\query.txt' +  ' -subject ' + path + '\\subject.txt')
os.system('del ' +  path + '\\query.txt')
os.system('del ' +  path + '\\subject.txt')
