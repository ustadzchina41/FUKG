import csv

def validate_workshop_diselenggarakanOleh(r65_file, workshop_file, organisasi_file):
    # Membaca data workshop dari csv workshop_attribute.csv
    workshop_data = {}
    with open(workshop_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            judul_workshop = row[0].strip()  # Kolom judulWorkshop
            workshop_data[judul_workshop] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari workshop

    # Membaca data organisasi dari csv organisasiMahasiswa.csv
    organisasi_data = {}
    with open(organisasi_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_organisasi = row[0].strip()  # Kolom namaOrganisasi
            organisasi_data[nama_organisasi] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari organisasi

    # Validasi data di R65_Workshop_diselenggarakanOleh.csv
    errors = []
    with open(r65_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            judul_workshop = row[0].strip()  # Kolom judulWorkshop
            nama_organisasi = row[1].strip()  # Kolom namaOrganisasi

            # Validasi judulWorkshop
            if judul_workshop not in workshop_data:
                errors.append(f"Data salah pada baris {line_num}: judulWorkshop '{judul_workshop}' tidak ditemukan di workshop_attribute.csv")

            # Validasi namaOrganisasi
            if nama_organisasi not in organisasi_data:
                errors.append(f"Data salah pada baris {line_num}: namaOrganisasi '{nama_organisasi}' tidak ditemukan di organisasiMahasiswa.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r65_file} sesuai.")

# Contoh pemanggilan fungsi validate_workshop_diselenggarakanOleh
r65_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\academic_workshop\R65_Workshop_diselenggarakanOleh.csv'
workshop_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\academic_workshop\workshop_attribute.csv'
organisasi_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\student_organization\organisasiMahasiswa_attribute.csv'

validate_workshop_diselenggarakanOleh(r65_file, workshop_file, organisasi_file)
