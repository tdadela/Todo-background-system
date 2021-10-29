#!/bin/sh
cd latex
pdflatex background.tex
pdftoppm -scale-to-x 1920 -scale-to-y 1080 background.pdf bc.png -png
feh --bg-fill bc.png-1.png
