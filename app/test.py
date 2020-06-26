import spacy
import torch
from core.nlu.spacy import SpacyModel
from core.summarizer.textrank import TextRank
from core.language.gpt2 import GPT2
from transformers import GPT2LMHeadModel, GPT2Tokenizer, GPT2Config


if __name__ == "__main__":
    # Load models
    print("[INFO] Loading models")

    # Loading spacy
    nlp = spacy.load('en_core_web_md', disable=['ner','tagger'])

    # Loading GPT2
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

    # add the EOS token as PAD token to avoid warnings
    model = GPT2LMHeadModel.from_pretrained("gpt2", pad_token_id=tokenizer.eos_token_id)

    # Initializing classes
    print("[INFO] Initializing classes")
    spacy_model = SpacyModel(nlp)
    gpt2 = GPT2(tokenizer, model)

    # Summarize text
    print("[INFO] Summarizing text")
    text = open('./data/coldplay.txt').read()
    summarizer = TextRank(spacy_model)
    summary = summarizer.summarize(text, 1)

    # Generate language
    print("[INFO] Generating story")
    story = gpt2.get_story(summary, 60)

    print("STORY")
    print("-"*50)

    print(story)