# Usage Instructions for SentimentAnalyzer

This document provides detailed instructions on how to use the SentimentAnalyzer module.

## Installation

Before using the SentimentAnalyzer, make sure you have installed all the necessary dependencies. You can do this by running the following command in your terminal:

```bash
pip install -r requirements.txt
```

## Setting Up

To use the SentimentAnalyzer, you first need to import it in your Python script. You can do this with the following line of code:

```python
from src.sentiment_analyzer import SentimentAnalyzer
```

Next, create an instance of the SentimentAnalyzer:

```python
analyzer = SentimentAnalyzer()
```

## Analyzing Text

To analyze the sentiment of a piece of text, use the `analyze_text` method. This method takes a string of text as input and returns a dictionary with the sentiment scores:

```python
text = "I love this product!"
sentiment_scores = analyzer.analyze_text(text)
print(sentiment_scores)
```

## Analyzing URL Content

You can also analyze the sentiment of the content of a URL using the `analyze_url` method. This method takes a URL as input and returns a dictionary with the sentiment scores:

```python
url = "http://example.com"
sentiment_scores = analyzer.analyze_url(url)
print(sentiment_scores)
```

## Running Tests

Unit tests for the SentimentAnalyzer and the OpenAIApiClient are located in the `tests/` directory. You can run these tests using the following commands:

```bash
python -m unittest tests/test_analyzer.py
python -m pytest tests/test_api_client.py
```

## Note

Remember to replace `'your_openai_api_key'` in `src/api_client.py` with your actual OpenAI API key.

