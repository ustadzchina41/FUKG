import csv

def validate_konferensi_universitas(r69_file, konferensi_file, universitas_file):
    # Membaca data konferensi dari csv konferensi_attribute.csv
    konferensi_data = {}
    with open(konferensi_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_konferensi = row[0].strip()  # Kolom namaKonferensi
            konferensi_data[nama_konferensi] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari konferensi

    # Membaca data universitas dari csv universitas_attribute.csv
    universitas_data = {}
    with open(universitas_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_universitas = row[0].strip()  # Kolom namaUniversitas
            universitas_data[nama_universitas] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari universitas

    # Validasi data di R69_Konferensi_diselenggarakanOleh.csv
    errors = []
    with open(r69_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            nama_konferensi = row[0].strip()  # Kolom namaKonferensi
            nama_universitas = row[1].strip()  # Kolom namaUniversitas

            # Validasi namaKonferensi
            if nama_konferensi not in konferensi_data:
                errors.append(f"Data salah pada baris {line_num}: namaKonferensi '{nama_konferensi}' tidak ditemukan di konferensi_attribute.csv")

            # Validasi namaUniversitas
            if nama_universitas not in universitas_data:
                errors.append(f"Data salah pada baris {line_num}: namaUniversitas '{nama_universitas}' tidak ditemukan di universitas_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r69_file} sesuai.")

# Contoh pemanggilan fungsi validate_konferensi_universitas
r69_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\academic_conference\R69_Konferensi_diselenggarakanOleh.csv'
konferensi_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\academic_conference\konferensi_attribute.csv'
universitas_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university\universitas_attribute.csv'

validate_konferensi_universitas(r69_file, konferensi_file, universitas_file)
