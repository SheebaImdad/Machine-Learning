# OUTPUT IS Lemma which is root word, return meaningful word
import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')

words=["eating","eaten","eat","go","going","goes","come","coming","programs","programming","history","histori","congratulations","fairly","sportingly"]
lemmatizer = WordNetLemmatizer()
for word in words:
    print(lemmatizer.lemmatize(word))
