import csv

def validate_konferensi_diikutiOleh(r66_file, konferensi_file, mahasiswa_file):
    # Membaca data konferensi dari csv konferensi_attribute.csv
    konferensi_data = {}
    with open(konferensi_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_konferensi = row[0].strip()  # Kolom namaKonferensi
            konferensi_data[nama_konferensi] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari konferensi

    # Membaca data mahasiswa dari csv mahasiswa_attribute.csv
    mahasiswa_data = {}
    with open(mahasiswa_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nomor_induk_mahasiswa = row[4].strip()  # Kolom nomorIndukMahasiswa
            mahasiswa_data[nomor_induk_mahasiswa] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari mahasiswa

    # Validasi data di R66_Konferensi_diikutiOleh.csv
    errors = []
    with open(r66_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            nama_konferensi = row[0].strip()  # Kolom namaKonferensi
            nomor_induk_mahasiswa = row[1].strip()  # Kolom nomorIndukMahasiswa

            # Validasi namaKonferensi
            if nama_konferensi not in konferensi_data:
                errors.append(f"Data salah pada baris {line_num}: namaKonferensi '{nama_konferensi}' tidak ditemukan di konferensi_attribute.csv")

            # Validasi nomorIndukMahasiswa
            if nomor_induk_mahasiswa not in mahasiswa_data:
                errors.append(f"Data salah pada baris {line_num}: nomorIndukMahasiswa '{nomor_induk_mahasiswa}' tidak ditemukan di mahasiswa_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r66_file} sesuai.")

# Contoh pemanggilan fungsi validate_konferensi_diikutiOleh
r66_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\academic_conference\R66_Konferensi_diikutiOleh.csv'
konferensi_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\academic_conference\konferensi_attribute.csv'
mahasiswa_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_student\mahasiswa_attribute.csv'

validate_konferensi_diikutiOleh(r66_file, konferensi_file, mahasiswa_file)
