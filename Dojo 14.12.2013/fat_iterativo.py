#!/usr/bin/env python

def fatorial(n):
    multiplicacao = 1
    for i in range(1, n+1):
        multiplicacao = i*multiplicacao
    print multiplicacao

fatorial(5)

