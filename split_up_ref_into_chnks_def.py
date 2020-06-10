# This script inputs a fasta file and breaks it up into smaller fasta files by the number of sequences chosen by the chunk_size variable. This facilitates parallelizing the maker annotation pipeline.

chunk_size = 20

contig_list=[]

group=0
for line in open("m_knwr_snps_consensus.fa"):
	i=line.strip().split()
	if line[0]==">":
                contig=i[0].strip(">")
                contig_list.append(contig)
                if len(contig_list)%chunk_size==1:
                    group+=1
                    outfile_name = "chnk"+"_"+str(group)+".fa"
                    outfile = open(outfile_name, 'w')
                outfile.write(line)
                continue
        else:
            outfile.write(line)

