    female(pam).
    female(liz).
    female(ann).
    female(pat).

    male(tom).
    male(bob).
    male(jim).

    parent(pam,bob).
    parent(tom,bob).
    parent(tom,liz).
    parent(bob,ann).
    parent(bob,pat).
    parent(pat,jim).


    mother(X,Y):-
  	parent(X,Y),
	  female(X).

    father(X,Y):-
	  parent(X,Y),
	  male(X).

    grandfather(X,Z):-
	  male(X),
	  parent(X,Y),
	  parent(Y,Z).

    grandmother(X,Z):-
	female(X),
	parent(X,Y),
	parent(Y,Z).

    sister(X,Y):-
	parent(Z,X),
	parent(Z,Y),
	female(X),
	X\==Y.

    brother(X,Y):-
	parent(Z,X),
	parent(Z,Y),
	male(X),
	X\==Y.
