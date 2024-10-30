# Stock-Margin Project

## Overview
The Stock-Margin project is a Python tool that leverages financial data from Upstox APIs to calculate margin requirements and premium earnings for options trading. It fetches option chain data for a given instrument and expiry date, computes margin and premium values, and exports the data to Excel for easy reference.

## Project Structure
The project consists of two main files:

- **calculate_margin_and_premium.py**: 
  - Fetches margin requirements and calculates premium earned based on lot size.
  - Requires an Upstox API access token and instrument details as inputs.

- **get_option_chain.py**: 
  - Retrieves option chain data using Upstox API and formats it into a structured DataFrame.
  - Exports the option chain data to an Excel sheet for analysis.

## Function: `get_option_chain_data`

### Overview
The `get_option_chain_data` function retrieves option chain data for a specified financial instrument (like NIFTY or BANKNIFTY) on a given expiry date. It fetches the highest bid price for put options (PE) or the highest ask price for call options (CE) and returns this data in a structured Pandas DataFrame.

### Inputs
- **instrument_name**: A string representing the name of the instrument (e.g., 'NIFTY' or 'BANKNIFTY').
- **expiry_date**: A string representing the expiration date of the options in `YYYY-MM-DD` format.
- **side**: A string that indicates the type of option to retrieve. Use "PE" for Put options and "CE" for Call options.

### Returns
- A Pandas DataFrame with the following columns:
  - **instrument_name**: Name of the financial instrument.
  - **strike_price**: The strike price of the options.
  - **side**: The type of option ('PE' or 'CE').
  - **bid/ask**: The highest bid price for PE options or the highest ask price for CE options.

### Code Logic
1. **Environment Variable Loading**:
   - The function utilizes the `dotenv` package to load environment variables from a `.env` file, which is used to securely store the API access token.
   - The access token is retrieved from an environment variable named `API_ACCESS_TOKEN`.

2. **API Request**:
   - Constructs the API endpoint URL and request parameters.
   - Sends a GET request to the Upstox API to retrieve option chain data.
   - Checks for HTTP errors and handles exceptions by printing an error message.

3. **Data Parsing**:
   - Initializes an empty list to store the parsed data.
   - Iterates over the retrieved option chain data:
     - Extracts the strike price and either the best bid price for PE options or the best ask price for CE options.
     - Appends the gathered data to the list in a structured format.

4. **DataFrame Creation**:
   - Converts the list of option data into a Pandas DataFrame and returns it.
## AI Tools Used
In this project, the following AI tools were utilized to assist with development and data analysis:

- **ChatGPT (OpenAI)**: This AI language model was used for code suggestions, troubleshooting, and generating documentation. It helped clarify concepts related to APIs and stock trading, provided explanations on how to structure the code, and guided the creation of a comprehensive README file.

## Understanding APIs, Stocks, and Upstox

### What is an API?
- **API (Application Programming Interface)**: An API allows different software applications to communicate with each other. In the context of Upstox, the API lets you programmatically access stock market data and perform trading operations without manually using the Upstox web or mobile interface.

### Understanding Stocks and Options
- **Stocks**: When you buy shares of a company, you own a small piece of that company. The value of your shares can go up or down based on the company’s performance and market conditions.
  
- **Options**: These are financial derivatives that give you the right, but not the obligation, to buy or sell an underlying asset (like stocks) at a predetermined price before or at the expiration date. Options come in two types:
  - **Call Options (CE)**: Gives the holder the right to buy the underlying asset.
  - **Put Options (PE)**: Gives the holder the right to sell the underlying asset.

### Using Upstox for Options Trading
1. **Account Setup**: You need an Upstox trading account to access their API. Once your account is set up, you can generate an API access token.

2. **Fetching Data**: Using the Upstox API, you can retrieve various data:
   - **Option Chain Data**: This includes all available options for a particular underlying asset. It shows strike prices, bid/ask prices, volume, open interest, and other relevant data.
   - **Market Data**: You can also access current stock prices, historical data, and market trends.

3. **Analysis**: Once you have the option chain data, you can perform various analyses, such as:
   - **Volatility Analysis**: Understanding how much the price of the underlying asset may fluctuate.
   - **Open Interest Analysis**: Gauging market sentiment and potential price movements based on the number of open contracts.
   - **Profit/Loss Calculations**: Estimating potential profits or losses based on different scenarios.

### Code’s Role
In this project, the provided code accomplishes the following:
- **Data Retrieval**: The code retrieves option chain data from the Upstox API based on the specified instrument (like NIFTY) and expiry date.
- **Margin and Premium Calculations**: It calculates the margin required for trading options and the premium earned from selling options.

### Further Learning
To improve your understanding, consider:
- **Reading Resources**: Look for articles or books on stock trading, especially focusing on options trading strategies.
- **API Documentation**: Check Upstox's API documentation for detailed information on how to use their endpoints.
- **Online Courses**: Many platforms offer courses on stock trading, options trading, and using APIs in Python.


### Example Usage
```python
from get_option_chain import get_option_chain_data

# Example function call
df = get_option_chain_data('NIFTY', '2024-06-19', 'PE')
print(df)
Environment Variables
To use this function, ensure you have a .env file in your project directory with the following structure:

makefile
Copy code
API_ACCESS_TOKEN=your_access_token_here
Usage
To use the functions, ensure your environment is configured as follows:

Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the scripts:

python
Copy code
from calculate_margin_and_premium import calculate_margin_and_premium
from get_option_chain import get_option_chain_data
Create an .env file in the project root with the following structure:

makefile
Copy code
API_ACCESS_TOKEN=your_access_token_here
Conclusion
This project provides an efficient way to access and analyze option chain data for financial instruments, helping traders make informed decisions based on margin and premium calculations.

