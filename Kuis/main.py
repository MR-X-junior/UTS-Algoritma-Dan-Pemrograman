"""
2605176005 - Eka Putra
2605176010 - Fairuz Miftahul Zahra
2605176017 - Muhammad Kifli
2605176025 - Aulia
2605176027 - Rahmat Adha
"""
# BELUM SELESAI
import os
import sys
import time
import json

if os.name == 'posix':
    red = '\033[91m'
    green = '\033[92m'
    yellow = '\033[93m'
    blue = '\033[94m'
    magenta = '\033[95m'
    cyan = '\033[96m'
    white = '\033[97m'
    reset = '\033[0m'
else:
    red = ''
    green = ''
    yellow = ''
    blue = ''
    magenta = ''
    cyan = ''
    white = ''
    reset = ''

# soal = json.loads(open("soal.json").read())


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def ketik(teks, delay=0.05):
    for karakter in teks + "\n":
        sys.stdout.write(karakter)
        sys.stdout.flush()
        time.sleep(delay)

def login():
    clear_screen()
    ketik("Silakan login untuk melanjutkan.")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username == "Tiara Maharani" and password == "radha":
        ketik("Login berhasil! Selamat datang, Tiara Maharani.\n")
        main()
    else:
        ketik("Login gagal! Username atau password salah.")
        time.sleep(2)
        login()

def main():
    clear_screen()
    print ("======= KUIS SEDERHANA =======")

   


if __name__ == "__main__":
    login()