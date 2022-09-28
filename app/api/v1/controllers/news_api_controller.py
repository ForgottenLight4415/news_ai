from flask import jsonify
from threading import Thread
from newsapi import NewsApiClient
from newspaper import Article, ArticleException, Config

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
config = Config()
config.browser_user_agent = user_agent
config.request_timeout = 10
print("Plugin configured")


def make_summary(article: dict):
    try:
        print("Connecting to: ", article['url'])
        news_article = Article(article['url'], config=config)
        news_article.download()
        news_article.parse()
        news_article.nlp()
        article['content'] = news_article.summary
    except ArticleException as e:
        print("An error occurred while making summary from ", article['url'])
        print(e)
        article['content'] = "Couldn't fetch summary"


def make_next_url(category, language, country, page, total_results, next=True):
    next_url = 'http://localhost:5000/'
    first_param_set = False

    if category or language or country or page:
        next_url += "?"
    else:
        return next_url

    if category:
        next_url += "category=" + category
        first_param_set = True

    if language:
        if first_param_set:
            next_url += "&"
        else:
            first_param_set = True
        next_url += "language=" + language

    if country:
        if first_param_set:
            next_url += "&"
        else:
            first_param_set = True
        next_url += "country=" + country
    
    if page:
        if first_param_set:
            next_url += "&"
        else:
            first_param_set = True
        if next:
            if page != total_results:
                next_url += "page=" + str(page + 1)
            else:
                next_url += "page=" + str(1)
        else:
            if page == 1:
                next_url += "page=" + str(total_results)
            else:
                next_url += "page=" + str(page - 1)

    return next_url
    


class NewsApiContentProvider:
    client = None
    apiKey = None

    def init_client(self, api_key: str):
        if self.client is None:
            self.client = NewsApiClient(api_key)
            self.apiKey = api_key

    def top_headlines(self, category=None, language="en", country=None, page=1, endpoint="web"):
        top_headlines = self.client.get_top_headlines(
            category=category,
            language=language,
            country=country,
            page=int(page)
        )

        if category:
            top_headlines['category'] = " in " + category.capitalize()
        else:
            top_headlines['category'] = ''

        top_headlines['next_url'] = make_next_url(category, language, country, int(page), top_headlines['totalResults'])
        top_headlines['prev_url'] = make_next_url(category, language, country, int(page), top_headlines['totalResults'], next=False)

        thread_pool = []
        for article in top_headlines['articles']:
            thread_pool.append(Thread(target=make_summary, args=(article,)))

        for thread in thread_pool:
            thread.start()

        for thread in thread_pool:
            thread.join()

        top_headlines['page'] = page

        if endpoint == "web":
            return top_headlines
        elif endpoint == "api":
            return jsonify(top_headlines)
        else:
            return "<p>Invalid endpoint</p>"
