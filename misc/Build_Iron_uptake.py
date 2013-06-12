# Builds a VF DB for Mobley et. al. using KEGG queries
# Mitchell Stanton-Cook

import sys
import os
import re
import textwrap


#BASE = "http://www.genome.jp/dbget-bin/www_bget?ecc:"
BASE = "http://www.genome.jp/dbget-bin/www_bget?"


out = open("Iron_uptake.fa", "w")

with open("Fe_uptake.csv") as fin:
    lines = fin.readlines()[1:]

for l in lines:
    all = l.strip().split(',')
    if all[-1] != '*':
        os.system('wget "'+BASE+all[-1]+":"+all[0]+'" --output-document='+all[0]+'.html')
        header = '>'
        # Handle locus tags
        with open(all[0]+'.html') as html_in:
            html_lines = html_in.readlines()
        lt = ''
        for e in html_lines:
            if e.find("<title>") != -1:
                lt = e.split(": ")[-1].strip("</title>\n")
                header = header+lt
                break
        # Handle gene names 
        pos = 0
        for idx, e in enumerate(html_lines):
            if e.find("<nobr>Gene name</nobr>") != -1:
                pos = idx+1
                break
        if pos == 0:
            header = header+", "+all[1]
        else:
            gene = html_lines[pos].split('overflow-y:hidden">')[-1][:-5].strip()
            header = header+", "+gene
        # Handle definition
        pos = 0
        for idx, e in enumerate(html_lines):
            if e.find("<nobr>Definition</nobr>") != -1:
                pos = idx+1
                break
        if pos == 0:
            header = header+", "
        else:
            defn = html_lines[pos].split('overflow-y:hidden">')[-1][:-5].strip()
            header = header+", "+(defn.replace(',', ';'))
        pos = 0
        for idx, e in enumerate(html_lines):
            if e.find("<nobr>Organism</nobr>") != -1:
                pos = idx+1
                break
        if pos == 0:
            header = header+", "
        else:
            org = html_lines[pos].split('&nbsp;')[-1][:-5].strip()
            header = header+", "+org
        if header.count(",") != 3:
            print header.count(","), header
            print "Exited", header
            print sys.exit(0)
        out.write(header+" [Iron uptake]\n")
        # Get the sequence...
        pos = 0
        for idx, e in enumerate(html_lines):
            if e.find("<nobr>NT seq</nobr>") != -1:
                pos = idx+2
                break
        seq = ''
        while html_lines[pos].find("</table>") == -1:
            if html_lines[pos] == '\n':
                pass
            else:
                x = re.sub('<[^<]+?>', '', html_lines[pos]).upper().strip()
                seq = seq+x
            pos = pos +1
        new = textwrap.wrap(seq, 80)
        for e in new:
            out.write(e+'\n')
