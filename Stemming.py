from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer

p_stemmer = PorterStemmer()
s_stemmer = SnowballStemmer(language="english")


print(s_stemmer.stem("writing"))
