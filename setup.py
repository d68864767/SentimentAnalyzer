# setup.py

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="SentimentAnalyzer",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A sentiment analysis tool using OpenAI API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/SentimentAnalyzer",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'numpy==1.21.2',
        'pandas==1.3.3',
        'openai==0.27.0',
        'nltk==3.6.2',
        'pytest==6.2.5',
        'requests==2.26.0',
    ],
)
