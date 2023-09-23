import requests

# Replace these placeholders with your actual API keys
ALPHA_VANTAGE_API_KEY = "C8JO1J71Z298XT2S"


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
