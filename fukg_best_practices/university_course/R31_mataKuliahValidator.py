import csv

def validate_matakuliah_diambilOleh(r31_file, matakuliah_file, mahasiswa_file):
    # Membaca data dari csv mataKuliah_attribute.csv
    matakuliah_data = {}
    with open(matakuliah_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            kode_matakuliah = row[0].strip()  # Kolom kodeMataKuliah
            matakuliah_data[kode_matakuliah] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari mata kuliah

    # Membaca data dari csv mahasiswa_attribute.csv
    mahasiswa_data = {}
    with open(mahasiswa_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nomor_induk_mahasiswa = row[4].strip()  # Kolom nomorIndukMahasiswa
            mahasiswa_data[nomor_induk_mahasiswa] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari mahasiswa

    # Validasi data di R31_MataKuliah_diambilOleh.csv
    errors = []
    with open(r31_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            kode_matakuliah = row[0].strip()  # Kolom kodeMataKuliah
            nomor_induk_mahasiswa = row[1].strip()  # Kolom nomorIndukMahasiswa

            # Validasi kodeMataKuliah
            if kode_matakuliah not in matakuliah_data:
                errors.append(f"Data salah pada baris {line_num}: kodeMataKuliah {kode_matakuliah} tidak ditemukan di mataKuliah_attribute.csv")

            # Validasi nomorIndukMahasiswa
            if nomor_induk_mahasiswa not in mahasiswa_data:
                errors.append(f"Data salah pada baris {line_num}: nomorIndukMahasiswa {nomor_induk_mahasiswa} tidak ditemukan di mahasiswa_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r31_file} sesuai.")

# Contoh pemanggilan fungsi validate_matakuliah_diambilOleh
r31_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_course\R31_MataKuliah_diambilOleh.csv'
matakuliah_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_course\mataKuliah_attribute.csv'
mahasiswa_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_student\mahasiswa_attribute.csv'

validate_matakuliah_diambilOleh(r31_file, matakuliah_file, mahasiswa_file)
