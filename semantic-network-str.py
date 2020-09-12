import regex as re
import numpy
import pandas as pd

texto = 'This uses the split() function of strings, which splits a string into a list of items. The result is then joined back into a string. You can split on any string, but whitespace is the default.'

texto = re.sub(r"[^\P{P}.]+", "", texto)
texto = re.sub(r"(?<=\.)\s", "", texto)

with open(r"stopwords.txt", 'r') as f:
    stopwords = [name.rstrip().lower() for name in f]
    texto = " ".join([x for x in texto.split(' ') if x.lower() not in stopwords])

vFrases = texto.split('.')
vFrases.pop(-1)
col1=[]
col2=[]

# print(vFrases)

for frase in vFrases:
    # frase = ''
    vPalavras = frase.split(' ')
    nPalavras = len(vPalavras)

    if nPalavras > 2:
    nLinhas = 0
    vNumeros = []
    for i in range(nPalavras):
        b = nPalavras-(i+1)
        if b>0:
            vNumeros.append(b)
        nLinhas = nLinhas + b

    nNumeros= len(vNumeros)
    invNumeros = vNumeros[::-1]

    c1 = []
    for i in range(nNumeros):
        for j in range(vNumeros[i]):
            c1.append(vPalavras[i])  
    col1.extend(c1)

    # print(nNumeros)

    ordemC2 = []
    for i in range(nNumeros):
        for j in invNumeros:
            ordemC2.append(j)
        invNumeros.pop(0)
    print(ordemC2)
    Mposicao = []
    posicaoC2 = []
    for i in range(int(nLinhas/nPalavras)):
        for j in range(nPalavras):
            posicaoC2.append(vPalavras[j])
            Mposicao.append(j)

    c2 =[]
    c2[:] = [posicaoC2[i] for i in ordemC2]
    col2.extend(c2)

matriz = numpy.c_[col1,col2]
df = pd.DataFrame(columns=["source", "target"], data=matriz)
df.to_csv("tec.csv", index=False)
