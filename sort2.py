# crea lista vuota
l=[]

# chiedi un nome
nome=input("Nome>")

# finché il dato inserito non è 'STOP' aggiungi alla lista e chiedi un nuovo nome
while nome != '':
    l.append(nome)
    nome=input("Nome>")

# ordina la lista
l.sort()
# stampa la lista
for n in l:
    print(n)
