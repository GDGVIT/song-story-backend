import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer, GPT2Config

class Model:
    '''
    This class provides functions to generate text using gpt2 model
    '''

    def __init__(self):
        '''
        Constructor class for GPT2
        '''
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    
        self.model = GPT2LMHeadModel.from_pretrained("gpt2", pad_token_id=self.tokenizer.eos_token_id)
    
    def get_text(self, context, max_length=100):
        '''
        This generates text
        '''
        encoded_input = self.tokenizer.encode(context, return_tensors='pt')
        output = self.model.generate(encoded_input,do_sample=True, max_length=max_length, top_k=50)
        gen_text = self.tokenizer.decode(output[0], skip_special_tokens=True)

        return gen_text
    
    def story(self, prompt, max_length=200):
        '''
        This function puts together the story
        '''
        story = self.get_text(prompt, max_length)
        

        start = story.find('.')
        end = story.rfind('.')

        return story[start+1:end]

model = Model()

def get_model():
    return model