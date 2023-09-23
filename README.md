# Stock-Info-WebApp 📈📰

This is a simple web app built with Flask that allows users to retrieve financial data for a given stock symbol. The app utilizes the Alpha Vantage API to fetch stock-related information such as Earnings Per Share (EPS), Price-to-Earnings (P/E) ratio, and Dividend Yield.

## Features

- **Stock Data Retrieval**: Retrieve essential financial data for a given stock symbol, including Earnings Per Share (EPS), Price-to-Earnings (P/E) ratio, and Dividend Yield.

- **User-Friendly Interface**: The web app provides a simple and intuitive interface for users to enter stock symbols and view financial information.

- **Customizable**: Easily customize the app by adding more features or modifying the frontend to meet your specific requirements.

- **Contributions Welcome**: Open to contributions from the community. Feel free to contribute to the project by submitting issues or pull requests.


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
    
    Replace **ALPHA_VANTAGE_API_KEY** in the financial_data.py file with your actual API key.

4. Run the application:

    ```bash
    python app.py

5. Access the web app in your browser at http://localhost:5000.

## Usage

- Enter a stock symbol in the provided input field on the homepage.
- Click the "Get Data" button.
- The app will fetch and display information about the stock, including Earnings Per Share (EPS), Price-to-Earnings (P/E) ratio, and Dividend Yield on the result page.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments

**Alpha Vantage API**