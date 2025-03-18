import csv

def validate_penelitian_terkaitDengan(r38_file, penelitian_file, departemen_file):
    # Membaca data dari csv penelitian_attribute.csv
    penelitian_data = {}
    with open(penelitian_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            judul_penelitian = row[0].strip()  # Kolom judulPenelitian
            penelitian_data[judul_penelitian] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari penelitian

    # Membaca data dari csv departemen_attribute.csv
    departemen_data = {}
    with open(departemen_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_departemen = row[0].strip()  # Kolom namaDepartemen
            departemen_data[nama_departemen] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari departemen

    # Validasi data di R38_Penelitian_terkaitDengan.csv
    errors = []
    with open(r38_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            judul_penelitian = row[0].strip()  # Kolom judulPenelitian
            nama_departemen = row[1].strip()  # Kolom namaDepartemen

            # Validasi judulPenelitian
            if judul_penelitian not in penelitian_data:
                errors.append(f"Data salah pada baris {line_num}: Judul penelitian '{judul_penelitian}' tidak ditemukan di penelitian_attribute.csv")

            # Validasi namaDepartemen
            if nama_departemen not in departemen_data:
                errors.append(f"Data salah pada baris {line_num}: Nama departemen '{nama_departemen}' tidak ditemukan di departemen_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r38_file} sesuai.")

# Contoh pemanggilan fungsi validate_penelitian_terkaitDengan
r38_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\research\R38_Penelitian_terkaitDengan.csv'
penelitian_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\research\penelitian_attribute.csv'
departemen_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\academic_department\departemen_attribute.csv'

validate_penelitian_terkaitDengan(r38_file, penelitian_file, departemen_file)
