import csv

def validate_relations(r11_file, alumni_file, fakultas_file):
    # Membaca data dari csv alumni_attribute.csv
    alumni_data = {}
    with open(alumni_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nomor_induk = row[0].strip()  # Kolom nomorIndukMahasiswa
            alumni_data[nomor_induk] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari alumni

    # Membaca data dari csv fakultas_attribute.csv
    fakultas_data = {}
    with open(fakultas_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_fakultas = row[0].strip()  # Kolom namaFakultas
            fakultas_data[nama_fakultas] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari fakultas

    # Validasi data di R11_Alumni_donaturKe.csv
    errors = []
    with open(r11_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            nomor_induk = row[0].strip()  # Kolom nomorIndukMahasiswa
            nama_fakultas = row[1].strip()  # Kolom namaFakultas

            # Validasi nomorIndukMahasiswa
            if nomor_induk not in alumni_data:
                errors.append(f"Data salah pada baris {line_num}: nomorIndukMahasiswa {nomor_induk} tidak ditemukan di alumni_attribute.csv")

            # Validasi namaFakultas
            if nama_fakultas not in fakultas_data:
                errors.append(f"Data salah pada baris {line_num}: namaFakultas {nama_fakultas} tidak ditemukan di fakultas_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r11_file} sesuai.")

# Panggil fungsi validate_relations dengan nama file CSV yang sesuai
r11_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\alumnus\R11_Alumni_donaturKe.csv'
alumni_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\alumnus\alumni_attribute.csv'
fakultas_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\faculty\fakultas_attribute.csv'

validate_relations(r11_file, alumni_file, fakultas_file)
