#!/usr/bin/env python3

import random as rd
import json
import numpy as np

##########################
# Pre-process data files #
##########################

with open("/home/rachael/projects/ngrams/syngrams.json", "r") as f:
    ngrams = json.load(f)

###################
# Parts of Speech #
###################

mini_conj = ["and", "or"]
conjunctions = mini_conj + ["but", "because", "though", "yet", "while",
                            "whereas"]
determiners = ["the", "a(n)", "my", "her", "his", "their", "this", "that",
               "every", "everyone's", "{}'s".format(ran(proper_noun))]
nouns = ngrams["NN"]
proper_nouns = ngrams["NNP"]
adjectives = ngrams["JJ"]
adverbs = ngrams["RB"]
prepositions = ["of", "on", "in", "under", "for"]
helping_verbs = ["is/are"]

#################
# Phrases, etc. #
#################


def prep_phrase():
    return "{} {}".format(prep(), types_np())


def verb_phrase():
    sub_vp = ["{}".format(intransitive_verb()),
              "{} {}".format(transitive_verb(), noun_phrase())]

    return ran(sub_vp + ["{} {}".format(helping_verb(), adjective()),
                         "{} {}".format(helping_verb(), noun_phrase()),
                         "{} {}".format(ran(sub_vp), prep_phrase()),
                         "{} {}".format(intransitive_verb(), adverb()),
                         "{} {} {}".format(adverb(), transitive_verb(),
                                           noun_phrase())
                         ])


def noun_phrase():
    return ran([types_np(),
                "{} {} {}".format(types_np(), conj(), types_np()),
                "{} {}".format(types_np(), prep_phrase())
                ])


def clause():
    return "{} {}".format(noun_phrase(), verb_phrase())


def sentence():
    out = ran(["{}.".format(clause()),
               "{}, {} {}.".format(clause(), coord_conj(), clause())])
    # out = out.capitalize()
    print(out)
    # return out


# def main():
#     sentence()


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
    sentence()
