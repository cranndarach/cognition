The computational theory of mind is fascinating. It takes the huge, nebulous
concept of cognition, recently thought to be so opaque that is was considered
useless in science, and turns it into something so concrete and _attainable_
that I can try to program little bits of it as part of my class notes, and I
can entertain the idea that the mind is Turing complete.

My programming skills are very much still developing, and one thing that I have
been learning about recently is the distinction between functional programming
and object-oriented programming styles. It is an interesting distinction
because it shifts the way I think about programming problems, and it has
introduced me to new ways of making code more efficient. When I am thinking
about computational theories of cognition, I find myself considering which
style would be more appropriate for a given problem. It seems that the
distinction between object-oriented and functional programming could have
implications for our understanding of cognition, and I would like to explore
this idea more.

## Object-oriented vs. functional programming

In object-oriented programming, everything is an object: a string, a number, an
expression, a function, all objects. Objects have types (or classes) that
define what one can do with them, or *to* them. The programmer can even define
new classes and objects, with their own attributes and methods. Once an object
is created, it can be updated throughout the life of the program. A counter can
be incremented without having to create a new counter object, a string can be
edited, a list can be modified, etc.

On the other hand, there are no objects in strict functional programming, only
values. Arguments that are passed to a function are used as input, but they are
not modified by the function. In fact, values cannot even be modified once they
are defined. In that way, the term "function" is being used in its mathematical
sense, "y=f(x)", in contrast with how it is used in imperative programming
(including object-oriented programming) to mean "do f to x."

These two styles of programming relate to the computational theories of
cognition in a couple ways. Interestingly, they can both be considered modular,
but in different ways. They also each have implementations made with fervent
devotion and with less commitment. There are also areas where each excels and
the other lags behind, which may have interesting implications for cognition. 

### Modularity

First, both object-oriented programming and functional programming can be
considered modular in their own respect. Objects are units in themselves. They
have their own properties and methods, some of which may be "private," or
inaccessible outside of the object itself. Functional programming is considered
modular because of the absence of consequence: because values are never
modified by functions, the programmer can be confident that passing `x` as
input to function `f` will yield the same result every single time.
Calculations are entirely self-contained, even if the output can be assigned to
a new global variable.

### Strict adherence vs. somewhere in between

There are some languages that are undoubtedly object-oriented, e.g., C/C++ and
Java. One might write a class with a set of properties and methods that other
objects or the user can use to change the values of those properties. The
purpose of the program is essentially to modify those properties in a specific
way and return some value or display some output as a result.

Other languages are undoubtedly functional, e.g., Haskell. One might define
a number of functions to get from one value to another, and define a number of
values using `let` statements, and then use function application and function
composition to determine some new value given the input.

Then there are languages that are a little bit of both. Python, for example, is
technically considered an object-oriented language, because its values are
objects, and they are dynamic or mutable. However, the instance-of-a-class
style characteristic of more canonical object-oriented languages is only one
way to code with Python. It also has a number of properties that are more
functional. For example, although objects can be modified, it is not
obligatory; the output of a function can be assigned to a new variable just as
easily as it can be assigned back to the input variable. Python also supports
list comprehensions (e.g., calculating the square of every item in a list using
`list2 = [x**2 for x in list1]`), generator expressions (e.g., calculating the
sum of all the items in a list using `y = sum(x for x in list1)`), and lambda
calculus (e.g., extracting the numbers greater than 10 from a list using `list2
= list(filter(lambda x: x > 10, list1))`), which are common uses of functional
programming. So, then, it seems that the answer to the question of "Is Python
an object-oriented language or a functional language?" may depend a lot on the
problem at hand.

### Strengths of each

Functional programming and object-oriented programming each have their
particular areas where they excel. When considering these areas within the
larger question of the computational theory of mind, it is interesting to
consider whether cognition as we understand it also excels in these areas.

A strength of object-oriented programming is its conceptual structure. Objects
have attributes, and those attributes are themselves objects. Thus, one could
construct objects out of features, relationships, tasks, etc., allowing for
hierarchical structure as well as an intuitive way to describe any given
object.

Mutability is the other primary advantage of object-oriented programming. It is
generally more efficient to overwrite a variable's value with a more up-to-date
version. This is also fairly intuitive from a cognitive perspective: knowledge,
experience, memory, even thought processes are dynamic, and so it makes sense
to allow computational implementations of cognition to have mutable values as
well.

But, challenging the above intuition, one of the advantages of functional
programming is that its values are immutable. Yes, it is convenient to simply
update the value of `x` as you go, but it is not exactly safe. A functional
program simply describes the means of getting from one value to another, but
leaves the input value intact. That is, after calculating the value of `f(x)`
for `x=1`, `x` will still be equal to 1. No matter how many times that function
is run, the value of `x` will remain the same. New values may be added to
memory, but the existing ones remain as they are. Could that be more reflective
of how cognition works? When we learn something new about an existing concept,
is that concept overwritten with a clone of itself with new piece of
information attached, or is the new piece of information stored alongside the
existing knowledge, with functions to relate them as needed? It is an
interesting question.

Functional programming has other advantages. First, it excels at pattern
matching. This is best depicted with example code. Imagine some (admittedly
unnatural) scenario where you wanted to check a pair of values and return `True`
if the first value was "apples" or (logical or) the second value was "oranges."
In Python, that would take some surprisingly convoluted code:

```py
def apples_and_oranges(pair):
    first, second = pair
    if first == "apples":
        return True
    elif second == "oranges":
        return True
    else:
        return False
```

First, the pair is broken into two separate variables. Then each one is tested
in turn for its equivalence with the desired value. If a match is found, the
function returns `True`. If not, it returns `False`.

Compare that to the Haskell equivalent:

```hs
applesAndOranges :: (String, String) -> Bool
applesAndOranges ("apples", _) = True
applesAndOranges (_, "oranges") = True
applesAndOranges _ = False
```

The first line is the type statement, telling the interpreter that the input
will be a pair of two strings, and the output will be a boolean. The next lines
do the pattern matching. The first line says, "for a pair that starts with
'apples', don't bother evaluating the second member. The answer is `True`." The
same applies to the next line: the first member does not need to be evaluated
if the second member is "oranges." The last line says, "if you've made it this
far, don't bother unpacking the pair. The answer is `False`."

This pattern-matching aptitude definitely seems like a place where functional
programming mirrors cognition better than object-oriented programming does, and
is worth thinking more about.

The "lazy" evaluation style ("don't bother evaluating the other member") is
also intriguing. By limiting computation to only what is needed to achieve the
answer, it allows for a way to deal with infinity where many other languages
would crash (e.g., Haskell has no problem grabbing the first three numbers of
an infinite list in `take 3 [1..]`, whereas other languages would need to
generate the "entire" infinite list first). If there is an analogous cognitive
evaluation style, it may suggest a way to handle concerns of limited
computational power/working memory that come with some computational theories.


