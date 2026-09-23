"""
Kelompok 8
Tema : Aplikasi Cek Kelulusan SNBT
2605176010 - Fairuz Miftahul Zahra
2605176017 - Muhammad Kifli
2605176025 - Aulia
2605176027 - Rahmat Adha

https://youtu.be/xxxxxxxxx

"""

matkul = [["Pendidikan Pancasila", 1],
          ["Ilmu Sosial Budaya Dasar", 2],
          ["Pengantar Ilmu Pendidikan", 2],
          ["Literasi Digital dan Media Pembelajaran TIK", 3],
          ["Algoritma dan Pemrograman", 3],
          ["Arsitektur dan Organisasi Komputer", 3],
          ["Logika Matematika", 2],
          ["Pengantar Teknologi Informasi", 2],
          ["Pendidikan Agama Islam", 2],
          ["Pendidikan Agama Kristen", 2],
          ["Multimedia dan Desain Grafis", 3],
          ["Pengembangan Perangkat Lunak", 3]
         ]

users = {
        "Rahmat Adha":"radha",
        "Muhammad Kifli":"terkiplikipli",
        "Rara":"rara",
        "Aulia":"aulimutanjai"
        }

while True:
    username = input("[?] Masukkan username: ")
    password = input("[?] Masukkan password: ")

    if username in users and password == users[username]:
        print(f"[✓] Login berhasil! Selamat datang, {username}\n")
        break
    else:
        print("[✗] Login gagal! Username atau password salah. Silakan coba lagi.\n")

mp1 = int(input("[?] Masukkan Nilai TKA Bahasa Indonesia: "))
mp2 = int(input("[?] Masukkan Nilai TKA Matematika: "))
mp3 = int(input("[?] Masukkan nilai TKA mapel pilihan pertama: "))
mp4 = int(input("[?] Masukkan nilai TKA mapel pilihan kedua: "))
nilai = (mp1 + mp2 + mp3 + mp4) / 4
print(f"[+] Rata-rata nilai: {nilai}")

if nilai >= 75:
    print("[✓] Selamat! Anda lulus SNBP 2026.")

    while True:
      print ("\n[+] Silakan pilih mata kuliah yang ingin diambil Minimal 20 SKS dan maksimal 20 SKS.")
      print ("[+] Gunakan , untuk memilih lebih dari satu mata kuliah Contoh: 1,2,3\n")
      for i in range(len(matkul)):
          print(f"[{i + 1:02d}] {matkul[i][0]} ({matkul[i][1]} SKS)")
      pilih = input(f"\n[?] Pilih mata kuliah (1-{len(matkul)}): ").strip().split(",")

      if any(not p.isdigit() or int(p) < 1 or int(p) > len(matkul) for p in pilih):
          print("[✗] Pilihan tidak valid. Silakan pilih nomor mata kuliah yang sesuai.\n")
      elif len(pilih) == 0:
          print("[✗] Anda harus memilih setidaknya satu mata kuliah.\n")
      else:
          total_sks = 0
          for i in range(len(pilih)):
              total_sks = total_sks + matkul[int(pilih[i]) - 1][1]

          if total_sks < 20:
              print(f"[✗] Total SKS Anda {total_sks}, di bawah batas minimal 20 SKS.")
          elif total_sks > 20:
              print(f"[✗] Total SKS Anda {total_sks}, melebihi batas maksimal 20 SKS.")
          else:
              print("\n[+] Mata kuliah yang dipilih:\n")
              for i in range(len(pilih)):
                  print(f"[{i + 1:02d}] {matkul[int(pilih[i]) - 1][0]} ({matkul[int(pilih[i]) - 1][1]} SKS)")
              print(f"\n[+] Total SKS diambil: {total_sks} / 20")

              ganti = input("\n[?] Apakah Anda ingin mengganti pilihan mata kuliah? (y/n): ").strip().lower() == "y"
              if not ganti:
                  break

    print ("\n[✓] Terima kasih! Pilihan mata kuliah Anda telah disimpan.")
    print (f"[+] Semangat ya kuliahnya {username} :)")

else:
    print("[✗] Mohon maaf, Anda tidak lulus SNBP 2026 :(")