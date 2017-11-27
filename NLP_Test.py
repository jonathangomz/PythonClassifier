import nltk
from nltk.probability import FreqDist


ask 		= 'where born the son of Isaac'
ask_nltk 	= nltk.word_tokenize(ask)
ask_tagged 	= nltk.pos_tag(ask_nltk)

'''
ver1 = 'In the beginning God created the heavens and the earth.'
ver2 = 'And the earth was waste and void; and darkness was upon the face of the deep: and the Spirit of God moved upon the face of the waters.'
ver3 = 'And God said, Let there be light: and there was light.'

ver1_nltk = nltk.word_tokenize(ver1)
ver2_nltk = nltk.word_tokenize(ver2)
ver3_nltk = nltk.word_tokenize(ver3)

ver1_tagged = nltk.pos_tag(ver1)
ver2_tagged = nltk.pos_tag(ver2)
ver3_tagged = nltk.pos_tag(ver3)

test1 = FreqDist(ver1)
print(test1.values())
'''

print(ask_tagged)
grammar = r"""
  NP: {<DT|JJ|NN.*>+}          # Chunk sequences of DT, JJ, NN
  PP: {<IN><NP>}               # Chunk prepositions followed by NP
  VP: {<VB.*><NP|PP|CLAUSE>+$} # Chunk verbs and their arguments
  CLAUSE: {<NP><VP>}           # Chunk NP, VP
  """
cp = nltk.RegexpParser(grammar)
result = cp.parse(ask_tagged)
print(result)