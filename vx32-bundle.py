import sys,shlex

def parsefile(f, outf):
  j=open(f).readlines()
  for line in j:
    if line.strip().startswith('include'):
      parsefile(shlex.split(line)[1], outf)
    else:
      outf.write(line)

if len(sys.argv)<2:
  print("Usage: vx32-bundle.py infile.bas outfile.bas")
outf=open(sys.argv[2], "wt")
parsefile(sys.argv[1], outf)
  
