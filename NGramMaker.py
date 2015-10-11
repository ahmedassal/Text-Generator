#hsd
from nltk.util import ngrams
from nltk.probability import FreqDist, LidstoneProbDist

class MakeNgram():

    def __init__( self, listInput ):
        text = listInput

    def makeBigram(self, listInput):
        bigram = ngrams(listInput, 2)
        #for bigram in bigram:
            #print bigram
        return bigram

    def countProbability(self, ngram):
        fdist = FreqDist(ngram)

