from flask import Flask, render_template, request
from financial_data import get_stock_data

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get_data", methods=["POST"])
def get_data():
    if request.method == "POST":
        stock_symbol = request.form["stock_symbol"]
        eps, pe_ratio, dividend_yield = get_stock_data(stock_symbol)

        return render_template(
            "result.html",
            stock_symbol=stock_symbol,
            eps=eps,
            pe_ratio=pe_ratio,
            dividend_yield=dividend_yield,
        )


if __name__ == "__main__":
    app.run(debug=True)
