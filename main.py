"""
Program Cek Kelulusan SNBT 2026
Eka Putra - 2605176005
Fairuz Miftahul Zahra - 2605176010
Muhammad Kifli - 2605176017
Aulia - 2605176025
Rahmat Adha - 2605176027
"""

data_peserta = [
    ["AULIA", "2605176025", "15-08-2007", True],
    ["FAIRUZ MIFTAHUL ZAHRA", "2605176010", "22-11-2006", False],
    ["MUHAMMAD KIFLI", "2605176017", "03-05-2007", True],
    ["RAHMAT ADHA", "2605176027", "19-09-2006", True],
    ["EKA PUTRA", "2605176005", "27-01-2007", False],
]

print("======= CEK KELULUSAN SNBT 2026 =======")

nomor = input("\nMasukkan Nomor Peserta   : ").strip()
tanggal = input("Masukkan Tanggal Lahir (DD-MM-YYYY): ").strip()

list_nomor = [data_peserta[0][1], data_peserta[1][1], data_peserta[2][1], data_peserta[3][1], data_peserta[4][1]]

if nomor in list_nomor and data_peserta[list_nomor.index(nomor)][2] == tanggal:
    peserta = data_peserta[list_nomor.index(nomor)]
    print("\n=================================================")
    if peserta[3]:
        print(f"NAMA PESERTA  : {peserta[0]}")
        print(f"NOMOR PESERTA : {peserta[1]}")
        print(f"TANGGAL LAHIR : {peserta[2]}")
        print("SELAMAT ANDA LULUS SNBT 2026")
    else:
        print(f"PESERTA ATAS NAMA {peserta[0]} DENGAN NOMOR PESERTA {peserta[1]} DINYATAKAN TIDAK LULUS SNBT 2026:(")
    print("=================================================")
else:
    print("\nData tidak ditemukan. Periksa kembali nomor peserta dan tanggal lahir Anda.")