import mnemonic
import random
import time
from test1 import get_bnb_price
from test import generate_bsc_addresses

def generate_mnemonic_from_wordlist(num_words=12):
    entropy_bits = num_words * 11  # Each word represents 11 bits of entropy in BIP39
    entropy_bytes = entropy_bits // 8

    # Generate random bytes for entropy
    entropy = bytes([random.randint(0, 255) for _ in range(entropy_bytes)])
    mnemo = mnemonic.Mnemonic("english")
    mnemonic_phrase = mnemo.to_mnemonic(entropy)
    return mnemonic_phrase

# with open("list.txt", 'a') as f:
#     while True:
#     # for i in range(1):
#         a = generate_mnemonic_from_wordlist()
#         # a = 'word snow hope palace horn balcony rare bind salon denial forum mirror'
#         b = generate_bsc_addresses(a)
#         for i in b:
#             print(i)
#             time.sleep(5)
#             s = get_bnb_price(i)
#             if s > 0:
#                 print(s)
#                 f.write(a + " : " + i + " : " + str(s) + "\n")



