import csv

def validate_asrama_bagianDari(r80_file, asrama_file, universitas_file):
    # Membaca data dari csv asrama_attribute.csv
    asrama_data = {}
    with open(asrama_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_asrama = row[0].strip()  # Kolom namaAsrama
            asrama_data[nama_asrama] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari asrama

    # Membaca data dari csv universitas_attribute.csv
    universitas_data = {}
    with open(universitas_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_universitas = row[0].strip()  # Kolom namaUniversitas
            universitas_data[nama_universitas] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari universitas

    # Validasi data di R80_Asrama_bagianDari.csv
    errors = []
    with open(r80_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            nama_asrama = row[0].strip()  # Kolom namaAsrama
            nama_universitas = row[1].strip()  # Kolom namaUniversitas

            # Validasi namaAsrama
            if nama_asrama not in asrama_data:
                errors.append(f"Data salah pada baris {line_num}: namaAsrama {nama_asrama} tidak ditemukan di asrama_attribute.csv")

            # Validasi namaUniversitas
            if nama_universitas not in universitas_data:
                errors.append(f"Data salah pada baris {line_num}: namaUniversitas {nama_universitas} tidak ditemukan di universitas_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r80_file} sesuai.")

# Contoh pemanggilan fungsi validate_asrama_bagianDari
r80_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_dormitory\R80_Asrama_bagianDari.csv'
asrama_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_dormitory\asrama_attribute.csv'
universitas_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university\universitas_attribute.csv'

validate_asrama_bagianDari(r80_file, asrama_file, universitas_file)
