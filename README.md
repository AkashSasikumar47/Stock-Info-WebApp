# Stock-Info-WebApp 📈📰

Stock-Info-WebApp is a Flask-based web application that allows you to retrieve financial data and recent news articles for a given stock symbol. Stay informed about your favorite stocks with real-time insights into Earnings Per Share (EPS), Price-to-Earnings (P/E) Ratio, Dividend Yield, and access the latest stock news.

## Features

- Retrieve essential financial data for a stock.
- Access the top 5 recent news articles related to the stock.
- User-friendly web interface for easy data retrieval.

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- requests

### Installation

1. Clone the repository:

   ```bash
   https://github.com/AkashSasikumar47/Stock-Info-WebApp.git

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt

3. Set up your API keys:
    
    Replace ALPHA_VANTAGE_API_KEY and NEWS_API_KEY in the financial_data.py file with your actual API keys.

4. Run the application:

    ```bash
    python app.py

5. Access the web app in your browser at http://localhost:5000.

## Usage

- Enter a stock symbol in the input field and click "Get Financial Data" to retrieve information.
- View fundamental data such as EPS, P/E Ratio, and Dividend Yield.
- See recent news articles related to the stock.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments

- Alpha Vantage API
- News API