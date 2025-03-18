import csv

def validate_kafetaria_bagianDari(r83_file, kafetaria_file, fakultas_file):
    # Membaca data dari csv kafetaria_attribute.csv
    kafetaria_data = {}
    with open(kafetaria_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_kafetaria = row[0].strip()  # Kolom namaKafetaria
            kafetaria_data[nama_kafetaria] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari kafetaria

    # Membaca data dari csv fakultas_attribute.csv
    fakultas_data = {}
    with open(fakultas_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_fakultas = row[0].strip()  # Kolom namaFakultas
            fakultas_data[nama_fakultas] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari fakultas

    # Validasi data di R83_Kafetaria_bagianDari.csv
    errors = []
    with open(r83_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            nama_kafetaria = row[0].strip()  # Kolom namaKafetaria
            nama_fakultas = row[1].strip()  # Kolom namaFakultas

            # Validasi namaKafetaria
            if nama_kafetaria not in kafetaria_data:
                errors.append(f"Data salah pada baris {line_num}: namaKafetaria {nama_kafetaria} tidak ditemukan di kafetaria_attribute.csv")

            # Validasi namaFakultas
            if nama_fakultas not in fakultas_data:
                errors.append(f"Data salah pada baris {line_num}: namaFakultas {nama_fakultas} tidak ditemukan di fakultas_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r83_file} sesuai.")

# Contoh pemanggilan fungsi validate_kafetaria_bagianDari
r83_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_cafeteria\R83_Kafetaria_bagianDari.csv'
kafetaria_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_cafeteria\kafetaria_attribute.csv'
fakultas_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\faculty\fakultas_attribute.csv'

validate_kafetaria_bagianDari(r83_file, kafetaria_file, fakultas_file)
