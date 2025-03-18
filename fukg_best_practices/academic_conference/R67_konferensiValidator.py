import csv

def validate_konferensi_diikutiOleh(r67_file, konferensi_file, dosen_file):
    # Membaca data konferensi dari csv konferensi_attribute.csv
    konferensi_data = {}
    with open(konferensi_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_konferensi = row[0].strip()  # Kolom namaKonferensi
            konferensi_data[nama_konferensi] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari konferensi

    # Membaca data dosen dari csv dosen_attribute.csv
    dosen_data = {}
    with open(dosen_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nidn = row[0].strip()  # Kolom NIDN
            dosen_data[nidn] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari dosen

    # Validasi data di R67_Konferensi_diikutiOleh.csv
    errors = []
    with open(r67_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            nama_konferensi = row[0].strip()  # Kolom namaKonferensi
            nidn = row[1].strip()  # Kolom NIDN

            # Validasi namaKonferensi
            if nama_konferensi not in konferensi_data:
                errors.append(f"Data salah pada baris {line_num}: namaKonferensi '{nama_konferensi}' tidak ditemukan di konferensi_attribute.csv")

            # Validasi NIDN
            if nidn not in dosen_data:
                errors.append(f"Data salah pada baris {line_num}: NIDN '{nidn}' tidak ditemukan di dosen_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r67_file} sesuai.")

# Contoh pemanggilan fungsi validate_konferensi_diikutiOleh
r67_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\academic_conference\R67_Konferensi_diikutiOleh.csv'
konferensi_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\academic_conference\konferensi_attribute.csv'
dosen_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_lecture\dosen_attribute.csv'

validate_konferensi_diikutiOleh(r67_file, konferensi_file, dosen_file)
