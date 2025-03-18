import csv

def validate_workshop_diselenggarakanOleh(r64_file, workshop_file, departemen_file):
    # Membaca data workshop dari csv workshop_attribute.csv
    workshop_data = {}
    with open(workshop_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            judul_workshop = row[0].strip()  # Kolom judulWorkshop
            workshop_data[judul_workshop] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari workshop

    # Membaca data departemen dari csv departemen_attribute.csv
    departemen_data = {}
    with open(departemen_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_departemen = row[0].strip()  # Kolom namaDepartemen
            departemen_data[nama_departemen] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari departemen

    # Validasi data di R64_Workshop_diselenggarakanOleh.csv
    errors = []
    with open(r64_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            judul_workshop = row[0].strip()  # Kolom judulWorkshop
            nama_departemen = row[1].strip()  # Kolom namaDepartemen

            # Validasi judulWorkshop
            if judul_workshop not in workshop_data:
                errors.append(f"Data salah pada baris {line_num}: judulWorkshop '{judul_workshop}' tidak ditemukan di workshop_attribute.csv")

            # Validasi namaDepartemen
            if nama_departemen not in departemen_data:
                errors.append(f"Data salah pada baris {line_num}: namaDepartemen '{nama_departemen}' tidak ditemukan di departemen_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r64_file} sesuai.")

# Contoh pemanggilan fungsi validate_workshop_diselenggarakanOleh
r64_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\academic_workshop\R64_Workshop_diselenggarakanOleh.csv'
workshop_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\academic_workshop\workshop_attribute.csv'
departemen_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\academic_department\departemen_attribute.csv'

validate_workshop_diselenggarakanOleh(r64_file, workshop_file, departemen_file)
