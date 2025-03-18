import csv

def validate_relations(r4_file, dosen_file, mata_kuliah_file):
    # Membaca data dari csv dosen_attribute.csv
    dosen_data = {}
    with open(dosen_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nidn = row[0].strip()  # Kolom NIDN
            dosen_data[nidn] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari dosen

    # Membaca data dari csv mataKuliah_attribute.csv
    mata_kuliah_data = {}
    with open(mata_kuliah_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            kode_mata_kuliah = row[0].strip()  # Kolom kodeMataKuliah
            mata_kuliah_data[kode_mata_kuliah] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari mata kuliah

    # Validasi data di R4_dosen_mengajar.csv
    errors = []
    with open(r4_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            nidn = row[0].strip()  # Kolom NIDN
            kode_mata_kuliah = row[1].strip()  # Kolom kodeMataKuliah

            # Validasi NIDN
            if nidn not in dosen_data:
                errors.append(f"Data salah pada baris {line_num}: NIDN {nidn} tidak ditemukan di dosen_attribute.csv")

            # Validasi kodeMataKuliah
            if kode_mata_kuliah not in mata_kuliah_data:
                errors.append(f"Data salah pada baris {line_num}: kodeMataKuliah {kode_mata_kuliah} tidak ditemukan di mataKuliah_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r4_file} sesuai.")

# Panggil fungsi validate_relations dengan nama file CSV yang sesuai
r4_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_lecture\R4_dosen_mengajar.csv'
dosen_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_lecture\dosen_attribute.csv'
mata_kuliah_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_course\mataKuliah_attribute.csv'

validate_relations(r4_file, dosen_file, mata_kuliah_file)
