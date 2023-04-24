from django.shortcuts import render
import json
# urllib.request to make a request to api
import urllib.request
import yfinance as yf
from nsetools import Nse
import requests
import spacy
import pytextrank
from newspaper import Article
from gnewsclient import gnewsclient
from gnews import GNews



def index(request):
    # city = 'Ahmedabad'
    # source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=imperial&appid=164fec96a27b97680ee442e489ce3f06').read()
    # converting JSON data to a dictionary
    # list_of_data = json.loads(source)

    # data for variable list_of_data
    # data = {
    #    "temp": str(list_of_data['main']['temp']) + 'k',
    # }
    google = yf.Ticker('GOOGL').info
    microsoft = yf.Ticker('MSFT').info
    tesla = yf.Ticker('TSLA').info
    apple = yf.Ticker('AAPL').info
    amazon = yf.Ticker('AMZN').info
    netflix = yf.Ticker('NFLX').info

    stockdata = {
        "google": google['regularMarketPreviousClose'],
        "microsoft": microsoft['regularMarketPreviousClose'],
        "tesla": tesla['regularMarketPreviousClose'],
        "apple": apple['regularMarketPreviousClose'],
        "amazon": amazon['regularMarketPreviousClose'],
        "netflix": netflix['regularMarketPreviousClose'],
    }
    get_top_news = get_hot_news()
    news_technology_article, news_business_article, news_entertainment_article, news_health_article, news_science_article, news_sports_article = top_3_news_category()
    
    return render(request, 'index.html', {'stockdata': stockdata, 'news_technology_article': news_technology_article, 'news_business_article': news_business_article, 'news_entertainment_article': news_entertainment_article, 'news_health_article': news_health_article, 'news_science_article': news_science_article, 'news_sports_article': news_sports_article, 'get_top_news': get_top_news})


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

def get_hot_news():
    client = gnewsclient.NewsClient(language='english', location='india', topic='Nation', max_results=4)
    articles = client.get_news()
    news_dict = {}
    # Get index 0 article details 
    counter = 0
    for article in articles:
        url = article['link']
        if url == None:
            counter+=1
            continue
        else:
            news_dict['headline'] = article['title']
            # news_dict['description'] = article['description']
            a = Article(url)
            a.download()
            a.parse()
            news_dict['description'] = summarizer_creator(a.text)
            news_dict['url'] = article['link']
            break
    print(news_dict)
    return news_dict



def top_3_news_category():
    topics = ['technology', 'business', 'entertainment', 'health', 'science', 'sports']
    news_technology_article = []
    news_business_article = []
    news_entertainment_article = []
    news_health_article = []
    news_science_article = []
    news_sports_article = []
    
    # keyword = str(keyword)
    # Loop through each category and source and retrieve the articles that contain the keyword
    
    for topic in topics:
        counter = 1
        client = gnewsclient.NewsClient(language='english', location='india', topic=topic, max_results=3, use_opengraph=True)
        articles = client.get_news()
        for article in articles:
            article_dict = {}
            if topic == 'technology':
                url = article['url']
                description = article['description']
                image = article['image']
                if url == None and description == None and image == None:
                    continue
                else:
                    if len(news_technology_article) == 2:
                        break
                        counter = 1
                    else:
                        article_dict['id'] = counter
                        article_dict['headline'] = article['title']
                        article_dict['description'] = article['description']
                        article_dict['category'] = topic
                        article_dict['url'] = article['url']
                        article_dict['image'] = article['image']
                        article['site_name'] = article['site_name']
                        news_technology_article.append(article_dict)
                        counter += 1
            elif topic == 'business':
                url = article['url']
                description = article['description']
                if url == None and description == None:
                    continue
                else:
                    if len(news_business_article) == 2:
                        break
                        counter = 1
                    else:
                        article_dict['id'] = counter
                        article_dict['headline'] = article['title']
                        article_dict['description'] = article['description']
                        article_dict['category'] = topic
                        article_dict['url'] = article['url']
                        article_dict['image'] = article['image']
                        article['site_name'] = article['site_name']
                        news_business_article.append(article_dict)
                        counter += 1
            elif topic == 'entertainment':
                url = article['url']
                description = article['description']
                if url == None and description == None:
                    continue
                else:
                    if len(news_entertainment_article) == 2:
                        break
                        counter = 1
                    else:
                        article_dict['id'] = counter
                        article_dict['headline'] = article['title']
                        article_dict['description'] = article['description']
                        article_dict['category'] = topic
                        article_dict['url'] = article['url']
                        article_dict['image'] = article['image']
                        article['site_name'] = article['site_name']
                        news_entertainment_article.append(article_dict)
                        counter += 1
            elif topic == 'health':
                url = article['url']
                description = article['description']
                if url == None and description == None:
                    continue
                else:
                    if len(news_health_article) == 2:
                        break
                        counter = 1
                    else:
                        article_dict['id'] = counter
                        article_dict['headline'] = article['title']
                        article_dict['description'] = article['description']
                        article_dict['category'] = topic
                        article_dict['url'] = article['url']
                        article_dict['image'] = article['image']
                        article['site_name'] = article['site_name']
                        news_health_article.append(article_dict)
                        counter += 1
            elif topic == 'science':
                url = article['url']
                description = article['description']
                if url == None and description == None:
                    continue
                else:
                    if len(news_science_article) == 2:
                        break
                        counter = 1
                    else:
                        article_dict['id'] = counter
                        article_dict['headline'] = article['title']
                        article_dict['description'] = article['description']
                        article_dict['category'] = topic
                        article_dict['url'] = article['url']
                        article_dict['image'] = article['image']
                        article['site_name'] = article['site_name']
                        news_science_article.append(article_dict)
                        counter += 1
            elif topic == 'sports':
                url = article['url']
                description = article['description']
                if url == None and description == None:
                    continue
                else:
                    if len(news_sports_article) == 2:
                        break
                        counter = 1
                    else:
                        article_dict['id'] = counter
                        article_dict['headline'] = article['title']
                        article_dict['description'] = article['description']
                        article_dict['category'] = topic
                        article_dict['url'] = article['url']
                        article_dict['image'] = article['image']
                        article['site_name'] = article['site_name']
                        news_sports_article.append(article_dict)
                        counter += 1
    return news_technology_article, news_business_article, news_entertainment_article, news_health_article, news_science_article, news_sports_article


def technology(request):
    articles_list = all_category_articles('technology')
    return render(request, 'technology.html', {'articles_list': articles_list})

def business(request):
    articles_list = all_category_articles('business')
    return render(request, 'business.html', {'articles_list': articles_list})


def entertainment(request):
    articles_list = all_category_articles('entertainment')
    return render(request, 'entertainment.html', {'articles_list': articles_list})


def health(request):
    articles_list = all_category_articles('health')
    return render(request, 'health.html', {'articles_list': articles_list})


def science(request):
    articles_list = all_category_articles('science')
    return render(request, 'science.html', {'articles_list': articles_list})

def sports(request):
    articles_list = all_category_articles('sports')
    return render(request, 'sports.html', {'articles_list': articles_list})

    
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
    

def summarizer(request):
    try:
        if request.method == "POST":
            news_content = request.POST.get('news_content')
            summary = summarizer_creator(news_content)
            #print(summary)
            return render(request, 'summarizer.html', {'summary': summary})
    except:
        return render(request, 'summarizer.html', {'summary': 'Please enter some text to summarize.'})
    return render(request, 'summarizer.html')
