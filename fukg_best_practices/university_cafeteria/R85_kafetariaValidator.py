import csv

def validate_kafetaria_digunakanOleh(r85_file, kafetaria_file, dosen_file):
    # Membaca data dari csv kafetaria_attribute.csv
    kafetaria_data = {}
    with open(kafetaria_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_kafetaria = row[0].strip()  # Kolom namaKafetaria
            kafetaria_data[nama_kafetaria] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari kafetaria

    # Membaca data dari csv dosen_attribute.csv
    dosen_data = {}
    with open(dosen_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nidn = row[0].strip()  # Kolom NIDN
            dosen_data[nidn] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari dosen

    # Validasi data di R85_Kafetaria_digunakanOleh.csv
    errors = []
    with open(r85_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            nama_kafetaria = row[0].strip()  # Kolom namaKafetaria
            nidn = row[1].strip()  # Kolom NIDN

            # Validasi namaKafetaria
            if nama_kafetaria not in kafetaria_data:
                errors.append(f"Data salah pada baris {line_num}: namaKafetaria {nama_kafetaria} tidak ditemukan di kafetaria_attribute.csv")

            # Validasi NIDN
            if nidn not in dosen_data:
                errors.append(f"Data salah pada baris {line_num}: NIDN {nidn} tidak ditemukan di dosen_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r85_file} sesuai.")

# Contoh pemanggilan fungsi validate_kafetaria_digunakanOleh
r85_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_cafeteria\R85_Kafetaria_digunakanOleh.csv'
kafetaria_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_cafeteria\kafetaria_attribute.csv'
dosen_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_lecture\dosen_attribute.csv'

validate_kafetaria_digunakanOleh(r85_file, kafetaria_file, dosen_file)
