#!/usr/bin/env python3

import random as rd


###################
# Parts of Speech #
###################

def conj():
    return ran(["and", "or"])


def coord_conj():
    return ran([conj(), "but", "because", "though", "yet", "while", "whereas"])


def det():
    return ran(["the", "a", "my", "her", "his", "their", "this", "that",
                "every", "everyone's", "{}'s".format(proper_noun())])


def noun():
    return ran(["mother", "father", "brother", "sister", "aunt", "uncle"])


def proper_noun():
    return ran(["Anna", "David"])


def helping_verb():
    return ran(["is"])


def adjective():
    adjs = ["nice", "tall"]
    return ran(adjs + ["{} {} {}".format(ran(adjs), conj(), ran(adjs))])


def prep():
    return ran(["of"])


#################
# Phrases, etc. #
#################


def verb_phrase():
    return ran(["{} {}".format(helping_verb(), adjective()),
                "{} {}".format(helping_verb(), noun_phrase())])


def noun_phrase():
    return ran([types_np(),
                "{} {} {}".format(types_np(), conj(), types_np()),
                "{} {} {}".format(types_np(), prep(), types_np()),
                ])


def clause():
    return "{} {}".format(noun_phrase(), verb_phrase())


def sentence():
    out = ran(["{}.".format(clause()),
               "{}, {} {}.".format(clause(), coord_conj(), clause())])
    print(out)
    return out


def main():
    sentence()


####################
# Helper Functions #
####################


def ran(spl):
    return rd.choice(spl)


def nominal():
    return ran([noun(), "{} {}".format(adjective(), noun())])


def combo_np():
    return "{} {}".format(det(), nominal())


def types_np():
    return ran([proper_noun(), combo_np()])


###################
# Run the program #
###################

if __name__ == "__main__":
    response = sentence()
