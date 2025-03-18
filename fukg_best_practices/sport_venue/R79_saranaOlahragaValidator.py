import csv

def validate_saranaOlahraga_digunakanOleh(r79_file, sarana_file, dosen_file):
    # Membaca data dari csv saranaOlahraga_attribute.csv
    sarana_data = {}
    with open(sarana_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_fasilitas = row[0].strip()  # Kolom namaFasilitas
            sarana_data[nama_fasilitas] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari sarana olahraga

    # Membaca data dari csv dosen_attribute.csv
    dosen_data = {}
    with open(dosen_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nidn = row[0].strip()  # Kolom NIDN
            dosen_data[nidn] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari dosen

    # Validasi data di R79_SaranaOlahraga_digunakanOleh.csv
    errors = []
    with open(r79_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            nama_fasilitas = row[0].strip()  # Kolom namaFasilitas
            nidn = row[1].strip()  # Kolom NIDN

            # Validasi namaFasilitas
            if nama_fasilitas not in sarana_data:
                errors.append(f"Data salah pada baris {line_num}: namaFasilitas {nama_fasilitas} tidak ditemukan di saranaOlahraga_attribute.csv")

            # Validasi NIDN
            if nidn not in dosen_data:
                errors.append(f"Data salah pada baris {line_num}: NIDN {nidn} tidak ditemukan di dosen_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r79_file} sesuai.")

# Contoh pemanggilan fungsi validate_saranaOlahraga_digunakanOleh
r79_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\sport_venue\R79_SaranaOlahraga_digunakanOleh.csv'
sarana_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\sport_venue\saranaOlahraga_attribute.csv'
dosen_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_lecture\dosen_attribute.csv'

validate_saranaOlahraga_digunakanOleh(r79_file, sarana_file, dosen_file)
