#!/usr/local/bin/python3.8

import sys
import random
import glob
import subprocess as sub

# grab the first argument:
path = sys.argv[1]

# run the command
command = ['ls', path]
completed_pro = sub.run(command, universal_newlines=True, stdout=sub.PIPE)
stdout = completed_pro.stdout
files = stdout.split('\n')

# another way of making the list is -- glob.glob(path + "*")

# print the random file
rs = random.choice(files)
print("Random: %s" % rs)
