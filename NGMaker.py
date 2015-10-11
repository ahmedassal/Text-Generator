from __future__ import division
#hsd
from nltk.util import ngrams

from nltk.probability import FreqDist, LidstoneProbDist

class NGMaker():


    def __init__( self, listInput ):
        self.text = listInput

    def _setugram(self, listInput):
        self._uniGram = listInput
        pdist = self._setuFdist()
        print (pdist)
        return pdist

    def makeBigram(self, listInput):
        bigram = ngrams(listInput, 2)
        #for bigram in bigram:
            #print (bigram)
        return bigram

    def _setuFdist(self):
        self._uniFdist = FreqDist(self._uniGram)
        return self.makeAProbMap()



    def makeBigramTree(self, listInput):
        bigram = self.makeBigram(listInput)


    def countProbability(self, ngram):
        fdist = FreqDist(ngram)

    def makeAProbMap(self):
        map = {}
        size = len(self._uniFdist)
        print(size)
        for j,v in self._uniFdist.items():
            map[j] = float(v/size)
        return map