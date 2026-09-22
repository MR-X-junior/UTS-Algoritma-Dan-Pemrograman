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
    print(f"[+] Rata-rata nilai: {nilai:.2f}")

    if nilai >= 75:
        print("[✓] Selamat! Anda lulus SNBP 2026.\n")
        print("[+] Silakan pilih mata kuliah yang ingin diambil, maksimal 3 mata kuliah")

        print(f"""
          [01] Pendidikan Pancasila
          [02] Ilmu Sosial Budaya Dasar
          [03] Pengantar Ilmu Pendidikan
          [04] Literasi Digital dan Media Pembelajaran TIK
          [05] Algoritma dan Pemrograman
          [06] Arsitektur dan Organisasi Komputer
          [07] Logika Matematika
          [08] Pengantar Teknologi Informasi
          [09] Pendidikan Agama Islam
          [10] Pendidikan Agama Kristen
          [11] Multimedia dan Desain Grafis
          [12] Pengembangan Perangkat Lunak""")

        mt1 = int(input("\n[?] Pilih mata kuliah ke-1: "))
        if mt1 >= 1 and mt1 <= 12:
            matkul_selected.append(matkul[mt1 - 1])
        else:
            print("[✗] Nomor tidak valid, mata kuliah ke-1 dilewati")

        mt2 = int(input("[?] Pilih mata kuliah ke-2: "))
        if mt2 >= 1 and mt2 <= 12 and mt2 != mt1:
            matkul_selected.append(matkul[mt2 - 1])
        elif mt2 == mt1:
            print("[✗] Mata kuliah sudah dipilih sebelumnya, mata kuliah ke-2 dilewati")
        else:
            print("[✗] Nomor tidak valid, mata kuliah ke-2 dilewati")

        mt3 = int(input("[?] Pilih mata kuliah ke-3: "))
        if mt3 >= 1 and mt3 <= 12 and mt3 != mt1 and mt3 != mt2:
            matkul_selected.append(matkul[mt3 - 1])
        elif mt3 == mt1 or mt3 == mt2:
            print("[✗] Mata kuliah sudah dipilih sebelumnya, mata kuliah ke-3 dilewati")
        else:
            print("[✗] Nomor tidak valid, mata kuliah ke-3 dilewati")

        jumlah_matkul = len(matkul_selected)
        print(f"\n[+] Total {jumlah_matkul} mata kuliah berhasil diambil:")

        if jumlah_matkul >= 1:
            print(f"1. {matkul_selected[0]}")
        if jumlah_matkul >= 2:
            print(f"2. {matkul_selected[1]}")
        if jumlah_matkul >= 3:
            print(f"3. {matkul_selected[2]}")

        if jumlah_matkul >= 1:
            ganti = input("\n[?] Apakah Anda ingin mengganti salah satu pilihan mata kuliah? (y/n): ").strip().lower() == "y"

            if ganti:
                print(f"\n[+] Pilih nomor urutan mata kuliah yang ingin diganti (1-{jumlah_matkul}):")
                if jumlah_matkul >= 1:
                    print(f"1. {matkul_selected[0]}")
                if jumlah_matkul >= 2:
                    print(f"2. {matkul_selected[1]}")
                if jumlah_matkul >= 3:
                    print(f"3. {matkul_selected[2]}")

                urutan = int(input("\n[?] Nomor urutan: "))

                if urutan >= 1 and urutan <= jumlah_matkul:
                    print(f"""
          [01] Pendidikan Pancasila
          [02] Ilmu Sosial Budaya Dasar
          [03] Pengantar Ilmu Pendidikan
          [04] Literasi Digital dan Media Pembelajaran TIK
          [05] Algoritma dan Pemrograman
          [06] Arsitektur dan Organisasi Komputer
          [07] Logika Matematika
          [08] Pengantar Teknologi Informasi
          [09] Pendidikan Agama Islam
          [10] Pendidikan Agama Kristen
          [11] Multimedia dan Desain Grafis
          [12] Pengembangan Perangkat Lunak""")

                    mt_baru = int(input(f"\n[?] Ganti '{matkul_selected[urutan - 1]}' dengan mata kuliah nomor: "))

                    if mt_baru >= 1 and mt_baru <= 12:
                        if matkul[mt_baru - 1] in matkul_selected:
                            print("[✗] Mata kuliah sudah dipilih, penggantian dibatalkan")
                        else:
                            matkul_selected[urutan - 1] = matkul[mt_baru - 1]
                            print("[✓] Pilihan berhasil diganti")
                    else:
                        print("[✗] Nomor tidak valid, penggantian dibatalkan")
                else:
                    print("[✗] Nomor urutan tidak valid, penggantian dibatalkan")

                print("\n[+] Daftar mata kuliah setelah diganti:")
                if jumlah_matkul >= 1:
                    print(f"1. {matkul_selected[0]}")
                if jumlah_matkul >= 2:
                    print(f"2. {matkul_selected[1]}")
                if jumlah_matkul >= 3:
                    print(f"3. {matkul_selected[2]}")

    else:
        print("[✗] Mohon maaf, Anda tidak lulus SNBP 2026 :(")
else:
    print("[✗] Login gagal! Username atau password salah.")