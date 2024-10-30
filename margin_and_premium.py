import requests
import pandas as pd
from dotenv import load_dotenv
import os
def calculate_margin_and_premium(data: pd.DataFrame, lot_size: int = 50) -> pd.DataFrame:
    load_dotenv()  
    access_token = os.getenv('API_ACCESS_TOKEN')  
    margin_url = 'https://api.upstox.com/v2/margin/requirement'
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }
    margin_required = []
    premium_earned = []

    for _, row in data.iterrows():
        strike_price = row['strike_price']
        side = row['side']
        bid_ask_price = row['bid/ask']
        margin_params = {
            'instrument_key': f"NSE_OPTION|{row['instrument_name']}|{strike_price}|{side}",
            'transaction_type': 'SELL'
        }
        try:
            response = requests.get(margin_url, params=margin_params, headers=headers)
            response.raise_for_status()
            margin = response.json().get('margin', {}).get('required', 0)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching margin: {e}")
            margin = 0  
        premium = bid_ask_price * lot_size
        margin_required.append(margin)
        premium_earned.append(premium)
    data['margin_required'] = margin_required
    data['premium_earned'] = premium_earned
    return data
