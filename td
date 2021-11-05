#!/bin/bash
cd ${0%/*}/tdbs
echo "${@}"
echo $1
case $1 in
  add) 
    python3 add.py "${@:2}"
    ;;
  finish | done)
    python3 finish.py "${@:2}"
    ;;
  remove)
    python3 finish.py "${@:2}" "remove"
    ;;
  *)
    exit 0
    ;;
esac

./generate_set_wallpaper.sh
