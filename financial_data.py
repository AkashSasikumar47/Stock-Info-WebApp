import requests

# Replace these placeholders with your actual API keys
ALPHA_VANTAGE_API_KEY = "API Key"
NEWS_API_KEY = "API Key"


def get_stock_data(stock_symbol):
    alpha_vantage_url = f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={stock_symbol}&apikey={ALPHA_VANTAGE_API_KEY}"

    try:
        response = requests.get(alpha_vantage_url)
        data = response.json()

        earnings_per_share = data.get("EPS")
        pe_ratio = data.get("PERatio")
        dividend_yield = data.get("DividendYield")

        return earnings_per_share, pe_ratio, dividend_yield

    except Exception as e:
        return None, None, None


def get_stock_news(stock_symbol):
    news_api_url = f"https://newsapi.org/v2/everything?q={stock_symbol}&apiKey={NEWS_API_KEY}&sortBy=publishedAt"

    try:
        response = requests.get(news_api_url)
        data = response.json()

        articles = data.get("articles", [])

        return articles

    except Exception as e:
        return []


# This code will now be used as a module in app.py
