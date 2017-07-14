#!/bin/bash -ex

OUTPUT="glued.ly"
touch ${OUTPUT}
cat start.tex > ${OUTPUT}
cat list.txt | sort | awk '{print "tabs/" $1 ".ly"}'| xargs cat >> ${OUTPUT}
cat end.tex >> ${OUTPUT}

lilypond-book --pdf --format=latex -lily-output-dir=lilyfiles glued.ly
pdflatex -interaction nonstopmode  -file-line-error  glued.tex
