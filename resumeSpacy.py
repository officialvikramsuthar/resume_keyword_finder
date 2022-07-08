import spacy
model_path = '/kaggle/input/resume-named-entity-recognizer/model'
import string
from textblob import TextBlob
from spacy.lang.en.stop_words import STOP_WORDS
string.punctuation
import nltk
#nltk.download('wordnet')
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer,PorterStemmer
from nltk.corpus import stopwords
import re
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer() 

try:
    import PyPDF2
    import pdfplumber
    import requests
    import json
except Exception:
    pass

class Resume(object):
    def __init__(self, filename=None):
        self.filename = filename
        
    def get(self):
        """
        
        """
        fFileObj = open(self.filename, 'rb')
        pdfReader = PyPDF2.PdfFileReader(fFileObj)
        pageObj = pdfReader.getPage(0)
        print("Total Pages : {} ".format(pdfReader.numPages))

        resume = pageObj.extractText()
        text = ""
        with pdfplumber.open("resume.pdf") as pdf:
             for i in range(len(pdf.pages)):
                    first_page = pdf.pages[i]
                    text = text + first_page.extract_text()
        
        return text

def preprocess(sentence):
    sentence=str(sentence)
    sentence = sentence.lower()
    sentence=sentence.replace('{html}',"") 
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', sentence)
    rem_url=re.sub(r'http\S+', '',cleantext)
    rem_num = re.sub('[0-9]+', '', rem_url)
    tokenizer = RegexpTokenizer(r'\w+')
    stop_words = set(STOP_WORDS)
    tokens = tokenizer.tokenize(rem_num)  
    filtered_words = [w for w in tokens if len(w) > 2 if not w in stop_words]
    stem_words=[stemmer.stem(w) for w in filtered_words]
    lemma_words=[lemmatizer.lemmatize(w) for w in stem_words]
    return " ".join(filtered_words)

resume = Resume(filename="resume.pdf")
response_news = resume.get()
response_news =  preprocess(response_news)
model_path = '.\model'
print("Loading from", model_path)
model = spacy.load(model_path)
resume = model(response_news)
print("Entities", [(ent.text, ent.label_) for ent in resume.ents])


