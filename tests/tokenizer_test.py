from tools.tokenizer import Tokenizer


def test_tokenize_splits_words_whitespace_and_commas_periods():
    tokens = Tokenizer.tokenize("Hello, world.  This is\na test.")

    assert tokens == ["Hello", ",", "world", ".", "This", "is", "a", "test", "."]


def test_tokenize_removes_empty_and_whitespace_only_tokens():
    tokens = Tokenizer.tokenize(" one   two\t\tthree ")

    assert tokens == ["one", "two", "three"]


def test_tokenize_prints_progress(monkeypatch):
    input_text = "x"
    calls = []

    def fake_print(*args, **kwargs):
        calls.append((args, kwargs))

    monkeypatch.setattr("builtins.print", fake_print)
    Tokenizer.tokenize(input_text)

    assert calls == [((f"Starting tokenization of {len(input_text)} characters",), {})]
