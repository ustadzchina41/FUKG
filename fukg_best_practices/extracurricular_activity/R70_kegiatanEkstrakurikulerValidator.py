import csv

def validate_kegiatan_ekstrakurikuler(r70_file, kegiatan_file, mahasiswa_file):
    # Membaca data kegiatan ekstrakurikuler dari csv kegiatanEkstrakurikuler_attribute.csv
    kegiatan_data = {}
    with open(kegiatan_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_kegiatan = row[0].strip()  # Kolom namaKegiatanEkstrakurikuler
            kegiatan_data[nama_kegiatan] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari kegiatan

    # Membaca data mahasiswa dari csv mahasiswa_attribute.csv
    mahasiswa_data = {}
    with open(mahasiswa_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nomor_induk_mahasiswa = row[4].strip()  # Kolom nomorIndukMahasiswa
            mahasiswa_data[nomor_induk_mahasiswa] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari mahasiswa

    # Validasi data di R70_KegiatanEkstrakurikuler_diikutiOleh.csv
    errors = []
    with open(r70_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            nama_kegiatan = row[0].strip()  # Kolom namaKegiatanEkstrakurikuler
            nomor_induk_mahasiswa = row[1].strip()  # Kolom nomorIndukMahasiswa

            # Validasi namaKegiatanEkstrakurikuler
            if nama_kegiatan not in kegiatan_data:
                errors.append(f"Data salah pada baris {line_num}: namaKegiatanEkstrakurikuler '{nama_kegiatan}' tidak ditemukan di kegiatanEkstrakurikuler_attribute.csv")

            # Validasi nomorIndukMahasiswa
            if nomor_induk_mahasiswa not in mahasiswa_data:
                errors.append(f"Data salah pada baris {line_num}: nomorIndukMahasiswa '{nomor_induk_mahasiswa}' tidak ditemukan di mahasiswa_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r70_file} sesuai.")

# Contoh pemanggilan fungsi validate_kegiatan_ekstrakurikuler
r70_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\extracurricular_activity\R70_KegiatanEkstrakurikuler_diikutiOleh.csv'
kegiatan_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\extracurricular_activity\kegiatanEkstrakurikuler_attribute.csv'
mahasiswa_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_student\mahasiswa_attribute.csv'

validate_kegiatan_ekstrakurikuler(r70_file, kegiatan_file, mahasiswa_file)
