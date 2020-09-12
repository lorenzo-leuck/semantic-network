import regex as re
import numpy
import pandas as pd
from csv import DictReader

f = open(r"stopwords.txt", 'r')
stopwords = [name.rstrip().lower() for name in f]

with open("teste-tweets.csv", encoding="utf-8") as f:
    vTweets = [row["text"] for row in DictReader(f)]

vFrases = []

for idx,tweet in enumerate(vTweets):
    tweet = re.sub(r"https?:\/\/(\S+)", "", tweet)
    # tira toda a pontuação exceto arroba e jogo da velha
    tweet = re.sub(r"[^\P{P}@#]+", "", tweet)
    # tira toda a pontuação
    # frase = frase.translate(str.maketrans('','',string.punctuation))
    tweet = " ".join([x for x in tweet.split(' ') if x.lower() not in stopwords])
    tweet = tweet.rstrip() 
    tweet = tweet.strip() 
    tweet = tweet.lower()   
    vFrases.append(tweet) 

col1=[]
col2=[]

for frase in vFrases:
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


        ordemC2 = []
        for i in range(nNumeros):
            for j in invNumeros:
                ordemC2.append(j)
            invNumeros.pop(0)

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
df = pd.DataFrame(columns=["source","target"], data=matriz)
df['source'].replace('', numpy.nan, inplace=True)
df.dropna(subset=['source'], inplace=True)
df['target'].replace('', numpy.nan, inplace=True)
df.dropna(subset=['target'], inplace=True)
df.to_csv("tweets-grafos3.csv", index=False)
