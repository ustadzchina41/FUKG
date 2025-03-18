import csv

def validate_universitas_memiliki(r21_file, universitas_file, fakultas_file):
    # Membaca data dari csv universitas_attribute.csv
    universitas_data = {}
    with open(universitas_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_universitas = row[0].strip()  # Kolom namaUniversitas
            universitas_data[nama_universitas] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari universitas

    # Membaca data dari csv fakultas_attribute.csv
    fakultas_data = {}
    with open(fakultas_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_fakultas = row[0].strip()  # Kolom namaFakultas
            fakultas_data[nama_fakultas] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari fakultas

    # Validasi data di R21_Universitas_memiliki.csv
    errors = []
    with open(r21_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            nama_universitas = row[0].strip()  # Kolom namaUniversitas
            nama_fakultas = row[1].strip()  # Kolom namaFakultas

            # Validasi namaUniversitas
            if nama_universitas not in universitas_data:
                errors.append(f"Data salah pada baris {line_num}: namaUniversitas {nama_universitas} tidak ditemukan di universitas_attribute.csv")

            # Validasi namaFakultas
            if nama_fakultas not in fakultas_data:
                errors.append(f"Data salah pada baris {line_num}: namaFakultas {nama_fakultas} tidak ditemukan di fakultas_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r21_file} sesuai.")

# Contoh pemanggilan fungsi validate_universitas_memiliki
r21_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university\R21_Universitas_memiliki.csv'
universitas_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university\universitas_attribute.csv'
fakultas_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\faculty\fakultas_attribute.csv'

validate_universitas_memiliki(r21_file, universitas_file, fakultas_file)
