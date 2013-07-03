import sys
import textwrap


def chunk(l, n=500):
    """ 
    Yield successive n-sized chunks from l.
    """
    return [l[i:i+n] for i in range(0, len(l), n)]

with open(sys.argv[1]) as fin:
    lines = fin.readlines()

for i in range(0, len(lines)):
    if lines[i].startswith('>'):
        counter = 1
        name = lines[i].strip()[1:]
        pos = i+1
        cur = ''
        try:
            while not lines[pos].startswith('>'):
                cur = cur+lines[pos].strip()
                pos = pos+1
        except IndexError:
            pass
        cur = cur.replace('N','')
        chunked = chunk(cur)
        for index, c in enumerate(chunked):
            print '>'+name+"_"+str(index+1)+", "+name+"_"+str(index+1)+", , Ec958 ["+name+"]"
            new = textwrap.wrap(c.upper(), 80)
            for e in new:
                print e

