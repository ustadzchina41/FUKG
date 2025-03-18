import csv

def validate_seminar_diselenggarakanOleh(r61_file, seminar_file, organisasi_file):
    # Membaca data seminar dari csv seminar_attribute.csv
    seminar_data = {}
    with open(seminar_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            judul_seminar = row[0].strip()  # Kolom judulSeminar
            seminar_data[judul_seminar] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari seminar

    # Membaca data organisasi dari csv organisasiMahasiswa.csv
    organisasi_data = {}
    with open(organisasi_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_organisasi = row[0].strip()  # Kolom namaOrganisasi
            organisasi_data[nama_organisasi] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari organisasi

    # Validasi data di R61_Seminar_diselenggarakanOleh.csv
    errors = []
    with open(r61_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            judul_seminar = row[0].strip()  # Kolom judulSeminar
            nama_organisasi = row[1].strip()  # Kolom namaOrganisasi

            # Validasi judulSeminar
            if judul_seminar not in seminar_data:
                errors.append(f"Data salah pada baris {line_num}: judulSeminar '{judul_seminar}' tidak ditemukan di seminar_attribute.csv")

            # Validasi namaOrganisasi
            if nama_organisasi not in organisasi_data:
                errors.append(f"Data salah pada baris {line_num}: namaOrganisasi '{nama_organisasi}' tidak ditemukan di organisasiMahasiswa.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r61_file} sesuai.")

# Contoh pemanggilan fungsi validate_seminar_diselenggarakanOleh
r61_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\seminar\R61_Seminar_diselenggarakanOleh.csv'
seminar_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\seminar\seminar_attribute.csv'
organisasi_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\student_organization\organisasiMahasiswa_attribute.csv'

validate_seminar_diselenggarakanOleh(r61_file, seminar_file, organisasi_file)
