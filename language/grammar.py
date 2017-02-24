#!/usr/bin/env python3

import random as rd

##########################
# Pre-process data files #
##########################

# prefix = "/home/rachael/Documents/School/databases/WordNet3.1/dict/index.{}"


def prep_list(pos):
    with open("./wordlists/index.{}".format(pos), "r") as f:
        wordlist = [line.split(" ")[0].replace("_", " ") for line in
                    f.readlines()[29::]]
    return wordlist

nouns = prep_list("noun")
adjs = prep_list("adj")
advs = prep_list("adv")
# verbs = prep_list("verb")

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
    names = list(set([name[:-1] for name in f.readlines()]))


###################
# Parts of Speech #
###################

def conj():
    return ran(["and", "or"])


def coord_conj():
    return ran([conj(), "but", "because", "though", "yet", "while", "whereas"])


def det():
    return ran(["the", "a(n)", "my", "her", "his", "their", "this", "that",
                "every", "everyone's", "{}'s".format(proper_noun())])


def noun():
    # return ran(["mother", "father", "brother", "sister", "aunt", "uncle"])
    return ran(nouns)


def proper_noun():
    # return ran(["Anna", "David"])
    return ran(names)


def helping_verb():
    return ran(["is/are"])


def transitive_verb():
    return ran(trans_verbs) + "(s)"


def intransitive_verb():
    return ran(intrans_verbs) + "(s)"


def adjective():
    # adjs = ["nice", "tall"]
    return ran(adjs + ["{} {} {}".format(ran(adjs), conj(), ran(adjs))])


def adverb():
    return ran(advs)


def prep():
    return ran(["of", "on", "in", "under", "for"])


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
    sentence()
