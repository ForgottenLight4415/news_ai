from newsapi import NewsApiClient
from flask import jsonify
from newspaper import Article, ArticleException, news_pool

class NewsApiContentProvider:
    client = None
    apiKey = None

    def init_client(self, apiKey: str):
        if self.client is None:
            self.client = NewsApiClient(apiKey)
            self.apiKey = apiKey

    def top_headlines(self, category=None, language="en", country=None, page=1, endpoint="web"):
        top_headlines = self.client.get_top_headlines(
            category=category,
            language=language,
            country=country,
            page=page
        )

        for article in top_headlines['articles']:
            print("Connecting to: " + article['url'])
            try:
                news_article = Article(article['url'])
                news_article.download()
                news_article.parse()
                news_article.nlp()
                if news_article.text is None:
                    article['content'] = "No content available"
                else:
                    article['content'] = news_article.summary
            except ArticleException as e:
                article['content'] = "An error occurred while getting this article"

        top_headlines['page'] = page

        if endpoint == "web":
            return top_headlines
        elif endpoint == "api":
            return jsonify(top_headlines)
        else:
            return "<p>Invalid endpoint</p>"
    