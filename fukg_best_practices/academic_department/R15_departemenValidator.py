import csv

def validate_relations(r15_file, departemen_file, penelitian_file):
    # Membaca data dari csv departemen_attribute.csv
    departemen_data = {}
    with open(departemen_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_departemen = row[0].strip()  # Kolom namaDepartemen
            departemen_data[nama_departemen] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari departemen

    # Membaca data dari csv penelitian_attribute.csv
    penelitian_data = {}
    with open(penelitian_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            judul_penelitian = row[0].strip()  # Kolom judulPenelitian
            penelitian_data[judul_penelitian] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari penelitian

    # Validasi data di R15_Departemen_tempatPenelitian.csv
    errors = []
    with open(r15_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            nama_departemen = row[0].strip()  # Kolom namaDepartemen
            judul_penelitian = row[1].strip()  # Kolom judulPenelitian

            # Validasi namaDepartemen
            if nama_departemen not in departemen_data:
                errors.append(f"Data salah pada baris {line_num}: namaDepartemen {nama_departemen} tidak ditemukan di departemen_attribute.csv")

            # Validasi judulPenelitian
            if judul_penelitian not in penelitian_data:
                errors.append(f"Data salah pada baris {line_num}: judulPenelitian {judul_penelitian} tidak ditemukan di penelitian_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r15_file} sesuai.")

# Panggil fungsi validate_relations dengan nama file CSV yang sesuai
r15_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\academic_department\R15_Departemen_tempatPenelitian.csv'
departemen_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\academic_department\departemen_attribute.csv'
penelitian_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\research\penelitian_attribute.csv'

validate_relations(r15_file, departemen_file, penelitian_file)
