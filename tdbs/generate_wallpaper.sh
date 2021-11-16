#!/bin/sh
python3 tex_input.py
cd ../latex
pdflatex background.tex >pdflatex.log
if [ -x "$(command -v xdpyinfo)" ]; then
    width=`xdpyinfo | grep dimensions | awk '{print $2}' | awk -Fx '{print $1}'`
    height=`xdpyinfo | grep dimensions | awk '{print $2}' | awk -Fx '{print $2}'`
else
    width=1920
    heigh=1080
fi
pdftoppm -scale-to-x ${width} -scale-to-y ${height} background.pdf bc -png
feh --bg-fill bc-1.png
