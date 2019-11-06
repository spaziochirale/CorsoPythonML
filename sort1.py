# chiede il numero di elementi da ordinare
n = eval(input("Quanti nomi vuoi inserire? "))

# effettuo un ciclo per il numero determinato di volte e inserisco ogni elemento
# nella lista
l=[]
for i in range(0,n):
    nome = input("Nome>")
    l.append(nome)

# ordino la lista
l.sort()

# stampo gli elementi della lista ordinata
for nome in l:
    print(nome)
