# classification technique

words=["eating","eaten","eat","go","going","come","coming","program","programming","history","histori","congratulations","fairly","sportingly"]
from nltk.stem import PorterStemmer,RegexpStemmer ,SnowballStemmer
ps = PorterStemmer()

for word in words:
    print(word+"--->"+ps.stem(word))

# regrexpStemmer


reg_stemmer = RegexpStemmer('ing|s$|e$|able$',min=4)
print(reg_stemmer.stem('eating'))
print(reg_stemmer.stem('ingeats'))


# snowball stemmer-- better accurately
snowball_stemmer = SnowballStemmer('english')
for word in words:
    print(word+"--->"+snowball_stemmer.stem(word))



