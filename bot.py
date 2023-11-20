import telebot
import time
from test1 import get_bnb_price
from test import generate_bsc_addresses
from main import generate_mnemonic_from_wordlist

# Telegram botni tokenini kiritish
TOKEN = "6936366717:AAFgafsv0wl_G4ArMulJHxkUPPhuuzaaQ6U"
bot = telebot.TeleBot(TOKEN)

def habar():
    with open("list.txt", 'a') as f:
        while True:
        # for i in range(1):
            a = generate_mnemonic_from_wordlist()
            # a = 'word snow hope palace horn balcony rare bind salon denial forum mirror'
            print(a)
            b = generate_bsc_addresses(a)
            for i in b:
                print(i)
                time.sleep(5)
                try:
                    s = get_bnb_price(i)
                    if s != None:
                        if s > 0:
                            print(s)
                            d = f"{a} : {i} : {str(s)}"
                            f.write(d + "\n")
                            user_id = "5084491398"
                            bot.send_message(user_id, d)
                except ConnectionError as e:
                    time.sleep(5)
                    print(f"Connection error: {e}")


habar()
# Botni ishga tushirish
if __name__ == "__main__":
    bot.polling(none_stop=True)
