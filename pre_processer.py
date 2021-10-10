import re
import string 
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
from nltk.corpus import stopwords



def make_stopwords():
    total_stopwords = set(stopwords.words('english'))
    total_stopwords.update(["br","href"])

    negative_stopwords = set(word for word in total_stopwords
                        if "n't" in word or "no" in word)

    final_stopwords = total_stopwords - negative_stopwords
    
    return final_stopwords


HTMLTAGS = re.compile('<.*?>')
table = str.maketrans(dict.fromkeys(string.punctuation))
remove_digits = str.maketrans('','',string.digits)
MULTIPLE_WHITESPACE = re.compile(r"\s+")

def pre_processer(review):
    #remove html tags
    review = HTMLTAGS.sub(r'',review)
    
    # removing puntuations 
    review = review.translate(table)
    
    # remove digits 
    review = review.translate(remove_digits)
    
    #lower case all letters 
    review = review.lower()
    
    #replace multiple white space with single space
    review = MULTIPLE_WHITESPACE.sub(" ",review).strip()
    
    
    #remove stopwords
    final_stopwords = make_stopwords()
    
    review = [word for word in review.split()
             if word not in final_stopwords]
   #stemming 

    review = ' '.join([stemmer.stem(word) for word in review])
    
    return review 