import glob
import os

chunks = glob.glob("chnk_*/chnk_*fa")

for chunk in chunks:
    number = chunk.strip("chnk_").strip(".fa")
    name = "run_maker" + chunk + ".sh"
    outfile = open(name, 'w')
    for line in open("run_maker1.sh"):
        i = line.strip().split()
        if "maker1" in line:
            sample_name = "maker"+number
            line = line.replace("maker1",sample_name)
        if "cd" in line:
            if i[0] == "cd":
                directory = i[1] + chunk
                outfile.write(" ".join([i[0],directory]))
                outfile.write("\n")
                continue

        outfile.write(line)
        
