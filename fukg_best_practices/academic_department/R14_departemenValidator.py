import csv

def validate_relations(r14_file, departemen_file, mata_kuliah_file):
    # Membaca data dari csv departemen_attribute.csv
    departemen_data = {}
    with open(departemen_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_departemen = row[0].strip()  # Kolom namaDepartemen
            departemen_data[nama_departemen] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari departemen

    # Membaca data dari csv mataKuliah_attribute.csv
    mata_kuliah_data = {}
    with open(mata_kuliah_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            kode_mata_kuliah = row[0].strip()  # Kolom kodeMataKuliah
            mata_kuliah_data[kode_mata_kuliah] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari mata kuliah

    # Validasi data di R14_Departemen_mengelola.csv
    errors = []
    with open(r14_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            nama_departemen = row[0].strip()  # Kolom namaDepartemen
            kode_mata_kuliah = row[1].strip()  # Kolom kodeMataKuliah

            # Validasi namaDepartemen
            if nama_departemen not in departemen_data:
                errors.append(f"Data salah pada baris {line_num}: namaDepartemen {nama_departemen} tidak ditemukan di departemen_attribute.csv")

            # Validasi kodeMataKuliah
            if kode_mata_kuliah not in mata_kuliah_data:
                errors.append(f"Data salah pada baris {line_num}: kodeMataKuliah {kode_mata_kuliah} tidak ditemukan di mataKuliah_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r14_file} sesuai.")

# Panggil fungsi validate_relations dengan nama file CSV yang sesuai
r14_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\academic_department\R14_Departemen_mengelola.csv'
departemen_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\academic_department\departemen_attribute.csv'
mata_kuliah_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_course\mataKuliah_attribute.csv'

validate_relations(r14_file, departemen_file, mata_kuliah_file)
