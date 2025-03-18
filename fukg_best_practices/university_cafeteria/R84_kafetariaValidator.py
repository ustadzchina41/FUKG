import csv

def validate_kafetaria_digunakanOleh(r84_file, kafetaria_file, mahasiswa_file):
    # Membaca data dari csv kafetaria_attribute.csv
    kafetaria_data = {}
    with open(kafetaria_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_kafetaria = row[0].strip()  # Kolom namaKafetaria
            kafetaria_data[nama_kafetaria] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari kafetaria

    # Membaca data dari csv mahasiswa_attribute.csv
    mahasiswa_data = {}
    with open(mahasiswa_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nomor_induk_mahasiswa = row[4].strip()  # Kolom nomorIndukMahasiswa
            mahasiswa_data[nomor_induk_mahasiswa] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari mahasiswa

    # Validasi data di R84_Kafetaria_digunakanOleh.csv
    errors = []
    with open(r84_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            nama_kafetaria = row[0].strip()  # Kolom namaKafetaria
            nomor_induk_mahasiswa = row[1].strip()  # Kolom nomorIndukMahasiswa

            # Validasi namaKafetaria
            if nama_kafetaria not in kafetaria_data:
                errors.append(f"Data salah pada baris {line_num}: namaKafetaria {nama_kafetaria} tidak ditemukan di kafetaria_attribute.csv")

            # Validasi nomorIndukMahasiswa
            if nomor_induk_mahasiswa not in mahasiswa_data:
                errors.append(f"Data salah pada baris {line_num}: nomorIndukMahasiswa {nomor_induk_mahasiswa} tidak ditemukan di mahasiswa_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r84_file} sesuai.")

# Contoh pemanggilan fungsi validate_kafetaria_digunakanOleh
r84_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_cafeteria\R84_Kafetaria_digunakanOleh.csv'
kafetaria_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_cafeteria\kafetaria_attribute.csv'
mahasiswa_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_student\mahasiswa_attribute.csv'

validate_kafetaria_digunakanOleh(r84_file, kafetaria_file, mahasiswa_file)
