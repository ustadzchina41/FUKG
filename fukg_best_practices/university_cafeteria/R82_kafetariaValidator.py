import csv

def validate_kafetaria_bagianDari(r82_file, kafetaria_file, universitas_file):
    # Membaca data dari csv kafetaria_attribute.csv
    kafetaria_data = {}
    with open(kafetaria_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_kafetaria = row[0].strip()  # Kolom namaKafetaria
            kafetaria_data[nama_kafetaria] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari kafetaria

    # Membaca data dari csv universitas_attribute.csv
    universitas_data = {}
    with open(universitas_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_universitas = row[0].strip()  # Kolom namaUniversitas
            universitas_data[nama_universitas] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari universitas

    # Validasi data di R82_Kafetaria_bagianDari.csv
    errors = []
    with open(r82_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            nama_kafetaria = row[0].strip()  # Kolom namaKafetaria
            nama_universitas = row[1].strip()  # Kolom namaUniversitas

            # Validasi namaKafetaria
            if nama_kafetaria not in kafetaria_data:
                errors.append(f"Data salah pada baris {line_num}: namaKafetaria {nama_kafetaria} tidak ditemukan di kafetaria_attribute.csv")

            # Validasi namaUniversitas
            if nama_universitas not in universitas_data:
                errors.append(f"Data salah pada baris {line_num}: namaUniversitas {nama_universitas} tidak ditemukan di universitas_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r82_file} sesuai.")

# Contoh pemanggilan fungsi validate_kafetaria_bagianDari
r82_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_cafeteria\R82_Kafetaria_bagianDari.csv'
kafetaria_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_cafeteria\kafetaria_attribute.csv'
universitas_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university\universitas_attribute.csv'

validate_kafetaria_bagianDari(r82_file, kafetaria_file, universitas_file)
