import spacy
import re
import string
import json

class SpacyModel:
    '''
    This is class for spacy language model
    and its associated functions
    '''
    def __init__(self):
        
        # Load NLP model
        self.nlp = spacy.load('en_core_web_md',disable=['ner','tagger'])

        # Load Clist
        with open('./clist.json') as f:
            self.cList = json.load(f) 

        self.c_re = re.compile('(%s)' % '|'.join(self.cList.keys()))
    
    def sentencize(self, text):
        '''
        This function splits text to sentences
        '''
        
        doc = self.nlp(text)
        
        return [sent.text for sent in doc.sents]
    
    def sent_sim(self, text1, text2):
        '''
        This function returns similarity between two documents
        '''
        
        doc1 = self.nlp(text1)
        doc2 = self.nlp(text2)
        
        return doc1.similarity(doc2)
    
    def clean_text(self, text):
        '''
        This function cleans text
        '''
        text = text.strip()
        doc = self.nlp(text)
        tokens = [token.text for token in doc if token.text.isalpha() or token.text in string.punctuation]
        return ' '.join(tokens)

    def expandContractions(self, text):
        '''
        This function expands contractions
        '''
        def replace(match):
            return self.cList[match.group(0)]
        return c_re.sub(replace, text.lower())
    
nlp = SpacyModel()

def get_spacy():
    return nlp