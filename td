#!/bin/bash

cd ${0%/*}/tdbs
python3 done_to_old.py

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
  migrate)
    python3 done_to_old.py "force"
    ;;
  refresh)
    ;;
  *)
    exit 0
    ;;
esac

./generate_set_wallpaper.sh
