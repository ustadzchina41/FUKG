import csv

def validate_laboratorium_digunakanUntuk(r51_file, laboratorium_file, penelitian_file):
    # Membaca data laboratorium dari csv laboratorium_attribute.csv
    laboratorium_data = {}
    with open(laboratorium_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_laboratorium = row[0].strip()  # Kolom namaLaboratorium
            laboratorium_data[nama_laboratorium] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari laboratorium

    # Membaca data penelitian dari csv penelitian_attribute.csv
    penelitian_data = {}
    with open(penelitian_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            judul_penelitian = row[0].strip()  # Kolom judulPenelitian
            penelitian_data[judul_penelitian] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari penelitian

    # Validasi data di R51_Laboratorium_digunakanUntuk.csv
    errors = []
    with open(r51_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            nama_laboratorium = row[0].strip()  # Kolom namaLaboratorium
            judul_penelitian = row[1].strip()  # Kolom judulPenelitian

            # Validasi namaLaboratorium
            if nama_laboratorium not in laboratorium_data:
                errors.append(f"Data salah pada baris {line_num}: namaLaboratorium '{nama_laboratorium}' tidak ditemukan di laboratorium_attribute.csv")

            # Validasi judulPenelitian
            if judul_penelitian not in penelitian_data:
                errors.append(f"Data salah pada baris {line_num}: judulPenelitian '{judul_penelitian}' tidak ditemukan di penelitian_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r51_file} sesuai.")

# Contoh pemanggilan fungsi validate_laboratorium_digunakanUntuk
r51_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_laboratory\R51_Laboratorium_digunakanUntuk.csv'
laboratorium_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_laboratory\laboratorium_attribute.csv'
penelitian_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\research\penelitian_attribute.csv'

validate_laboratorium_digunakanUntuk(r51_file, laboratorium_file, penelitian_file)
