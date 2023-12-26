# tests/test_analyzer.py

import unittest
from unittest.mock import patch, Mock
from src.sentiment_analyzer import SentimentAnalyzer

class TestSentimentAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = SentimentAnalyzer()

    @patch('src.sentiment_analyzer.OpenAIApiClient')
    def test_analyze_text(self, MockApiClient):
        # Mock the preprocess_text method of the API client
        MockApiClient.return_value.preprocess_text.return_value = "This is a test"

        # Mock the polarity_scores method of the SentimentIntensityAnalyzer
        self.analyzer.sia.polarity_scores = Mock(return_value={"neg": 0.0, "neu": 0.0, "pos": 1.0, "compound": 1.0})

        # Test the analyze_text method
        sentiment_scores = self.analyzer.analyze_text("This is a test")
        self.assertEqual(sentiment_scores, {"neg": 0.0, "neu": 0.0, "pos": 1.0, "compound": 1.0})

    @patch('src.sentiment_analyzer.requests.get')
    @patch('src.sentiment_analyzer.OpenAIApiClient')
    def test_analyze_url(self, MockApiClient, MockRequests):
        # Mock the get method of the requests module
        MockRequests.return_value.text = "This is a test"

        # Mock the preprocess_text method of the API client
        MockApiClient.return_value.preprocess_text.return_value = "This is a test"

        # Mock the polarity_scores method of the SentimentIntensityAnalyzer
        self.analyzer.sia.polarity_scores = Mock(return_value={"neg": 0.0, "neu": 0.0, "pos": 1.0, "compound": 1.0})

        # Test the analyze_url method
        sentiment_scores = self.analyzer.analyze_url("http://test.com")
        self.assertEqual(sentiment_scores, {"neg": 0.0, "neu": 0.0, "pos": 1.0, "compound": 1.0})

if __name__ == '__main__':
    unittest.main()
