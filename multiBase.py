#!/usr/bin python
# coding=utf-8
# base64 para URLS // codeBase = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_"

# base69 codeBase = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_:/$?."
# base70 codeBase = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_:/$?. "

# Se puede codificar un mensaje si se crea una base aleatorio con los mismos caracteres aunque no he tenido en cuenta tildes ni caracteres especiales

codeBase = "u.rEH2gDxk$Ki?mcCzb9lp _:OwhdMyWP/Yeos8SJfaA6GX1-LvNBI5qF7Q4n30tTjRZUV"

#base16 = "0123456789ABCDEF"
#base5 = "01234"

def encode(valor_en,base):
    nnum = ""
    code = codeBase[0:base]
    while valor_en > 0:
        nnum = nnum +code[int(valor_en%base)]
        valor_en = valor_en/base
    return nnum[::-1]

def decode(valor_de,base):
    numero = 0
    c = 0
    n = valor_de
    code = codeBase[0:base]
    for i in n[::-1]:
        numero += (code.find(i)*(base**c))
        c +=1
    return numero

if __name__ == '__main__':
    #Ejemplos de uso
    b = int(raw_input("base:"))
    valor = int(raw_input("numero:"))
    v = encode(valor,b)
    print v
    print decode(v,b)
    val = encode(decode('Hola me llamo Jose Reyes',70), 64)
    print val
    print encode(decode(val, 64),70)