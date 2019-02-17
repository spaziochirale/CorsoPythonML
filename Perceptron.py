# ESEMPIO DEFINIZIONE E TRAINING DI UN PERCEPTRON
# PER RISOLVERE UN PROBLEMA DI CLASSIFICAZIONE
# CON SEPARAZIONE LINEARE DEI DATI
#
# Corso di Python & Machine Learning
#

import numpy as np
import pylab as pl
import random       

class Perceptron:
    def __init__(self, learn_speed, num_inputs):
        self.speed = learn_speed
        self.weights = []
        for x in range(0, num_inputs):
            self.weights.append(random.random()*2-1)

    # Activation function
    def activate(self, num):
        if num > 0:
            return 1
        return -1

    # Forward propagation
    def feed_forward(self, inputs):
        sum = 0
        for x in range(0, len(self.weights)):
            sum += self.weights[x] * inputs[x]
        return self.activate(sum)

    # Back propagation
    def back_propagation(self, inputs, desired_output):
        guess = self.feed_forward(inputs)   
        error = desired_output - guess      
        for x in range(0, len(self.weights)):
            self.weights[x] += error*inputs[x]*self.speed
        if error == 0:
            return(0)
        else:
            return(1)

class Trainer:
    def __init__(self):
        self.perceptron = Perceptron(0.01, 3)

    def f(self, x):
        return 0.5*x + 10 # linea retta: f(x) = 0.5x + 10

# La funzione train riceve come parametro il numero di punti da utilizzare 
    def train(self,n): 
        for x in range(0, n):
            x_coord = random.random()*500-250
            y_coord = random.random()*500-250
            line_y = self.f(x_coord)
            if y_coord > line_y:
                answer = 1
            else:
                answer = -1
            self.perceptron.back_propagation([x_coord, y_coord,1], answer)
        return self.perceptron 

# Definizione della linea
def linea(x):
    return 0.5*x + 10

# Definizione della funzione per generare casualmente i punti di test
def generaPunti(n):
    l=[]
    for x in range(0, n):
        x = random.random()*500-250
        y = random.random()*500-250
        l.append([x,y])
    return l

# Funzione per disegnare la retta e i risultati
def test(p, listaPunti, titolo):
    lx=[]
    ly=[]
    for x in range(-250,250):
        y=linea(x)
        lx.append(x)
        ly.append(y)
    pl.plot(lx,ly)
    for punto in listaPunti:
        guess=p.feed_forward([punto[0],punto[1],1])
        if guess == 1:
            formato = 'go'
        else:
            formato = 'ro'
        pl.plot(punto[0],punto[1],formato)
    pl.title(titolo)
    pl.grid(True)
    pl.show()
 

# Creare un trainer
# Generare il perceptron addestrandolo con un numero a piacere di punti
# Generare la lista di prova
# Lanciare il test
l=generaPunti(500)
t=Trainer()
p=t.train(0)
test(p,l,"Perceptron non addestrato")
p=t.train(10)
test(p,l,"Perceptron addestrato su 10 punti")
p=t.train(100)
test(p,l,"Perceptron addestrato su 100 punti")
p=t.train(1000)
test(p,l,"Perceptron addestrato su 1000 punti")
p=t.train(1000000)
test(p,l,"Perceptron addestrato su 1 milione di punti")








