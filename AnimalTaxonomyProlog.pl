%.    Esempio di ragionamento inferenziale
%
%.    Tassonomia elementare del regno animale
%
%.   @author Stefano Capezzone (Corso di Coding e Machine Learning)
%.    


mammifero(X) :- allattaLaProle(X), ricopertoDa(X,peli).
ricopertoDa(ragno, peli).
ricopertoDa(cane, peli).
ricopertoDa(gallina, piume).
ricopertoDa(cigno, piume).
allattaLaProle(cane).
uccello(X) :- ricopertoDa(X,piume).
possiede(X,becco) :- uccello(X).
possiede(X,bocca) :- mammifero(X).


/** <examples>

?- mammifero(cane).
?- uccello(cigno).
?- possiede(gallina, X).

*/
