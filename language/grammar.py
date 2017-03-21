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

# print(len(ngrams["NN"]))
# sys.exit(0)


def expand_lex(lex):
    return [word for word, freq in lex.items() for _ in range(int(freq/10000))]


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

# #################
# # Phrases, etc. #
# #################
#
#
# def prep_phrase():
#     return "{} {}".format(prep(), types_np())
#
#
# def verb_phrase():
#     sub_vp = ["{}".format(intransitive_verb()),
#               "{} {}".format(transitive_verb(), noun_phrase())]
#
#     return ran(sub_vp + ["{} {}".format(helping_verb(), adjective()),
#                          "{} {}".format(helping_verb(), noun_phrase()),
#                          "{} {}".format(ran(sub_vp), prep_phrase()),
#                          "{} {}".format(intransitive_verb(), adverb()),
#                          "{} {} {}".format(adverb(), transitive_verb(),
#                                            noun_phrase())
#                          ])
#
#
# def noun_phrase():
#     return ran([types_np(),
#                 "{} {} {}".format(types_np(), conj(), types_np()),
#                 "{} {}".format(types_np(), prep_phrase())
#                 ])
#
#
# def clause():
#     return "{} {}".format(noun_phrase(), verb_phrase())
#
#
# def sentence():
#     out = ran(["{}.".format(clause()),
#                "{}, {} {}.".format(clause(), coord_conj(), clause())])
#     # out = out.capitalize()
#     print(out)
#     # return out
#
#
# # def main():
# #     sentence()
#
#
# ####################
# # Helper Functions #
# ####################


def word_gen(words):
    while True:
        yield rd.choice(words)


def phrase_gen(*args):
    # if "list" in list(map(type, args)):
    #     choices = []
    #     for arg in args:
    #         if type(arg) == "list":
    string_template = args[0]
    while True:
        yield string_template.format(next(gen) for gen in args[1:])


def option_gen(*options):
    while True:
        yield rd.choice(options)


# def formatter(arg):
#     string_template = arg[0]
#     return string_template.format([next(gen) for gen in arg[1:]])


# def ran(spl):
#     return rd.choice(spl)


noun = word_gen(nouns)
adjective = word_gen(adjectives)
det = word_gen(determiners)

# nominal = option_gen(next(noun), next(phrase_gen("{} {}", adjective, noun)))
# noun_phrase = phrase_gen("{} {}", det, nominal)


def noun_phrase():
    while True:
        yield "{} {}".format(next(det), next(nom))
np = noun_phrase()


def nominal():
    while True:
        options = [next(noun),
                   "{} {}".format(next(adjective), next(noun))]
        yield rd.choice(options)
nom = nominal()

# def nominal():
#     return ran([noun(), "{} {}".format(adjective(), noun())])
#
#
# def combo_np():
#     return "{} {}".format(det(), nominal())
#
#
# def types_np():
#     return ran([proper_noun(), combo_np()])
#
#
# ###################
# # Run the program #
# ###################
#
# if __name__ == "__main__":
#     sentence()
