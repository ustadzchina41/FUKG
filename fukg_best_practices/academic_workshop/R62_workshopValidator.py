import csv

def validate_workshop_diikutiOleh(r62_file, workshop_file, dosen_file):
    # Membaca data workshop dari csv workshop_attribute.csv
    workshop_data = {}
    with open(workshop_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            judul_workshop = row[0].strip()  # Kolom judulWorkshop
            workshop_data[judul_workshop] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari workshop

    # Membaca data dosen dari csv dosen_attribute.csv
    dosen_data = {}
    with open(dosen_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nidn = row[0].strip()  # Kolom NIDN
            dosen_data[nidn] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari dosen

    # Validasi data di R62_Workshop_diikutiOleh.csv
    errors = []
    with open(r62_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            judul_workshop = row[0].strip()  # Kolom judulWorkshop
            nidn = row[1].strip()  # Kolom NIDN

            # Validasi judulWorkshop
            if judul_workshop not in workshop_data:
                errors.append(f"Data salah pada baris {line_num}: judulWorkshop '{judul_workshop}' tidak ditemukan di workshop_attribute.csv")

            # Validasi NIDN
            if nidn not in dosen_data:
                errors.append(f"Data salah pada baris {line_num}: NIDN '{nidn}' tidak ditemukan di dosen_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r62_file} sesuai.")

# Contoh pemanggilan fungsi validate_workshop_diikutiOleh
r62_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\academic_workshop\R62_Workshop_diikutiOleh.csv'
workshop_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\academic_workshop\workshop_attribute.csv'
dosen_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_lecture\dosen_attribute.csv'

validate_workshop_diikutiOleh(r62_file, workshop_file, dosen_file)
