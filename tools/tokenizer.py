import re

class Tokenizer:
    def tokenize(text: str):
        print(f"Starting tokenization of {len(text)} characters")
        
        result = re.split(r'([,.]|\s)', text)
        pre_processed = [item.strip() for item in result if item.strip()]
        
        all_words = sorted(set(pre_processed))
        vocab = {token:integer for integer,token in enumerate(all_words)}
        
        return vocab
