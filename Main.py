from TextModifier import TextModifier
from nltk.corpus import treebank
import io
from NGMaker import NGMaker
from nltk.corpus import brown
from nltk.parse import RecursiveDescentParser
from nltk import Nonterminal, nonterminals, Production, CFG



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

    grammar1 = CFG.fromstring("""
    S -> NP VP
    PP -> P NP
    NP -> 'the' N
    VP -> V NP
    N -> 'noun'
    V -> 'verb'
    P -> 'preposition'
    """)

    grammar = {'S':{'NP':'VP'},'PP':{'P':'NP'},'NP':{'the':'N'},'VP':{'V':'NP'},'N':'noun','V':'verb','P':'preposition'}

    sent = ''
    _tmp = []
    stepOne = grammar['S']



    def _test(self, stepOne):
        if isinstance(stepOne,dict):
            for s in stepOne:
                self._test(s)
                self._tmp.append(s)

        else:
            self._tmp.append(stepOne)

    print(_tmp)


    #n-gram
    bigramN = 2
    trigramN = 3

    nm = NGMaker(stemmedc)
    unigram = nm._setugram(stemmedc)
    bigramc = nm._setBigram(stemmedc)
    trigram = nm._setTrigram(stemmedc)

    response = raw_input("Please enter your input: ")

    brownNewsSents = brown.sents(categories = 'news')

    parser = RecursiveDescentParser(grammar)




    print(stemmedc)


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






