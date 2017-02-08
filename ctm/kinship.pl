parent(abel, me).
parent(bella, me).
sibling(me, claudia).
sibling(claudia, me).
sibling(me, duddie).
sibling(abel, edgar).
sibling(fanny, abel).
sibling(gordie, bella).
sibling(duddie, me).
sibling(edgar, abel).
sibling(fanny, abel).
sibling(gordie, bella).

female(bella).
female(claudia).
female(fanny).
male(abel).
male(duddie).
male(edgar).
male(gordie).

% sibling(X, Y) :- sibling(X, Z), sibling(Z, Y).
% sibling(X, Y) :- sibling(Y, X), !.

mother(X, Y) :- female(X), parent(X, Y).
father(X, Y) :- male(X), parent(X, Y).

aunt_or_uncle(X, Y) :- parent(Z, Y), sibling(Z, X).
aunt(X, Y) :- female(X), aunt_or_uncle(X, Y).
uncle(X, Y) :- male(X), aunt_or_uncle(X, Y).
