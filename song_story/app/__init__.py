import spacy
import torch
import random
from .core.nlu.spacy import SpacyModel, get_spacy
from .core.summarizer.textrank import TextRank
from .core.language.gpt2 import Model, get_model
from .genius.artist import Artist
from .genius import Client, get_client

from transformers import GPT2LMHeadModel, GPT2Tokenizer, GPT2Config

from fastapi import FastAPI, Depends
from pydantic import BaseModel

app = FastAPI()


class StoryRequest(BaseModel):
    name: str


@app.get("/")
def status():
    return {"status": "success", "message": "Server up and running"}


@app.get("/story")
def get_story(
    request: StoryRequest,
    model: Model = Depends(get_model),
    nlp: SpacyModel = Depends(get_spacy),
    client: Client = Depends(get_client),
):

    name = request.name
    artist = client.search_artist(name)

    # Choose a random song
    seed = random.randint(0, len(artist.songs) - 1)

    _id = artist.songs[seed][0]
    title = artist.songs[seed][1]

    context = client.get_referents(_id)

    summarizer = TextRank(nlp)

    prompt = summarizer.summarize(context, 1)

    story = model.story_from_prompt(prompt, 1000)

    return {
        "status": "success",
        "message": "Some story",
        "story": story,
        "title": title,
    }
