#!/usr/bin/env python3

import random as rd
import json

##########################
# Pre-process data files #
##########################

with open("syngrams.json", "r") as f:
    ngrams = json.load(f)


def expand_lex(lex):
    return [word for word, freq in lex.items() for _ in
            range(int(freq/1000))]


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


def sgl_np():
    while True:
        options = [next(pn).title(),
                   next(prp),
                   "{} {}".format(next(det), next(nom))
                   # "{} {} {}".format(next(noun_phrase()), next(conj),
                   #                   next(noun_phrase()))
                   ]
        yield rd.choice(options)


def conj_np():
    while True:
        yield "{} {} {}".format(next(sgl_np()), next(conj), next(sgl_np()))


def noun_phrase():
    while True:
        yield rd.choice([next(sgl_np()), next(conj_np())])


def sgl_nom():
    while True:
        options = [next(noun),
                   "{} {}".format(next(adj), next(noun))
                   # "{} {} {}".format(next(nominal()), next(conj),
                   #                   next(nominal()))
                   ]
        yield rd.choice(options)


def conj_nom():
    while True:
        yield "{} {} {}".format(next(sgl_nom()), next(conj), next(sgl_nom()))


def nominal():
    while True:
        yield rd.choice([next(sgl_nom()), next(conj_nom())])


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
