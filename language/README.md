# Readme for the sentence producer (grammar.py)

This started as an exercise trying to Pythonize an example from class, and then
it grew. It is far from complete, and there is no weighting for unigram/bigram/ngram
frequency. But it's fun.

Below are usage instructions, followed by some details of the program.

## Running the program

**Requirement:** Python3
**Recommended:** IPython interpreter

* Download [the file](https://raw.githubusercontent.com/cranndarach/cognition/master/language/grammar.py); save it somewhere you'll remember (e.g., Desktop or Documents)
* Open a terminal or command propmt
* `cd` (change directories) into the folder where you saved the file. If you saved
it to Desktop or Documents, that means you will enter `cd Desktop` or `cd Documents`

#### If you are using IPython (recommended)

* enter `ipython` into the terminal. This will start an interactive IPython session.
* enter `%run grammar.py`
    * It should delay a second and then print out a sentence.
* If you want to make more sentences, keep entering `sentence()`
* When you are done, enter `exit`, or `quit()`, or press Ctrl+D (or Cmd+D)

#### If you are not using IPython

* Enter `python grammar.py` into your terminal
    * It will delay a second and then print a sentence.
* If you want to generate more sentences, keep entering `python grammar.py`

## Details

### Use of WordNet

Most of the word lists come from WordNet (Princeton University, 2010). WordNet
has some collocations (multi-word phrases), spelling variations, low-frequency
words, etc. All of these have been left in.

The names come from a US Census database found on Kaggle.

### Verbs

WordNet's verbs are not subdivided into transitive, intransitive, etc. To account
for this for this toy grammar, I took a random sample of around a hundred verbs,
and separated them into transitive or intransitive.

### Inflection

There is nothing built in to inflect words according to the context. I might add
it in sometime. It seems like a fun exercise. You're welcome to fork it and give
it a shot yourself.

## References

Princeton University "About WordNet." WordNet. Princeton University. 2010. <http://wordnet.princeton.edu>
