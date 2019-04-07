#!/bin/bash -ex

#INPUTS="ogniskowe.txt akustyczne.txt elektryczne.txt mix.txt tabulatures.txt"
INPUTS="ogniskowe.txt"

##################################

for INPUT in $INPUTS
do
OUTPUT_LY=`echo $INPUT | sed 's/txt/ly/g'`
OUTPUT_TEX=`echo $INPUT | sed 's/txt/tex/g'`
echo $OUTPUT_FILE
OUTPUT="output/$OUTPUT_LY"
LISTS="lists"

touch ${OUTPUT}
cat parts/start.tex > ${OUTPUT}


FILENAMES=`cat ${LISTS}/${INPUT} | sort | sed -e '/^$/d' | awk '{print "tabs/" $1 ".ly"}'`

for filename in $FILENAMES; do
  cat $filename
done >> ${OUTPUT}

cat parts/end.tex >> ${OUTPUT}

lilypond-book --pdf --format=latex -lily-output-dir=output ${OUTPUT}
pdflatex -interaction nonstopmode  -file-line-error  $OUTPUT_TEX || true
pdflatex -interaction nonstopmode  -file-line-error  $OUTPUT_TEX || true

rm *.ly *.dep *.aux *.log *.toc
done
