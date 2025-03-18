import csv

def validate_perpustakaan_mengandung(r56_file, perpustakaan_file, buku_file):
    # Membaca data perpustakaan dari csv perpustakaan_attribute.csv
    perpustakaan_data = {}
    with open(perpustakaan_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_perpustakaan = row[0].strip()  # Kolom namaPerpustakaan
            perpustakaan_data[nama_perpustakaan] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari perpustakaan

    # Membaca data buku dari csv buku_attribute.csv
    buku_data = {}
    with open(buku_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            judul_buku = row[0].strip()  # Kolom judulBuku
            buku_data[judul_buku] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari buku

    # Validasi data di R56_Perpustakaan_mengandung.csv
    errors = []
    with open(r56_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            nama_perpustakaan = row[0].strip()  # Kolom namaPerpustakaan
            judul_buku = row[1].strip()  # Kolom judulBuku

            # Validasi namaPerpustakaan
            if nama_perpustakaan not in perpustakaan_data:
                errors.append(f"Data salah pada baris {line_num}: namaPerpustakaan '{nama_perpustakaan}' tidak ditemukan di perpustakaan_attribute.csv")

            # Validasi judulBuku
            if judul_buku not in buku_data:
                errors.append(f"Data salah pada baris {line_num}: judulBuku '{judul_buku}' tidak ditemukan di buku_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r56_file} sesuai.")

# Contoh pemanggilan fungsi validate_perpustakaan_mengandung
r56_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\academic_library\R56_Perpustakaan_mengandung.csv'
perpustakaan_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\academic_library\perpustakaan_attribute.csv'
buku_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\book\buku_attribute.csv'

validate_perpustakaan_mengandung(r56_file, perpustakaan_file, buku_file)
