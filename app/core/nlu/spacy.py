import spacy

class Model:
    '''
    This is class for spacy language model
    and its associated functions
    '''
    def __init__(self, nlp):
        
        # Load NLP model
        self.nlp = nlp
    
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