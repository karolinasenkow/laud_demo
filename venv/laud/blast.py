import os

# set path
path = os.getcwd()
path = path + '\\laud'

def test0():
    os.system('makeblastdb -in ' + path + '\\16S_db.fasta -out ' + path + '\\16S -title 16S -dbtype nucl')
    os.system('blastn -query ' + path + '\\query.txt -db ' + path + '\\16S')
    os.system('blastn -query ' + path + '\\query.txt -db ' + path + '\\16S -outfmt "6 sacc pident length qstart qend sstart send bitscore evalue stitle"')

def test1():
    os.system('makeblastdb -in ' + path + '\\bacterial_genome.fna -out ' + path + '\\bacteria -title bacteria -dbtype nucl')
    os.system('blastn -query ' + path + '\\query.txt -db ' + path + '\\bacteria')
    os.system('blastn -query ' + path + '\\query.txt -db ' + path + '\\bacteria -outfmt "6 sacc pident length qstart qend sstart send bitscore evalue stitle"')


if __name__ == '__main__':
    import argparse
    # declare args
    args = argparse.Namespace

    parser = argparse.ArgumentParser(description='Choose database.') 
    parser.add_argument('--download','-d', type=int, required=False, dest="download",help='0 for 16S, 1 for bacterial genome data')

    args = parser.parse_args()

    choice = args.download
    if choice == 0:
        test0()

    elif choice == 1:
        test1()
    else:
        print("Please choose 0 for download and 1 for test data")

#os.system('blastn -query ' + path + '\\query.txt' +  ' -subject ' + path + '\\subject.txt')
