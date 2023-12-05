from web3 import Web3
from bip_utils import Bip44, Bip44Coins, Bip44Changes

def generate_btc_addresses(mnemonic_phrase, num_addresses=1):
    # BSC RPC endpoint
    bsc_rpc_endpoint = 'https://bsc-dataseed.binance.org/'

    # Initialize Web3 provider
    w3 = Web3(Web3.HTTPProvider(bsc_rpc_endpoint))

    # Create BTC wallet using the provided mnemonic
    wallet = Bip44.FromMnemonic(mnemonic_phrase, Bip44Coins.BITCOIN)

    btc_addresses = []

    for i in range(num_addresses):
        # Derivation path for BTC (m/44'/0'/0'/0/)
        path = f"{Bip44Coins.BITCOIN}/{Bip44Changes.CHAIN_EXT}"

        private_key = wallet.PrivateKey(path).ToHex()
        address = wallet.PublicKey(path).ToAddress()

        # Validate the address using Web3
        if w3.isAddress(address):
            btc_addresses.append(address)

    return btc_addresses





mnemonic_phrase = 'word snow hope palace horn balcony rare bind salon denial forum mirror'
generated_addresses = generate_btc_addresses(mnemonic_phrase)

print("Generated BSC Addresses:", generated_addresses)
for i, address in enumerate(generated_addresses, start=1):
    print(f"Address {i}: {address}")
