#!/usr/bin/env python3

import random as rd
import json
# import sys
# import numpy as np

##########################
# Pre-process data files #
##########################

with open("syngrams.json", "r") as f:
    ngrams = json.load(f)


def expand_lex(lex):
    return [word for word, freq in lex.items() for _ in range(int(freq/10000))]


def word_gen(words):
    while True:
        yield rd.choice(words)


###################
# Parts of Speech #
###################

nouns = expand_lex(ngrams["NN"])
adjectives = expand_lex(ngrams["JJ"])
conjunctions = expand_lex(ngrams["CC"])
prepositions = expand_lex(ngrams["IN"])
proper_nouns = expand_lex(ngrams["NNP"])
determiners = expand_lex(ngrams["DT"])
personal_pronouns = expand_lex(ngrams["PRP"])
adverbs = expand_lex(ngrams["RB"])
verbs = expand_lex(ngrams["VBZ"])

# ####################
# # Helper Functions #
# ####################

noun = word_gen(nouns)
adj = word_gen(adjectives)
det = word_gen(determiners)
verb = word_gen(verbs)
conj = word_gen(conjunctions)
prep = word_gen(prepositions)
pn = word_gen(proper_nouns)
prp = word_gen(personal_pronouns)
adv = word_gen(adverbs)


def noun_phrase():
    while True:
        options = [next(pn).title(),
                   next(prp),
                   "{} {}".format(next(det), next(nom))
                   ]
        yield rd.choice(options)


def nominal():
    while True:
        options = [next(noun),
                   "{} {}".format(next(adj), next(noun))]
        yield rd.choice(options)


def vb():
    while True:
        options = [next(verb),
                   "{} {}".format(next(adv), next(verb))]
        yield rd.choice(options)


def verb_phrase():
    while True:
        options = [next(v),
                   "{} {}".format(next(v), next(pp))
                   ]
        yield rd.choice(options)


def prep_phrase():
    while True:
        yield "{} {}".format(next(prep), next(np))


def sentence():
    while True:
        sent = "{} {}.".format(next(np), next(vp))
        sent = sent.capitalize()
        yield sent


np = noun_phrase()
nom = nominal()
v = vb()
vp = verb_phrase()
pp = prep_phrase()


def go():
    print(next(sentence()))

# ###################
# # Run the program #
# ###################

if __name__ == "__main__":
    go()
