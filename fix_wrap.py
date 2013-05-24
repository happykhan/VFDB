import sys
import textwrap


with open(sys.argv[1]) as fin:
    lines = fin.readlines()

for i in range(0, len(lines)):
    if lines[i].startswith('>'):
        print lines[i].strip()+" ["+sys.argv[1].split('.')[0].replace("_", " ")+"]"
        pos = i+1
        cur = ''
        try:
            while not lines[pos].startswith('>'):
                cur = cur+lines[pos].strip()
                pos = pos+1
        except IndexError:
            pass
        new = textwrap.wrap(cur.upper(), 80)
        for e in new:
            print e

