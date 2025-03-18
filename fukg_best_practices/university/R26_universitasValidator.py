import csv

def validate_universitas_tempatPenelitian(r26_file, universitas_file, penelitian_file):
    # Membaca data dari csv universitas_attribute.csv
    universitas_data = {}
    with open(universitas_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_universitas = row[0].strip()  # Kolom namaUniversitas
            universitas_data[nama_universitas] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari universitas

    # Membaca data dari csv penelitian_attribute.csv
    penelitian_data = {}
    with open(penelitian_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            judul_penelitian = row[0].strip()  # Kolom judulPenelitian
            penelitian_data[judul_penelitian] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari penelitian

    # Validasi data di R26_Universitas_tempatPenelitian.csv
    errors = []
    with open(r26_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            nama_universitas = row[0].strip()  # Kolom namaUniversitas
            judul_penelitian = row[1].strip()  # Kolom judulPenelitian

            # Validasi namaUniversitas
            if nama_universitas not in universitas_data:
                errors.append(f"Data salah pada baris {line_num}: namaUniversitas {nama_universitas} tidak ditemukan di universitas_attribute.csv")

            # Validasi judulPenelitian
            if judul_penelitian not in penelitian_data:
                errors.append(f"Data salah pada baris {line_num}: judulPenelitian {judul_penelitian} tidak ditemukan di penelitian_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r26_file} sesuai.")

# Contoh pemanggilan fungsi validate_universitas_tempatPenelitian
r26_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university\R26_Universitas_tempatPenelitian.csv'
universitas_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university\universitas_attribute.csv'
penelitian_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\research\penelitian_attribute.csv'

validate_universitas_tempatPenelitian(r26_file, universitas_file, penelitian_file)
