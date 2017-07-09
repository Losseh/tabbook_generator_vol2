#!/bin/bash

while read line; do
  IFS="\t " read -a limits <<< "$line"
  echo "start: ${limits[0]}"
  echo "end: ${limits[1]}"
  START="${limits[0]}"
  END="${limits[1]}"
  TITLE=`sed -n "${START}p" output.tex | iconv -f utf-8 -t ascii//translit`
  TITLE=`echo $TITLE | cut -d"{" -f 2 | sed 's/}//g' | tr '[:upper:]' '[:lower:]' | sed 's/\ /\_/g'`
  TITLE=${TITLE}.tex
  sed -n "${START},${END}p" output.tex > files/$TITLE
done < sections_limits1.txt

# get start and end of file
# read name of file from the start line
# put the section between start and end into the [file]

