# NewsSnap - News Website Fully Functional and Responsive with Backend Framework Django
#### #django-newswebsite
NewsSnap is a news aggregation website built using Django that provides users with concise and easy-to-read summaries of news articles from various sources. With its intuitive user interface and advanced backend algorithms, NewsSnap makes it easy for users to stay informed without having to read through lengthy articles.

## Setup
- ```git clone https://github.com/ShahStavan/NewsSnap.git```
- ```cd NewsSnap```
- Enable Virtual Environement in Python
  ```python -m venv env```
- Installing Packages(Requires approx. 1Gb internet for installing all packages)
  ```pip install -r requirements.txt.```
- Starting Django server
  ```python manage.py runserver```
  
 ## Python Packages which is used in Project with it's description
  1. GnewsClient ==> For fetching all the details related to news as an instance News Headline, News Url, News Description, etc..
  2. Newspaper3k ==> For scraping article content by providing News Url from above GnewsClient json data.
  3. yfinance ==> For fetching stock data
  4. spacy ==> NLP model for summarizing article
  5. pytextrank ==> This module will assign rank to all the news content scraped from url and the most ranked text will be displayed to user.
  
 ## Main Summarizer Module Code
 ```python
 def summarizer_creator(text):
    # print("The summarized content is: ")
    nlp = spacy.load("en_core_web_lg")
    # en_core_web_lg this is a model
    nlp.add_pipe("textrank")
    doc = nlp(text)
    # change "string" to "text"
    # limit_sentences takes top sentences
    # limit_phrases = 2
    for sent in doc._.textrank.summary(limit_sentences=2):
        return str(sent)
 ```
  
