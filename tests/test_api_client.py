# tests/test_api_client.py

import pytest
from src.api_client import OpenAIApiClient

def test_preprocess_text():
    client = OpenAIApiClient()

    # Test URL removal
    text = "Visit https://example.com for more info."
    expected = "Visit  for more info."
    assert client.preprocess_text(text) == expected

    # Test non-alphabetic character removal
    text = "Hello, World! 123"
    expected = "Hello World "
    assert client.preprocess_text(text) == expected

    # Test conversion to lowercase
    text = "Hello World"
    expected = "hello world"
    assert client.preprocess_text(text) == expected

def test_generate_text():
    client = OpenAIApiClient()

    # Test text generation
    prompt = "Translate the following English text to French: '{}'"
    text = "Hello, World!"
    response = client.generate_text(prompt.format(text))

    # We can't predict the exact output, but we can check that it's not empty
    assert len(response) > 0

# Run the tests
if __name__ == "__main__":
    pytest.main()
