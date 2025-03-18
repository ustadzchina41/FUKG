import csv

def validate_matakuliah_diajarOleh(r30_file, matakuliah_file, dosen_file):
    # Membaca data dari csv mataKuliah_attribute.csv
    matakuliah_data = {}
    with open(matakuliah_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            kode_matakuliah = row[0].strip()  # Kolom kodeMataKuliah
            matakuliah_data[kode_matakuliah] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari mata kuliah

    # Membaca data dari csv dosen_attribute.csv
    dosen_data = {}
    with open(dosen_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nidn = row[0].strip()  # Kolom NIDN
            dosen_data[nidn] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari dosen

    # Validasi data di R30_MataKuliah_diajarOleh.csv
    errors = []
    with open(r30_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            kode_matakuliah = row[0].strip()  # Kolom kodeMataKuliah
            nidn = row[1].strip()  # Kolom NIDN

            # Validasi kodeMataKuliah
            if kode_matakuliah not in matakuliah_data:
                errors.append(f"Data salah pada baris {line_num}: kodeMataKuliah {kode_matakuliah} tidak ditemukan di mataKuliah_attribute.csv")

            # Validasi NIDN
            if nidn not in dosen_data:
                errors.append(f"Data salah pada baris {line_num}: NIDN {nidn} tidak ditemukan di dosen_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r30_file} sesuai.")

# Contoh pemanggilan fungsi validate_matakuliah_diajarOleh
r30_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_course\R30_MataKuliah_diajarOleh.csv'
matakuliah_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_course\mataKuliah_attribute.csv'
dosen_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_lecture\dosen_attribute.csv'

validate_matakuliah_diajarOleh(r30_file, matakuliah_file, dosen_file)
