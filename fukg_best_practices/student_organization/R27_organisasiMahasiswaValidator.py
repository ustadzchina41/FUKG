import csv

def validate_organisasi_diikutiOleh(r27_file, organisasi_file, mahasiswa_file):
    # Membaca data dari csv organisasiMahasiswa.csv
    organisasi_data = {}
    with open(organisasi_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_organisasi = row[0].strip()  # Kolom namaOrganisasi
            organisasi_data[nama_organisasi] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari organisasi

    # Membaca data dari csv mahasiswa_attribute.csv
    mahasiswa_data = {}
    with open(mahasiswa_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nomor_induk = row[4].strip()  # Kolom nomorIndukMahasiswa
            mahasiswa_data[nomor_induk] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari mahasiswa

    # Validasi data di R27_OrganisasiMahasiswa_diikutiOleh.csv
    errors = []
    with open(r27_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            nama_organisasi = row[0].strip()  # Kolom namaOrganisasi
            nomor_induk = row[1].strip()  # Kolom nomorIndukMahasiswa

            # Validasi namaOrganisasi
            if nama_organisasi not in organisasi_data:
                errors.append(f"Data salah pada baris {line_num}: namaOrganisasi {nama_organisasi} tidak ditemukan di organisasiMahasiswa.csv")

            # Validasi nomorIndukMahasiswa
            if nomor_induk not in mahasiswa_data:
                errors.append(f"Data salah pada baris {line_num}: nomorIndukMahasiswa {nomor_induk} tidak ditemukan di mahasiswa_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r27_file} sesuai.")

# Contoh pemanggilan fungsi validate_organisasi_diikutiOleh
r27_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\student_organization\R27_OrganisasiMahasiswa_diikutiOleh.csv'
organisasi_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\student_organization\organisasiMahasiswa_attribute.csv'
mahasiswa_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_student\mahasiswa_attribute.csv'

validate_organisasi_diikutiOleh(r27_file, organisasi_file, mahasiswa_file)
