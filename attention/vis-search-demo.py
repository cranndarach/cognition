#!/usr/bin/env python3

import random as rd


class Stimulus:
    def __init__(self, letter, color):
        self.letter = letter
        self.color = color

class VisSearch:
    def __init__(self, target_letter, target_color, distractor_letters,
                 distractor_colors, display_sizes):
        self.target_letter = target_letter
        self.target_color = target_color
        self.distractor_colors = distractor_colors
        self.distractor_letters = distractor_letters
        self.display_sizes = display_sizes

    def make_array(self):
        target = Stimulus(self.target_letter, self.target_color)
        dist_colors = None # come back here
