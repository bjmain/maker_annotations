# This script creates and directory for each fasta file in this directory and sets up the directory to run maker.

import glob
import os

chunks = glob.glob("chnk_*.fa")
for chunk in chunks:
    name = chunk.strip(".fa")
    os.system("mkdir %s" % (name))
    os.system("mv %s %s" % (chunk, name))
    os.system("ln -s /home/path_to/pacbio/annotations/ctark1_repeatmodeler_consensi.fa.classified %s" % (name))
    os.system("ln -s /home/path_to/pacbio/annotations/ctar_transcriptome_GFDL01.1.fsa_nt %s" % (name))
    os.system("ln -s /home/path_to/pacbio/annotations/Culex-quinquefasciatus-Johannesburg_PEPTIDES_CpipJ2.4.fa %s" % (name))
    # The below maker_* files are created by the command: maker -CTL
    os.system("cp /home/path_to/maker_* %s" % (name))


opts_files = glob.glob("chnk_*/maker_opts.ctl")
for f in opts_files:
    filename = f.split("/")[0]
    new_chnk = "/home/path_to/" + filename + "/" + filename + ".fa"
    os.system("sed -i 's#/home/path_to/chnk1.fa#%s#g' %s" % (new_chnk, f))
