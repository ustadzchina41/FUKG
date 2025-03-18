import csv

def validate_workshop_diikutiOleh(r63_file, workshop_file, mahasiswa_file):
    # Membaca data workshop dari csv workshop_attribute.csv
    workshop_data = {}
    with open(workshop_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            judul_workshop = row[0].strip()  # Kolom judulWorkshop
            workshop_data[judul_workshop] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari workshop

    # Membaca data mahasiswa dari csv mahasiswa_attribute.csv
    mahasiswa_data = {}
    with open(mahasiswa_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nomor_induk_mahasiswa = row[4].strip()  # Kolom nomorIndukMahasiswa
            mahasiswa_data[nomor_induk_mahasiswa] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari mahasiswa

    # Validasi data di R63_Workshop_diikutiOleh.csv
    errors = []
    with open(r63_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            judul_workshop = row[0].strip()  # Kolom judulWorkshop
            nomor_induk_mahasiswa = row[1].strip()  # Kolom nomorIndukMahasiswa

            # Validasi judulWorkshop
            if judul_workshop not in workshop_data:
                errors.append(f"Data salah pada baris {line_num}: judulWorkshop '{judul_workshop}' tidak ditemukan di workshop_attribute.csv")

            # Validasi nomorIndukMahasiswa
            if nomor_induk_mahasiswa not in mahasiswa_data:
                errors.append(f"Data salah pada baris {line_num}: nomorIndukMahasiswa '{nomor_induk_mahasiswa}' tidak ditemukan di mahasiswa_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r63_file} sesuai.")

# Contoh pemanggilan fungsi validate_workshop_diikutiOleh
r63_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\academic_workshop\R63_Workshop_diikutiOleh.csv'
workshop_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\academic_workshop\workshop_attribute.csv'
mahasiswa_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_student\mahasiswa_attribute.csv'

validate_workshop_diikutiOleh(r63_file, workshop_file, mahasiswa_file)
