# maker_annotations
These scripts enable running maker in parallel on your genome.
1) split_up_ref_into_chnks_def.py: Split up your genome into bite-size pieces by number of contigs
2) directory_setup.py: Place each fasta chunk in its own directory and set it up to run maker
3) maker_opts_update.py: This script customizes each maker directory to run the associated fasta chunk (smaller fasta file)
4) run_maker1.sh: This is a template shell script to run maker with SLURM
5) sh_setup.py: Make a shell script for each chunk, then submit each one using a bash for loop.
