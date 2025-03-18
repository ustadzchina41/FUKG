import csv

def validate_publikasi_ditulisOleh(r39_file, publikasi_file, dosen_file):
    # Membaca data dari csv publikasi_attribute.csv
    publikasi_data = {}
    with open(publikasi_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            judul_publikasi = row[0].strip()  # Kolom judulPublikasi
            publikasi_data[judul_publikasi] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari publikasi

    # Membaca data dari csv dosen_attribute.csv
    dosen_data = {}
    with open(dosen_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nidn = row[0].strip()  # Kolom NIDN
            dosen_data[nidn] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari dosen

    # Validasi data di R39_Publikasi_ditulisOleh.csv
    errors = []
    with open(r39_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            judul_publikasi = row[0].strip()  # Kolom judulPublikasi
            nidn = row[1].strip()  # Kolom NIDN

            # Validasi judulPublikasi
            if judul_publikasi not in publikasi_data:
                errors.append(f"Data salah pada baris {line_num}: Judul publikasi '{judul_publikasi}' tidak ditemukan di publikasi_attribute.csv")

            # Validasi NIDN
            if nidn not in dosen_data:
                errors.append(f"Data salah pada baris {line_num}: NIDN '{nidn}' tidak ditemukan di dosen_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r39_file} sesuai.")

# Contoh pemanggilan fungsi validate_publikasi_ditulisOleh
r39_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\publication\R39_Publikasi_ditulisOleh.csv'
publikasi_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\publication\publikasi_attribute.csv'
dosen_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_lecture\dosen_attribute.csv'

validate_publikasi_ditulisOleh(r39_file, publikasi_file, dosen_file)
