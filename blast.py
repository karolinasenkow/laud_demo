import os
import argparse

# set path
path = os.getcwd()

# declare args
args = argparse.Namespace

parser = argparse.ArgumentParser(description='Choose database.') 
parser.add_argument('--download','-d', type=int, required=False, dest="download",help='0 for 16S, 1 for bacterial genome data')

args = parser.parse_args()

def test0():
    print('test0 data')

def test1():
    print('test1 data')

if __name__ == '__main__':
    choice = args.download
    if choice == 0:
        test0()

    elif choice == 1:
        test1()
    else:
        print("Please choose 0 for download and 1 for test data")

#os.system('blastn -query ' + path + '\\query.txt' +  ' -subject ' + path + '\\subject.txt')
