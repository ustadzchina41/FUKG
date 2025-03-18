import csv

def validate_seminar_diikutiOleh(r59_file, seminar_file, dosen_file):
    # Membaca data seminar dari csv seminar_attribute.csv
    seminar_data = {}
    with open(seminar_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            judul_seminar = row[0].strip()  # Kolom judulSeminar
            seminar_data[judul_seminar] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari seminar

    # Membaca data dosen dari csv dosen_attribute.csv
    dosen_data = {}
    with open(dosen_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nidn = row[0].strip()  # Kolom NIDN
            dosen_data[nidn] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari dosen

    # Validasi data di R59_Seminar_diikutiOleh.csv
    errors = []
    with open(r59_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            judul_seminar = row[0].strip()  # Kolom judulSeminar
            nidn = row[1].strip()  # Kolom NIDN

            # Validasi judulSeminar
            if judul_seminar not in seminar_data:
                errors.append(f"Data salah pada baris {line_num}: judulSeminar '{judul_seminar}' tidak ditemukan di seminar_attribute.csv")

            # Validasi NIDN
            if nidn not in dosen_data:
                errors.append(f"Data salah pada baris {line_num}: NIDN '{nidn}' tidak ditemukan di dosen_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r59_file} sesuai.")

# Contoh pemanggilan fungsi validate_seminar_diikutiOleh
r59_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\seminar\R59_Seminar_diikutiOleh.csv'
seminar_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\seminar\seminar_attribute.csv'
dosen_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_lecture\dosen_attribute.csv'

validate_seminar_diikutiOleh(r59_file, seminar_file, dosen_file)
