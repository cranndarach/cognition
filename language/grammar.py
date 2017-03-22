#!/usr/bin/env python3

import random as rd
import json

##########################
# Pre-process data files #
##########################

with open("syngrams.json", "r") as f:
    ngrams = json.load(f)


def expand_lex(*args):
    words = []
    for lex in args:
        words += [word for word, freq in lex.items() for _ in
                  range(int(freq / 5000))]
    return words


def word_gen(words):
    while True:
        yield rd.choice(words)


# A curiosity function:
def percent_of(what, query):
    how_many = len(list(filter(lambda x: x == query, what)))
    out_of = len(what)
    percent = (how_many / out_of) * 100
    percent = round(percent, 3)
    print("{} out of {}, or {}%".format(str(how_many), str(out_of),
                                        str(percent)))
    return percent


###################
# Parts of Speech #
###################

nouns = expand_lex(ngrams["NN"])
adjectives = expand_lex(ngrams["JJ"])
conjunctions = expand_lex(ngrams["CC"])
prepositions = expand_lex(ngrams["IN"])
proper_nouns = expand_lex(ngrams["NNP"])
determiners = expand_lex(ngrams["DT"], ngrams["PRP$"], ngrams["WDT"])
personal_pronouns = expand_lex(ngrams["PRP"])
adverbs = expand_lex(ngrams["RB"])
verbs = expand_lex(ngrams["VBZ"])
modals = expand_lex(ngrams["MD"])
wh_adverbs = expand_lex(ngrams["WRB"])

####################
# Helper Functions #
####################

noun = word_gen(nouns)
adj = word_gen(adjectives)
det = word_gen(determiners)
verb = word_gen(verbs)
conj = word_gen(conjunctions)
prep = word_gen(prepositions)
pn = word_gen(proper_nouns)
prp = word_gen(personal_pronouns)
adv = word_gen(adverbs)
wh_adv = word_gen(wh_adverbs)
modal = word_gen(modals)


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
        # yield rd.choice([next(sgl_np()), next(conj_np())])
        # I know this is just an extra layer but I'm leaving it so
        # that the single/conjunction can be brought back if wanted.
        yield next(sgl_np())


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
        # yield rd.choice([next(sgl_nom()), next(conj_nom())])
        yield next(sgl_nom())


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


def sub_clause():
    while True:
        yield "{} {}".format(next(wh_adv), next(cl))


def clause():
    while True:
        yield "{} {}".format(next(np), next(vp))
        # sent = sent.capitalize()
        # yield sent


def sentence():
    while True:
        options = [next(cl)]*4 + ["{}, {}".format(next(cl), next(subcl))]
        yield "{}.".format(rd.choice(options)).capitalize()

np = noun_phrase()
nom = nominal()
v = vb()
vp = verb_phrase()
pp = prep_phrase()
cl = clause()
subcl = sub_clause()


def go():
    print(next(sentence()))

# ###################
# # Run the program #
# ###################

if __name__ == "__main__":
    go()
