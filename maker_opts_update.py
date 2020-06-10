import glob
import os

# This script update the fasta file in every maker_opts.ctl file

opts_files = glob.glob("chnk_*/maker_opts.ctl")
for f in opts_files:
    filename = f.split("/")[0]
    new_chnk = "/home/bmain/tarsalis/polished_Ctar_2020-05-23/" + filename + "/" + filename + ".fa"
    os.system("sed -i 's#/home/bmain/tarsalis/pacbio/male_knwr/fastq/racon2_Mt_annotations/chnk1/chnk1/chnk1.fa#%s#g' %s" % (new_chnk, f))
    #print("sed 's#/home/bmain/tarsalis/pacbio/male_knwr/fastq/racon2_Mt_annotations/chnk1/chnk1/chnk1.fa#%s#g' %s" % (new_chnk, f))
    #break
    #/home/bmain/tarsalis/pacbio/male_knwr/fastq/racon2_Mt_annotations/chnk1/chnk1/chnk1.fa
