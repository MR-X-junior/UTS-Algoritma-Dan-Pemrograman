"""
KRS (Kartu Rencana Studi) Application
2605176010 - Fairuz Miftahul Zahra
2605176017 - Muhammad Kifli
2605176025 - Aulia
2605176027 - Rahmat Adha

https://github.com/MR-X-junior/UTS-Algoritma-Dan-Pemrograman/KRS
"""
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

users = {
         "Rahmat Adha":"radha",
         "Muhammad Kifli":"keeeppp",
         
         }

username = input("[?] Masukkan username: ")
password = input("[?] Masukkan password: ")

if username in users and password == users[username]:
    print(f"[✓] Login berhasil! Selamat datang, {username}\n")
    mp1 = int(input("[?] Masukkan Nilai TKA Bahasa Indonesia: "))
    mp2 = int(input("[?] Masukkan Nilai TKA Matematika: "))
    mp3 = int(input("[?] Masukkan nilai TKA mapel pilihan pertama: "))
    mp4 = int(input("[?] Masukkan nilai TKA mapel pilihan kedua: "))
    nilai = (mp1 + mp2 + mp3 + mp4) / 4
    print(f"[+] Rata-rata nilai: {nilai}")

    if nilai >= 75:
        print("[✓] Selamat! Anda lulus SNBP 2026.")

        while True:
          print ("\n[+] Silakan pilih mata kuliah yang ingin diambil Maksimal 5 mata kuliah")
          print ("[+] Gunakan , untuk memilih lebih dari satu mata kuliah Contoh: 1,2,3\n")
          for i in range(len(matkul)):
              print(f"[{i + 1:02d}] {matkul[i]}")
          pilih = input(f"\n[?] Pilih mata kuliah (1-{len(matkul)}): ").strip().split(",")

          if len(pilih) > 5:
              print("[✗] Anda hanya dapat memilih maksimal 5 mata kuliah.\n")
          elif any(not p.isdigit() or int(p) < 1 or int(p) > len(matkul) for p in pilih):
              print("[✗] Pilihan tidak valid. Silakan pilih nomor mata kuliah yang sesuai.\n")
          elif len(pilih) == 0:
              print("[✗] Anda harus memilih setidaknya satu mata kuliah.\n")
          else:
              print("\n[+] Mata kuliah yang dipilih:\n")
              for i in range(len(pilih)):
                  print(f"[{i + 1:02d}] {matkul[int(pilih[i]) - 1]}")

              ganti = input("\n[?] Apakah Anda ingin mengganti pilihan mata kuliah? (y/n): ").strip().lower() == "y"
              if not ganti: break

        print ("\n[✓] Terima kasih! Pilihan mata kuliah Anda telah disimpan.")
        print (f"[+] Semangat ya kuliahnya {username} :)")

    else:
        print("[✗] Mohon maaf, Anda tidak lulus SNBP 2026 :(")
else:
    print("[✗] Login gagal! Username atau password salah.")
    
