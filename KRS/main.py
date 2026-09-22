"""
KRS (Kartu Rencana Studi) Application
2605176005 - Eka Putra
2605176010 - Fairuz Miftahul Zahra
2605176017 - Muhammad Kifli
2605176025 - Aulia
2605176027 - Rahmat Adha

https://github.com/MR-X-junior/UTS-Algoritma-Dan-Pemrograman/KRS
"""
matkul_selected = []
matkul = ["Pendidikan Pancasila",
           "Ilmu Sosial Budaya Dasar",
           "Pengantar Ilmu Pendidikan",
           "Literasi Digital dan Media Pembelajaran TIK",
           "Algoritma dan Pemrograman",
           "Arsitektur dan Organisasi Komputer",
           "Logika Matematika",
           "Pengantar Teknologi Informasi",
           "Pendidikan Agama Islam",
           "Pendidikan Agama Kristen",
           "Multimedia dan Desain Grafis",
           "Pengembangan Perangkat Lunak"
         ]



username = input("[?] Masukkan username: ")
password = input("[?] Masukkan password: ")

if username == "Tiara Maharani" and password == "radha":
    print("[✓] Login berhasil! Selamat datang, Tiara Maharani.\n")
    mp1 = int(input("[?] Masukkan Nilai TKA Bahasa Indonesia: "))
    mp2 = int(input("[?] Masukkan Nilai TKA Matematika: "))
    mp3 = int(input("[?] Masukkan nilai TKA mapel pilihan pertama: "))
    mp4 = int(input("[?] Masukkan nilai TKA mapel pilihan kedua: "))
    nilai = (mp1 + mp2 + mp3 + mp4) / 4
    print(f"[+] Rata-rata nilai: {nilai}")

    if nilai >= 75:
        print("[✓] Selamat! Anda lulus SNBP 2026.\n")

        #  Lebih bagus lagi jika menggunakan error handling
        while True:
          print ("[+] Silakan pilih mata kuliah yang ingin diambil Maksimal 3 mata kuliah")
          print ("[+] Gunakan , untuk memilih lebih dari satu mata kuliah Contoh: 1,2,3\n")
          print("\n".join(f"[{i + 1:02d}] {matkul[i]}" for i in range(len(matkul))))
          pilih = list(dict.fromkeys(input(f"\n[?] Pilih mata kuliah (1-{len(matkul)}): ").strip().split(",")))

          if len(pilih) > 3:
              print("[✗] Anda hanya dapat memilih maksimal 3 mata kuliah.\n")
          elif any(not p.isdigit() or int(p) < 1 or int(p) > len(matkul) for p in pilih):
              print("[✗] Pilihan tidak valid. Silakan pilih nomor mata kuliah yang sesuai.\n")
          elif len(pilih) == 0:
              print("[✗] Anda harus memilih setidaknya satu mata kuliah.\n")
          else:
              print("\n[+] Mata kuliah yang dipilih:\n")
              for i in range(len(pilih)):
                  print(f"[{i + 1:02d}] {matkul[int(pilih[i]) - 1]}")

              ganti = input("\n[?] Apakah Anda ingin mengganti pilihan mata kuliah? (y/n): ").strip().lower() == "y"
              if not ganti:break

        print ("\n[✓] Terima kasih! Pilihan mata kuliah Anda telah disimpan.")
        print ("[+] Semangat ya kuliahnya cantik :)")

              

    else:
        print("[✗] Mohon maaf, Anda tidak lulus SNBP 2026 :(")
else:
    print("[✗] Login gagal! Username atau password salah.")
    