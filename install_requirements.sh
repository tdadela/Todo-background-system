#!/bin/sh
packages='python3 texlive poppler-utils feh'
if   [ -x "$(command -v apt)" ];    then sudo apt install $packages
elif [ -x "$(command -v dnf)" ];    then sudo dnf install $packages
elif [ -x "$(command -v yum)" ];    then sudo yum install $packages
elif [ -x "$(command -v apk)" ];    then sudo apk add --no-cache $packages
elif [ -x "$(command -v zypper)" ]; then sudo zypper install $packages
elif [ -x "$(command -v pacman)" ]; then sudo pacman -S poppler python3 texlive feh
else echo "You need to install: $packages manually." >&2
fi
