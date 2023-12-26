# SentimentAnalyzer

SentimentAnalyzer is a Python module that uses the OpenAI API to perform sentiment analysis on text data.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install SentimentAnalyzer.

```bash
pip install -r requirements.txt
```

## Usage

```python
from src.sentiment_analyzer import SentimentAnalyzer

# Create an instance of the SentimentAnalyzer
analyzer = SentimentAnalyzer()

# Analyze sentiment of a text
result = analyzer.analyze_sentiment("This is a sample text.")
print(result)
```

For more detailed usage instructions, please refer to the [usage_instructions.md](docs/usage_instructions.md) file.

## Running the tests

The tests for the SentimentAnalyzer can be run using pytest.

```bash
pytest tests/
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions, feel free to contact the author at your.email@example.com.
