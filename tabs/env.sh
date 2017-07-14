ls | xargs sed -i '1 a\\\begin\{samepage\}' 
ls | xargs sed -i '$a\\\end\{samepage\}'
