from tools.tokenizer import Tokenizer


def test_tokenize_returns_vocab_with_unique_ids():
    vocab = Tokenizer.tokenize("Hello, world.  This is\na test.")

    assert vocab == {
        ",": 0,
        ".": 1,
        "Hello": 2,
        "This": 3,
        "a": 4,
        "is": 5,
        "test": 6,
        "world": 7,
    }


def test_tokenize_assigns_one_id_per_unique_token():
    vocab = Tokenizer.tokenize("one one   two\t\tthree two")

    assert vocab == {"one": 0, "three": 1, "two": 2}


def test_tokenize_prints_progress(monkeypatch):
    input_text = "x"
    calls = []

    def fake_print(*args, **kwargs):
        calls.append((args, kwargs))

    monkeypatch.setattr("builtins.print", fake_print)
    Tokenizer.tokenize(input_text)

    assert calls == [((f"Starting tokenization of {len(input_text)} characters",), {})]
