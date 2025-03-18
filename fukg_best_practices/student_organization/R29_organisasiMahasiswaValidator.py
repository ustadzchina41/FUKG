import csv

def validate_organisasi_bagianDari_fakultas(r29_file, organisasi_file, fakultas_file):
    # Membaca data dari csv organisasiMahasiswa_attribute.csv
    organisasi_data = {}
    with open(organisasi_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_organisasi = row[0].strip()  # Kolom namaOrganisasi
            organisasi_data[nama_organisasi] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari organisasi

    # Membaca data dari csv fakultas_attribute.csv
    fakultas_data = {}
    with open(fakultas_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_fakultas = row[0].strip()  # Kolom namaFakultas
            fakultas_data[nama_fakultas] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari fakultas

    # Validasi data di R29_OrganisasiMahasiswa_bagianDari.csv
    errors = []
    with open(r29_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            nama_organisasi = row[0].strip()  # Kolom namaOrganisasi
            nama_fakultas = row[1].strip()  # Kolom namaFakultas

            # Validasi namaOrganisasi
            if nama_organisasi not in organisasi_data:
                errors.append(f"Data salah pada baris {line_num}: namaOrganisasi {nama_organisasi} tidak ditemukan di organisasiMahasiswa_attribute.csv")

            # Validasi namaFakultas
            if nama_fakultas not in fakultas_data:
                errors.append(f"Data salah pada baris {line_num}: namaFakultas {nama_fakultas} tidak ditemukan di fakultas_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r29_file} sesuai.")

# Contoh pemanggilan fungsi validate_organisasi_bagianDari_fakultas
r29_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\student_organization\R29_OrganisasiMahasiswa_bagianDari.csv'
organisasi_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\student_organization\organisasiMahasiswa_attribute.csv'
fakultas_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\faculty\fakultas_attribute.csv'

validate_organisasi_bagianDari_fakultas(r29_file, organisasi_file, fakultas_file)
