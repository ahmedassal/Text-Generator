#hsd
from nltk.util import ngrams
from nltk.probability import FreqDist, LidstoneProbDist

class MakeNgram():


    def __init__( self, listInput ):
        self.text = listInput

    def _setugram(self, listInput):
        self._uniGram = listInput

    def _setuFdist(self):
        self._uniFdist = FreqDist(self._uniGram)

    def makeBigram(self, listInput):
        bigram = ngrams(listInput, 2)
        for bigram in bigram:
            print (bigram)
        return bigram

    def makeBigramTree(self, listInput):
        bigram = self.makeBigram(listInput)


    def countProbability(self, ngram):
        fdist = FreqDist(ngram)

