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
 ## Fetching News Data based on Category:
 ```python
 # In the parameter you need to pass category for fetching specific category news
 # Categories Available: Nation, World, Business, Health, Entertainment, Sports, Science and Technology
 # Want to read full code? Check it in following path: news/views.py file
 def all_category_articles(category):
    category = category
    response = client = gnewsclient.NewsClient(language='english', location='india', topic=category, max_results=10, use_opengraph=True)
    articles = client.get_news()
    articles_list = []
    counter = 1
    

    for article in articles:
        if len(articles_list) < 4:
            url = article['url']
            description = article['description']
            image = article['image']
            if url == None and description == None and image == None:
                continue
            else:
                # create a dictionary to store the article information
                article_dict = {}

                # get the headline, description, and content of the article
                article_dict['id'] = counter
                article_dict['headline'] = article['title']
                article_dict['description'] = article['description']
                article_dict['category'] = category
                article_dict['url'] = article['url']
                article_dict['image'] = article['image']
                #article['site_name'] = article['site_name']
                article = Article(article_dict['url'])
                article.download()
                article.parse()
                content = article.text

                if content != None:
                    article_dict['content'] = content
                    article_dict['summary'] = summarizer_creator(content)
                else:
                    article_dict['content'] = "Content not available"
                    article_dict['summary'] = "Content not available"
                print(article.text)
                # append the article dictionary to the list
                articles_list.append(article_dict)
                counter += 1

        # limit the number of articles to 20
        else:
            counter = 1
            break
    for article in articles_list:
        print("ID:", article['id'])
        print("Headline:", article['headline'])
        print("Description:", article['description'])
        print("Category:", article['category'])
        print("URL:", article['url'])
        print("Image:", article['image'])
        # print("Content:", article['content'])
        print("Summary:", article['summary'])
        # print("Site Name:", article['site_name'])
        print("---------------------------------------------------------------")
        print("\n")
        
    return articles_list
 ```
  
