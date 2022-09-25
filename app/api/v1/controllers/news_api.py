from newsapi import NewsApiClient

class NewsApiContentProvider:
    client = None
    apiKey = None

    def init_client(self, apiKey: str):
        if self.client is None:
            self.client = NewsApiClient(apiKey)
            self.apiKey = apiKey

    def top_headlines(self, category=None, language="en", country=None, page=1):
        top_headlines = self.client.get_top_headlines(
            category=category,
            language=language,
            country=country,
            page=page
        )

        for article in top_headlines['articles']:
            if article['content'] is None:
                article['content'] = "No content available"
            if len(article['content']) > 150:
                article['content'] = article['content'][:150] + '...'

        return top_headlines['articles']
    