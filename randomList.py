#!/usr/bin python
# coding=utf-8
import random
def randomList(lista):
    p = []
    for i in lista:
        b = True
        while b:
            n = int(random.random()*len(lista))+1
            if n in p:
                b = True
            else:
                p.append(n)
                b = False

    print p
    return p


def randomListString(lista):
    p = []
    ps = []
    for i in lista:
        b = True
        while b:
            n = int(random.random()*len(lista))
            if n in p:
                b = True
            else:
                p.append(n)
                ps.append(lista[n])
                b = False

    print p
    print ps
    return ps

if __name__ == '__main__':
    #Ejemplos de uso
    a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    s = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","z"]
    randomList(a)
    randomListString(s)
