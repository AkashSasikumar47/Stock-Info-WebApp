from flask import Flask, render_template, request
from financial_data import get_stock_data, get_stock_news

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get_data", methods=["POST"])
def get_data():
    if request.method == "POST":
        stock_symbol = request.form["stock_symbol"]
        eps, pe_ratio, dividend_yield = get_stock_data(stock_symbol)
        articles = get_stock_news(stock_symbol)

        # Limit the number of articles to the top 5
        top_5_articles = articles[:5]

        return render_template(
            "result.html",
            stock_symbol=stock_symbol,
            eps=eps,
            pe_ratio=pe_ratio,
            dividend_yield=dividend_yield,
            articles=top_5_articles,  # Use the top 5 articles here
        )


if __name__ == "__main__":
    app.run(debug=True)
