import csv

def validate_organisasi_bagianDari(r28_file, organisasi_file, universitas_file):
    # Membaca data dari csv organisasiMahasiswa_attribute.csv
    organisasi_data = {}
    with open(organisasi_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_organisasi = row[0].strip()  # Kolom namaOrganisasi
            organisasi_data[nama_organisasi] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari organisasi

    # Membaca data dari csv universitas_attribute.csv
    universitas_data = {}
    with open(universitas_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_universitas = row[0].strip()  # Kolom namaUniversitas
            universitas_data[nama_universitas] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari universitas

    # Validasi data di R28_OrganisasiMahasiswa_bagianDari.csv
    errors = []
    with open(r28_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            nama_organisasi = row[0].strip()  # Kolom namaOrganisasi
            nama_universitas = row[1].strip()  # Kolom namaUniversitas

            # Validasi namaOrganisasi
            if nama_organisasi not in organisasi_data:
                errors.append(f"Data salah pada baris {line_num}: namaOrganisasi {nama_organisasi} tidak ditemukan di organisasiMahasiswa_attribute.csv")

            # Validasi namaUniversitas
            if nama_universitas not in universitas_data:
                errors.append(f"Data salah pada baris {line_num}: namaUniversitas {nama_universitas} tidak ditemukan di universitas_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r28_file} sesuai.")

# Contoh pemanggilan fungsi validate_organisasi_bagianDari
r28_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\student_organization\R28_OrganisasiMahasiswa_bagianDari.csv'
organisasi_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\student_organization\organisasiMahasiswa_attribute.csv'
universitas_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university\universitas_attribute.csv'

validate_organisasi_bagianDari(r28_file, organisasi_file, universitas_file)
