from web3 import Web3
from eth_account import Account
from mnemonic import Mnemonic

def generate_bsc_addresses(mnemonic_phrase, num_addresses=1):
    # BSC RPC endpoint
    bsc_rpc_endpoint = 'https://bsc-dataseed.binance.org/'

    # Initialize Web3 provider
    w3 = Web3(Web3.HTTPProvider(bsc_rpc_endpoint))

    # Enable unaudited HDWallet features
    Account.enable_unaudited_hdwallet_features()

    # Derivation path for BSC (m/44'/60'/0'/0/)
    derivation_path = "m/44'/60'/0'/0/"

    # Create accounts using the provided mnemonic
    mnemo = Mnemonic("english")
    seed = mnemo.to_seed(mnemonic_phrase)

    bsc_addresses = []

    for i in range(num_addresses):
        path = f"{derivation_path}{i}"
        private_key = Account.from_mnemonic(mnemonic_phrase, passphrase="", account_path=path)._private_key.hex()
        address = Account.from_key(private_key).address

        # Validate the address using Web3
        if w3.is_address(address):
            bsc_addresses.append(address)

    return bsc_addresses


# mnemonic_phrase = 'word snow hope palace horn balcony rare bind salon denial forum mirror'
# generated_addresses = generate_bsc_addresses(mnemonic_phrase)

# print("Generated BSC Addresses:", generated_addresses)
# for i, address in enumerate(generated_addresses, start=1):
#     print(f"Address {i}: {address}")
