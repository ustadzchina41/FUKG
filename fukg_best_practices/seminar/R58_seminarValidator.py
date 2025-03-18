import csv

def validate_seminar_diikutiOleh(r58_file, seminar_file, mahasiswa_file):
    # Membaca data seminar dari csv seminar_attribute.csv
    seminar_data = {}
    with open(seminar_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            judul_seminar = row[0].strip()  # Kolom judulSeminar
            seminar_data[judul_seminar] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari seminar

    # Membaca data mahasiswa dari csv mahasiswa_attribute.csv
    mahasiswa_data = {}
    with open(mahasiswa_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nomor_induk_mahasiswa = row[4].strip()  # Kolom nomorIndukMahasiswa
            mahasiswa_data[nomor_induk_mahasiswa] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari mahasiswa

    # Validasi data di R58_Seminar_diikutiOleh.csv
    errors = []
    with open(r58_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            judul_seminar = row[0].strip()  # Kolom judulSeminar
            nomor_induk_mahasiswa = row[1].strip()  # Kolom nomorIndukMahasiswa

            # Validasi judulSeminar
            if judul_seminar not in seminar_data:
                errors.append(f"Data salah pada baris {line_num}: judulSeminar '{judul_seminar}' tidak ditemukan di seminar_attribute.csv")

            # Validasi nomorIndukMahasiswa
            if nomor_induk_mahasiswa not in mahasiswa_data:
                errors.append(f"Data salah pada baris {line_num}: nomorIndukMahasiswa '{nomor_induk_mahasiswa}' tidak ditemukan di mahasiswa_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r58_file} sesuai.")

# Contoh pemanggilan fungsi validate_seminar_diikutiOleh
r58_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\seminar\R58_Seminar_diikutiOleh.csv'
seminar_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\seminar\seminar_attribute.csv'
mahasiswa_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_student\mahasiswa_attribute.csv'

validate_seminar_diikutiOleh(r58_file, seminar_file, mahasiswa_file)
