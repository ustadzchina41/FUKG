import csv

def validate_relations(r3_file, mahasiswa_file, organisasi_file):
    # Membaca data dari csv mahasiswa_attribute.csv
    mahasiswa_data = {}
    with open(mahasiswa_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nomor_induk = row[4].strip()  # Kolom nomorIndukMahasiswa
            mahasiswa_data[nomor_induk] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari mahasiswa

    # Membaca data dari csv organisasiMahasiswa.csv
    organisasi_data = {}
    with open(organisasi_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_organisasi = row[0].strip()  # Kolom namaOrganisasi
            organisasi_data[nama_organisasi] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari organisasi

    # Validasi data di R3_mahasiswa_anggotaDari.csv
    errors = []
    with open(r3_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            nomor_induk = row[0].strip()  # Kolom nomorIndukMahasiswa
            nama_organisasi = row[1].strip()  # Kolom namaOrganisasi

            # Validasi nomorIndukMahasiswa
            if nomor_induk not in mahasiswa_data:
                errors.append(f"Data salah pada baris {line_num}: nomorIndukMahasiswa {nomor_induk} tidak ditemukan di mahasiswa_attribute.csv")

            # Validasi namaOrganisasi
            if nama_organisasi not in organisasi_data:
                errors.append(f"Data salah pada baris {line_num}: namaOrganisasi {nama_organisasi} tidak ditemukan di organisasiMahasiswa.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r3_file} sesuai.")

# Panggil fungsi validate_relations dengan nama file CSV yang sesuai
r3_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_student\R3_mahasiswa_anggotaDari.csv'
mahasiswa_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_student\mahasiswa_attribute.csv'
organisasi_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\student_organization\organisasiMahasiswa_attribute.csv'

validate_relations(r3_file, mahasiswa_file, organisasi_file)
