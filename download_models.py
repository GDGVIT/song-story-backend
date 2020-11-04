import torch
import pickle
from transformers import GPT2LMHeadModel, GPT2Tokenizer, GPT2Config
from transformers import T5Tokenizer, T5ForConditionalGeneration


if __name__ == "__main__":
        print("[INFO] Downloading tokenizers")
        gpt2_tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        pickle.dump(gpt2_tokenizer, open('./models/tokenizer.pkl', 'wb'))
        print("[INFO] Done ...")
        
        print("[INFO] Downloading GPT2")
        gpt2_model = GPT2LMHeadModel.from_pretrained(
            "gpt2", pad_token_id=gpt2_tokenizer.eos_token_id
        )
        gpt2_model.save_pretrained('./models/open-ai-gpt2')
        print("[INFO] Done ...")
        