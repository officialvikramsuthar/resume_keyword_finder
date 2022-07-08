try:
    import spacy
    import json
    import string
    from textblob import TextBlob
    from spacy.lang.en.stop_words import STOP_WORDS
    string.punctuation
    import nltk
    nltk.download('wordnet')
    from nltk.tokenize import RegexpTokenizer
    from nltk.stem import WordNetLemmatizer,PorterStemmer
    from nltk.corpus import stopwords
    import re
    lemmatizer = WordNetLemmatizer()
    stemmer = PorterStemmer()   
except Exception as e:
    print(e)
    

class EntityGenerator(object):
    
    _slots__ = ['text']
    
    def __init__(self, text=None):
        self.text = text
        
    def get(self):
        """
        Return a Json
        """
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(self.text)
        text = [ent.text for ent in doc.ents]
        entity = [ent.label_ for ent in doc.ents]
    
        from collections import Counter
        import json

        data = Counter(zip(entity))
        unique_entity = list(data.keys())
        unique_entity = [x[0] for x in unique_entity]

        d = {}
        for val in unique_entity:
            d[val] = []

        for key,val in dict(zip(text, entity)).items():
            if val in unique_entity:
                d[val].append(key)
        return d

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
        with pdfplumber.open("rotated_example.pdf") as pdf:
             for i in range(len(pdf.pages)):
                    first_page = pdf.pages[i]
                    text = text + first_page.extract_text()
        
        return text
            
        #return resume
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

resume = Resume(filename="rotated_example.pdf")
response_news = resume.get()
#response_news = preprocess(response_news)
helper = EntityGenerator(text=response_news)
response = helper.get()
print(json.dumps(response , indent=3))