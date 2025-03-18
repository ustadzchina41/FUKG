import csv

def validate_relations(r1_file, mahasiswa_file, mata_kuliah_file):
    # Membaca data dari csv mahasiswa_attribute.csv
    mahasiswa_data = {}
    with open(mahasiswa_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nomor_induk = row[4].strip()  # Kolom nomorIndukMahasiswa
            mahasiswa_data[nomor_induk] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari mahasiswa

    # Membaca data dari csv mataKuliah_attribute.csv
    mata_kuliah_data = {}
    with open(mata_kuliah_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            kode_mata_kuliah = row[0].strip()  # Kolom kodeMataKuliah
            mata_kuliah_data[kode_mata_kuliah] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari mata kuliah

    # Validasi data di R1_mahasiswa_mengambil.csv
    errors = []
    with open(r1_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            nomor_induk = row[0].strip()  # Kolom nomorIndukMahasiswa
            kode_mata_kuliah = row[1].strip()  # Kolom kodeMataKuliah

            # Validasi nomorIndukMahasiswa
            if nomor_induk not in mahasiswa_data:
                errors.append(f"Data salah pada baris {line_num}: nomorIndukMahasiswa {nomor_induk} tidak ditemukan di mahasiswa_attribute.csv")

            # Validasi kodeMataKuliah
            if kode_mata_kuliah not in mata_kuliah_data:
                errors.append(f"Data salah pada baris {line_num}: kodeMataKuliah {kode_mata_kuliah} tidak ditemukan di mataKuliah_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r1_file} sesuai.")

# Panggil fungsi validate_relations dengan nama file CSV yang sesuai
r1_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_student\R1_mahasiswa_mengambil.csv'
mahasiswa_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_student\mahasiswa_attribute.csv'
mata_kuliah_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_course\mataKuliah_attribute.csv'

validate_relations(r1_file, mahasiswa_file, mata_kuliah_file)
