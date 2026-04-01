import re

class Tokenizer:
    def tokenize(text: str):
        print(f"Starting tokenization of {len(text)} characters")
        result = re.split(r'([,.]|\s)', text)
        return [item.strip() for item in result if item.strip()]
