#!/bin/sh

pandoc -t beamer -o $1.pdf $1.md -V theme:Rochester -V colortheme:beetle
