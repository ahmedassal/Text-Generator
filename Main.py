from TextModifier import TextModifier
from nltk.corpus import treebank
import io
from NGMaker import NGMaker




__author__ = 'Group 48'
#test stuff
class Main:



    c = io.open('ourcorpus.txt', mode='r', encoding='utf-8')
    corpus = c.read()

    # proccess corpus
    tmc = TextModifier(corpus)
    tokenzc = tmc.cleanText(corpus)
    lowercaseListc = tmc.lowercase(tokenzc)
    noMoreStopwordsc = tmc.removeStopWords(lowercaseListc)
    stemmedc = tmc.stemmText(noMoreStopwordsc)

    print(stemmedc)

    #n-gram
    bigramN = 2
    trigramN = 3

    nm = NGMaker(stemmedc)
    unigram = nm._setugram(stemmedc)
    bigramc = nm._setBigram(stemmedc)
    trigram = nm._setTrigram(stemmedc)

    response = raw_input("Please enter your input: ")



    tmr = TextModifier(response)
    tokenz = tmr.cleanText(response)

    #test

    #all chars to lowercase
    lowercaseList = tmr.lowercase(tokenz)
    #remove stop words
    noMoreStopwords = tmr.removeStopWords(lowercaseList)
    #Stemming
    stemmed = tmr.stemmText(noMoreStopwords)

    print('Your input data is:')
    print(stemmed)


    legitWords = []
    for word in stemmed:
        if word in unigram:
            legitWords.append(word)
        else:
            print('no such word exists')






