#!/bin/sh

# In a terminal, run `bash make-beamer.sh filename-without-extension`
# So for this, I would run `bash make-beamer.sh tg80slides`
pandoc -t beamer -o $1.pdf $1.md -V theme:Rochester -V colortheme:beetle
