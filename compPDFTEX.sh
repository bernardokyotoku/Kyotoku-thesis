#!/bin/bash
d=s/FDL-setup/$1/g
cat frame.tex|sed $d >temp.tex
pdflatex temp
rm temp.tex
rm temp.aux
rm temp.log
rm temp.out
open temp.pdf
