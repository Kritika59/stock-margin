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

sql
Copy code

Feel free to copy this Markdown code into a file named `README.md` in your GitH
