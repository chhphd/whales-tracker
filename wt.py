from functions import Wallet
from datetime import datetime
import json
import argparse
import re
import pandas as pd

def parser() -> str:
    '''
    Argparse implementation to input address when running the program
    Program should be run by:
    
    python wt.py --address=[your_address]
    
    '''  
    # Init parser
    parser = argparse.ArgumentParser(prog='Whale trecker')
    
    # Parser arguments
    parser.add_argument('--address', dest='input_address', default='', help='address to be tracked')
    
    args = parser.parse_args()
    # input_address = args.input_address

    return args.input_address

def validate_eth_address(input_string: str) -> bool:
    '''
    Validates the ETH address. Rules:
    - string starts with '0x'
    - string consists of 42 characters
    - string contains only a-f, A-F, 0-9 after 'hx'

    Args:
        input_string: str

    Returns:
    True or ValueError    
    '''
    
    regex_pattern = r'^0x[a-fA-F0-9]{40}$'
    
    if re.match(regex_pattern, input_string):
        return True
    else:
        raise ValueError('Please input a valid ETH address!')
    

def export_to_csv(df, filename):
    '''
    Export a pandas DataFrame to a CSV file.

    Args:
        df (pd.DataFrame): The DataFrame to export.
        filename (str): The name of the file to export the data to.
    '''

    # Prompt the user
    while True:
        choice = input('Do you want to export this to .csv? (y/n): ')

        if choice == 'y':
            df.to_csv(filename, index=True)
            break
        elif choice == 'n':
            break    
        else:
            print('Please input "y" or "n".')

def add_wallets():

    wallet_list = []

    try:
        # Load JSON file
        with open('wallets.json', 'r') as f:
            wallets = json.load(f)

    except FileNotFoundError:
        print('File not found!')    

    # Loop through each address
    for item in wallets:
        wallet = Wallet(address=item['wallet'], label=item['label'])
        wallet_list.append(wallet.dataframe)

    return pd.concat(wallet_list, ignore_index=True)

# Main menu
def menu():
    print('------------------------------------------')
    print('-----------   WHALE  TRACKER   -----------')
    print(f'{input_address}')
    print('------------------------------------------')

    # Menu 1 change contents depending on user's input when running the program
    message = 'Your holdings' if len(input_address) > 0 else 'You cannot see your holdings since you did not provide an address.'
    print(f'1. {message}')

    print('2. Whales holdings (from json)')
    print('0. Exit')

# Main menu options
def option1():
    # TODO: progress bar

    # If user provided input then validate ETH address
    if len(input_address) == 0: 
        print('You did not provide an address. Please rerun with --address=[your_address]')    
    else:
        validate_eth_address(input_address)
        wallet = Wallet(address=input_address, label='MyWallet')
        print(wallet.dataframe)
        export_to_csv(wallet.dataframe, f'output/{wallet.address}_{wallet.label}_{formatted_now}.csv')


def option2():
    # TODO: progress bar
    data = add_wallets()
    print(data)
    export_to_csv(data, f'output/AllWhales_{formatted_now}.csv')

# Main function
def main():
    while True:    
        menu()
        choice = input('Enter your choice: ')
        if choice == '1':
            option1()
        elif choice == '2':
            option2()
        elif choice == '0':
            print('Exiting...')
            break
        else:
            print('Invalid choice. Please choose again.')

# Get the current date and time
now = datetime.now()
formatted_now = now.strftime('%Y%m%d_%H%M%S')

# Program
if __name__ == '__main__':
    input_address = parser()
    main()