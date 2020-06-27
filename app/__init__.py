import spacy
import torch
from .core.nlu.spacy import SpacyModel, get_spacy
from .core.summarizer.textrank import TextRank
from .core.language.gpt2 import Model, get_model
from transformers import GPT2LMHeadModel, GPT2Tokenizer, GPT2Config

from fastapi import FastAPI, Depends 
from pydantic import BaseModel

app = FastAPI()

class StoryRequest(BaseModel):
    name: str


@app.get("/")
def status():
    return {'status':"success", 'message':"Server up and running"}

@app.get('/story')
def get_story(request: StoryRequest, model: Model = Depends(get_model),
                nlp: SpacyModel = Depends(get_spacy)):
    
    
    return {'status':"success", 'message':"Some story"}
