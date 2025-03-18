import csv

def validate_seminar_diselenggarakanOleh(r60_file, seminar_file, departemen_file):
    # Membaca data seminar dari csv seminar_attribute.csv
    seminar_data = {}
    with open(seminar_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            judul_seminar = row[0].strip()  # Kolom judulSeminar
            seminar_data[judul_seminar] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari seminar

    # Membaca data departemen dari csv departemen_attribute.csv
    departemen_data = {}
    with open(departemen_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_departemen = row[0].strip()  # Kolom namaDepartemen
            departemen_data[nama_departemen] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari departemen

    # Validasi data di R60_Seminar_diselenggarakanOleh.csv
    errors = []
    with open(r60_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            judul_seminar = row[0].strip()  # Kolom judulSeminar
            nama_departemen = row[1].strip()  # Kolom namaDepartemen

            # Validasi judulSeminar
            if judul_seminar not in seminar_data:
                errors.append(f"Data salah pada baris {line_num}: judulSeminar '{judul_seminar}' tidak ditemukan di seminar_attribute.csv")

            # Validasi namaDepartemen
            if nama_departemen not in departemen_data:
                errors.append(f"Data salah pada baris {line_num}: namaDepartemen '{nama_departemen}' tidak ditemukan di departemen_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r60_file} sesuai.")

# Contoh pemanggilan fungsi validate_seminar_diselenggarakanOleh
r60_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\seminar\R60_Seminar_diselenggarakanOleh.csv'
seminar_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\seminar\seminar_attribute.csv'
departemen_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\academic_department\departemen_attribute.csv'

validate_seminar_diselenggarakanOleh(r60_file, seminar_file, departemen_file)
