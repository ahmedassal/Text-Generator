from TextModifier import TextModifier

from nltk.util import ngrams
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
import io
from nltk.corpus import brown
from nltk.probability import LidstoneProbDist
from ngram import NgramModel


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

    mn = MakeNgram(stemmedc)
    bigramc = mn.makeBigram(stemmedc)
    listWithProb = mn.countProbability(bigramc)





    response = raw_input("Please enter your input: ")

    tmr = TextModifier(response)
    tokenz = tmr.cleanText(response)

    #test
    print('Your input data is:')
    print(tokenz)

    #all chars to lowercase
    lowercaseList = tmr.lowercase(tokenz)

    #test
    print(lowercaseList)

    #remove stop words
    noMoreStopwords = tmr.removeStopWords(lowercaseList)

    #test
    print('No more stop words: ')
    print(noMoreStopwords)

    #Stemming
    stemmed = tmr.stemmText(noMoreStopwords)

    #test
    print('Stemmed text: ')
    print(stemmed)





    sent = "I am the I am the I am the best computer hacker 4 in, the world and Henrik and Jenny as well. We never knew what would happen"


    unigram = sent.split()
    bigram  = ngrams(sent.split(), bigramN)
    trigram = ngrams(sent.split(), trigramN)

    fdist1 = FreqDist()
    fdist2 = FreqDist(bigram)

    for j,v in fdist2.items():
        print j,v


    for word in word_tokenize(sent):
        fdist1[word.lower()] +=1

    print(fdist1.items())



