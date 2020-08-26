import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer, GPT2Config


class Model:
    """
    This class provides functions to generate text using gpt2 model
    """

    def __init__(self):
        """
        Constructor class for GPT2
        """
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

        self.model = GPT2LMHeadModel.from_pretrained(
            "gpt2", pad_token_id=self.tokenizer.eos_token_id
        )

    def get_text(self, context, max_length=100):
        """
        This generates text
        """
        encoded_input = self.tokenizer.encode(context, return_tensors="pt")
        output = self.model.generate(
            encoded_input, do_sample=True, max_length=max_length, top_k=50
        )
        gen_text = self.tokenizer.decode(output[0], skip_special_tokens=True)

        return gen_text

    def story_from_prompt(self, prompt, max_length=200):
        """
        This function puts together the story
        """
        story = self.get_text(prompt, max_length)

        start = story.find(".")
        end = story.rfind(".")

        return story[start + 1 : end]

    def story_from_sentences(self, sents, para_len=100):
        """
        Forms story from sentences
        """

        paras = []

        para = ""
        for sent in sents:
            pretext = para
            context = sent
            skip_length = len(pretext) + len(context)
            para = self.get_text(pretext + context, para_len)

            para = para[skip_length:]

            start = para.find(".")
            end = para.rfind(".")

            paras.append(para[start + 1 : end])

        return " ".join(paras)


model = Model()


def get_model():
    return model
