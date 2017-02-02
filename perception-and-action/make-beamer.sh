#!/bin/bash

pandoc -t beamer -o early-vision-slides.pdf early-vision-slides.md -V theme:Rochester -V colortheme:beetle
