import csv

def validate_saranaOlahraga_digunakanOleh(r78_file, sarana_file, mahasiswa_file):
    # Membaca data dari csv saranaOlahraga_attribute.csv
    sarana_data = {}
    with open(sarana_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_fasilitas = row[0].strip()  # Kolom namaFasilitas
            sarana_data[nama_fasilitas] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari sarana olahraga

    # Membaca data dari csv mahasiswa_attribute.csv
    mahasiswa_data = {}
    with open(mahasiswa_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nomor_induk_mahasiswa = row[4].strip()  # Kolom nomorIndukMahasiswa
            mahasiswa_data[nomor_induk_mahasiswa] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari mahasiswa

    # Validasi data di R78_SaranaOlahraga_digunakanOleh.csv
    errors = []
    with open(r78_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            nama_fasilitas = row[0].strip()  # Kolom namaFasilitas
            nomor_induk_mahasiswa = row[1].strip()  # Kolom nomorIndukMahasiswa

            # Validasi namaFasilitas
            if nama_fasilitas not in sarana_data:
                errors.append(f"Data salah pada baris {line_num}: namaFasilitas {nama_fasilitas} tidak ditemukan di saranaOlahraga_attribute.csv")

            # Validasi nomorIndukMahasiswa
            if nomor_induk_mahasiswa not in mahasiswa_data:
                errors.append(f"Data salah pada baris {line_num}: nomorIndukMahasiswa {nomor_induk_mahasiswa} tidak ditemukan di mahasiswa_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r78_file} sesuai.")

# Contoh pemanggilan fungsi validate_saranaOlahraga_digunakanOleh
r78_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\sport_venue\R78_SaranaOlahraga_digunakanOleh.csv'
sarana_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\sport_venue\saranaOlahraga_attribute.csv'
mahasiswa_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_student\mahasiswa_attribute.csv'

validate_saranaOlahraga_digunakanOleh(r78_file, sarana_file, mahasiswa_file)
