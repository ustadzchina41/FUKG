import csv

def validate_relations(r5_file, dosen_file, penelitian_file):
    # Membaca data dari csv dosen_attribute.csv
    dosen_data = {}
    with open(dosen_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nidn = row[0].strip()  # Kolom NIDN
            dosen_data[nidn] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari dosen

    # Membaca data dari csv penelitian_attribute.csv
    penelitian_data = {}
    with open(penelitian_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            judul_penelitian = row[0].strip()  # Kolom judulPenelitian
            penelitian_data[judul_penelitian] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari penelitian

    # Validasi data di R5_dosen_melakukanPenelitian.csv
    errors = []
    with open(r5_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            nidn = row[0].strip()  # Kolom NIDN
            judul_penelitian = row[1].strip()  # Kolom judulPenelitian

            # Validasi NIDN
            if nidn not in dosen_data:
                errors.append(f"Data salah pada baris {line_num}: NIDN {nidn} tidak ditemukan di dosen_attribute.csv")

            # Validasi judulPenelitian
            if judul_penelitian not in penelitian_data:
                errors.append(f"Data salah pada baris {line_num}: judulPenelitian '{judul_penelitian}' tidak ditemukan di penelitian_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r5_file} sesuai.")

# Panggil fungsi validate_relations dengan nama file CSV yang sesuai
r5_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_lecture\R5_dosen_melakukanPenelitian.csv'
dosen_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_lecture\dosen_attribute.csv'
penelitian_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\research\penelitian_attribute.csv'

validate_relations(r5_file, dosen_file, penelitian_file)
