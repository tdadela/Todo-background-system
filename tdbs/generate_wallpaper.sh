#!/bin/sh
python3 tex_input.py
cd ../latex
pdflatex background.tex >pdflatex.log
pdftoppm -scale-to-x 1920 -scale-to-y 1080 background.pdf bc -png
feh --bg-fill bc-1.png
