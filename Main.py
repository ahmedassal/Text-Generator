__author__ = 'Group 48'
#test stuff
class Main:
    from nltk.util import ngrams
    from nltk.probability import FreqDist
    from nltk.tokenize import word_tokenize


    sent = "I am the I am the I am the best computer hacker 4 in, the world and Henrik and Jenny as well. We never knew what would happen"
    bigramN = 2
    trigramN = 3

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


