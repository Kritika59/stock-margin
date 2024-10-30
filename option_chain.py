import requests
import pandas as pd
from dotenv import load_dotenv
import os
def get_option_chain_data(instrument_name: str, expiry_date: str, side: str) -> pd.DataFrame:
    load_dotenv()  
    access_token = os.getenv('API_ACCESS_TOKEN')  
    url = 'https://api.upstox.com/v2/option/chain'
    params = {
        'instrument_key': f'NSE_INDEX|{instrument_name}',
        'expiry_date': expiry_date
    }
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        option_chain = response.json().get('data', [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()
    data = []
    for item in option_chain:
        strike_price = item['strike_price']
        if side == "PE":  
            bid_price = item['put_options']['market_data'].get('best_bid_price', 0)
            data.append([instrument_name, strike_price, 'PE', bid_price])
        elif side == "CE":  
            ask_price = item['call_options']['market_data'].get('best_ask_price', 0)
            data.append([instrument_name, strike_price, 'CE', ask_price])
    df = pd.DataFrame(data, columns=['instrument_name', 'strike_price', 'side', 'bid/ask'])
    return df
