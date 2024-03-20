import requests
import pandas as pd

class Wallet:

    def __init__(self, address):
        self.address = address
        self.balances = self.get_token_balances(self.address)
        self.dataframe = self.create_dataframe(self.balances, self.address)
    
    def get_token_balances(self, address: str) -> dict:
        url = f'https://api.llamafolio.com/balances/{address}/tokens'
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for 4XX and 5XX status codes
            data = response.json()
            return data
        except requests.exceptions.RequestException as e:
            print(f'Error: {e}')
            return None

    def create_dataframe(self, balances: dict, address: str) -> pd.DataFrame:
        # Initialize lists to store data
        wallets = []
        # chain_ids = []
        chain_names = []
        coin_addresses = []
        symbols = []
        # decimals = []
        # prices = []
        amounts = []
        balance_usds = []

        # Iterate over chains and balances
        for chain in balances['chains']:
            # chain_id = chain['chainId']
            chain_name = chain['id']
            for balance in chain['balances']:
                wallets.append(address)
                # chain_ids.append(chain_id)
                chain_names.append(chain_name)
                coin_addresses.append(balance['address'])
                symbols.append(balance['symbol'])
                # decimals.append(int(balance['decimals']))
                # prices.append(balance.get('price', None))
                # readable_amount = format(int(balance['amount'])/10**(int(balance['decimals'])))
                amounts.append(int(balance['amount'])/10**(int(balance['decimals'])))
                # readable_balance = '{:.0f}'.format(float(balance.get('balanceUSD', '0')))
                # readable_balance = format(int(balance.get('balanceUSD', '0')))
                balance_usds.append(balance.get('balanceUSD', '0'))
        
        # Create DataFrame
        df = pd.DataFrame({
            'Wallet': wallets,
            # 'ChainID': chain_ids,
            'ChainName': chain_names,
            'CoinAddress': coin_addresses,
            'Symbol': symbols,
            # 'Decimals': decimals,
            # 'Price': prices,
            'Amount': amounts,
            'BalanceUSD': balance_usds
        })

        # Set a threshold to filter out dust
        threshold = 5000

        # Filter the dataframe and output the filtered one
        df['BalanceUSD'] = df['BalanceUSD'].apply(lambda x: float(x))
        filtered_df = df[df['BalanceUSD'] >= threshold]

        return filtered_df