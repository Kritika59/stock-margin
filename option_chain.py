import requests
import pandas as pd
from typing import Optional
def get_option_chain_data(
    instrument_name: str, 
    expiry_date: str, 
    access_token: str
) -> pd.DataFrame:
    """
    Retrieve comprehensive option chain data for both PE and CE options.
    
    Parameters:
    -----------
    instrument_name : str
        Instrument key from Upstox (e.g., "NSE_INDEX|Nifty 50")
    expiry_date : str
        Expiration date of the options in YYYY-MM-DD format
    access_token : str
        Authentication token for the Upstox API
    
    Returns:
    --------
    pd.DataFrame
        DataFrame containing option chain data with columns:
        - instrument_name
        - strike_price
        - side (PE/CE)
        - bid/ask
    """
    url = 'https://api.upstox.com/v2/option/chain'
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }
    params = {
        "mode": "option_chain",
        'instrument_key': instrument_name,
        'expiry_date': expiry_date
    }
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()  # Raise an exception for bad responses
        option_chain = response.json().get('data', [])
        if not option_chain:
            print(f"No option chain data found for {instrument_name} on {expiry_date}")
            return pd.DataFrame(columns=['instrument_name', 'strike_price', 'side', 'bid/ask'])
        data_list = []
        for entry in option_chain:
            strike_price = entry['strike_price']
            try:
                put_options = entry.get('put_options', {})
                put_market_data = put_options.get('market_data', {})
                put_bid_price = put_market_data.get('bid_price', None)
                if put_bid_price is not None:
                    data_list.append([
                        instrument_name, 
                        strike_price, 
                        'PE', 
                        put_bid_price
                    ])
                call_options = entry.get('call_options', {})
                call_market_data = call_options.get('market_data', {})
                call_ask_price = call_market_data.get('ask_price', None)
                
                if call_ask_price is not None:
                    data_list.append([
                        instrument_name, 
                        strike_price, 
                        'CE', 
                        call_ask_price
                    ])
            except KeyError as e:
                print(f"Skipping entry due to missing key: {e}")
                continue
        df = pd.DataFrame(data_list, columns=['instrument_name', 'strike_price', 'side', 'bid/ask'])
        df = df.sort_values(['strike_price', 'side'])
        return df
    except requests.RequestException as e:
        print(f"API request error: {e}")
        return pd.DataFrame(columns=['instrument_name', 'strike_price', 'side', 'bid/ask'])
    except Exception as e:
        print(f"Unexpected error: {e}")
        return pd.DataFrame(columns=['instrument_name', 'strike_price', 'side', 'bid/ask'])
if __name__ == "__main__":
    access_token = "YOUR_ACCESS_TOKEN" 
    instrument_name = "NSE_INDEX|Nifty 50"
    expiry_date = "2024-11-07"
    try:
        calculated_data = get_option_chain_data(instrument_name, expiry_date, access_token)
        if not calculated_data.empty:
            print("Option Chain Data:")
            print(calculated_data[['instrument_name', 'strike_price', 'side', 'bid/ask']].to_string(index=False))
            csv_filename = f"option_chain_data_{expiry_date}.csv"
            calculated_data.to_csv(csv_filename, index=False)
            print(f"Data saved to {csv_filename}")
            print(f"\nTotal entries: {len(calculated_data)}")
            pe_data = calculated_data[calculated_data['side'] == 'PE']
            ce_data = calculated_data[calculated_data['side'] == 'CE']
            
            print("\nPut Options (PE) Summary:")
            print(pe_data.describe())
            
            print("\nCall Options (CE) Summary:")
            print(ce_data.describe())
        else:
            print("No option data retrieved.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
