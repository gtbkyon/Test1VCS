import sys
import os
cwd = os.getcwd()

sys.path.append(cwd)

from generate_list import printIt

for x in range(1000):
    printIt()