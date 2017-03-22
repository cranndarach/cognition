#!/usr/bin/env python3

import random as rd
# import json

##########################
# Pre-process data files #
##########################


def prep_list(pos):
    with open("./wordlists/index.{}".format(pos), "r") as f:
        wordlist = [line.split(" ")[0].replace("_", " ") for line in
                    f.readlines()[29::]]
    return wordlist

nouns = prep_list("noun")
adjectives = prep_list("adj")
adverbs = prep_list("adv")
conjunctions = ["and", "or"]
coord_conjs = conjunctions + ["but", "because", "though", "yet", "while",
                              "whereas"]
determiners = ["the", "a(n)", "my", "her", "his", "their", "this", "that",
               "every", "everyone's"]
prepositions = ["of", "on", "in", "under", "inside", "within", "outside",
                "in front of", "behind", "next to", "from", "toward", "near",
                "on top of", "across from"]
trans_verbs = ["glorify", "refuse", "destabilize", "undersell", "distort",
               "play a joke on", "add", "impale", "kiss", "discolorize",
               "ambush", "pinpoint", "communalize", "machine-wash", "nose",
               "maltreat", "skirt", "roll out", "disbar", "pass over",
               "mythicize", "click", "ponder", "post", "write down",
               "create mentally", "unbolt", "damn", "masculinize",
               "containerize", "broadcast", "harden", "cork", "partake in",
               "cut out", "shine at", "swish", "sovietize", "deputize",
               "synchronize", "cross-link", "splint", "co-opt", "tout",
               "muck up", "win", "inhale", "set down", "cloud over", "depilate",
               "write on", "counterbalance", "attempt", "bulldoze", "try",
               "outscore", "sink", "reconvict", "implement", "jumble",
               "get hitched with", "condition", "recapitulate", "bench",
               "cut to", "omit", "cube", "compost", "draw a bead on", "degrade",
               "oust", "devise", "permit", "pull", "cybernate", "fire up",
               "look on", "check over", "tailor-make", "stick", "spare",
               "marinate", "embroil", "motivate", "effuse", "whap", "poop out",
               "bet on", "pet", "dandify", "pick out"]
intrans_verbs = ["skip town", "refuse", "houseclean", "ripple", "roll out",
                 "ring out", "rhapsodize", "click", "overlap", "swagger",
                 "harden", "burn out", "oversleep", "slack off", "horse around",
                 "recover", "swish", "chuck up the sponge", "synchronize",
                 "splinter", "sulk", "wail", "fly off the handle", "win",
                 "run away", "depilate", "try", "bulldoze", "sink",
                 "mill about", "compete", "die down", "take the air",
                 "rain buckets", "look on", "flump", "skateboard", "marinate",
                 "take the veil", "disappear", "move involuntarily", "poop out",
                 "wobble"]

with open("./wordlists/names.csv", "r") as f:
    proper_nouns = [name[:-1] for name in f.readlines()]


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

noun = word_gen(nouns)
adj = word_gen(adjectives)
dt = word_gen(determiners)
t_verb = word_gen(trans_verbs)
i_verb = word_gen(intrans_verbs)
conj = word_gen(coord_conjs)
prep = word_gen(prepositions)
pn = word_gen(proper_nouns)
# prp = word_gen(personal_pronouns)
adv = word_gen(adverbs)
# wh_adv = word_gen(wh_adverbs)
# modal = word_gen(modals)


def determiner():
    while True:
        options = [next(dt),
                   "{}'s".format(next(pn))
                   ]
        yield rd.choice(options)


def sgl_np():
    while True:
        options = [next(pn).title(),
                   # next(prp),
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


def tverb():
    while True:
        options = ["{} {}".format(next(t_verb), next(np)),
                   "{} {} {}".format(next(adv), next(t_verb), next(np))
                   ]
        yield rd.choice(options)


def iverb():
    while True:
        options = [next(i_verb),
                   "{} {}".format(next(adv), next(i_verb))
                   ]
        yield rd.choice(options)


def verb_phrase():
    while True:
        options = [next(iv),
                   "{} {}".format(next(iv), next(pp)),
                   next(tv),
                   "{} {}".format(next(tv), next(pp))
                   ]
        yield rd.choice(options)


def prep_phrase():
    while True:
        yield "{} {}".format(next(prep), next(np))


def sub_clause():
    while True:
        yield "{} {}".format(next(conj), next(cl))


def clause():
    while True:
        yield "{} {}".format(next(np), next(vp))
        # sent = sent.capitalize()
        # yield sent


def sentence():
    while True:
        options = [next(cl)]*4 + ["{}, {}".format(next(cl), next(subcl))]
        yield "{}.".format(rd.choice(options)).capitalize()

det = determiner()
np = noun_phrase()
nom = nominal()
iv = iverb()
tv = tverb()
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
