import os

# set path
path = os.getcwd()
path = path + '/laud'

def _16S():
    os.system('makeblastdb -in ' + path + '/16S.fasta -out ' + path + '/16S -title 16S -dbtype nucl')
    os.system('blastn -query ' + path + '/query.txt -db ' + path + '/16S > ' + path + '/16S_blast_result.txt')

def WGS():
    os.system('makeblastdb -in ' + path + '/wgs.fasta -out ' + path + '/wgs -title wgs -dbtype nucl')
    os.system('blastn -query ' + path + '/query.txt -db ' + path + '/wgs > ' + path + '/wgs_blast_result.txt')

def assembled_contigs():
    os.system('makeblastdb -in ' + path + '/assembled_contigs.fasta -out ' + path + '/assembled_contigs -title assembled_contigs -dbtype nucl')
    os.system('blastn -query ' + path + '/query.txt -db ' + path + '/assembled_contigs > ' + path + '/assembled_contig_blast_result.txt')

if __name__ == '__main__':
    import argparse
    # declare args
    args = argparse.Namespace

    parser = argparse.ArgumentParser(description='Choose database.') 
    parser.add_argument('--download','-d', type=int, required=False, dest="download",help='0 for 16S, 1 for whole genome sequencing data, 2 for assembled contigs')

    args = parser.parse_args()

    choice = args.download
    if choice == 0:
        _16S()

    elif choice == 1:
        WGS()

    elif choice == 2:
        assembled_contigs()

    else:
        print("0 for 16S, 1 for whole genome sequencing data, 2 for assembled contigs")
