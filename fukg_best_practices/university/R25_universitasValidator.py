import csv

def validate_universitas_tempatKerja(r25_file, universitas_file, staf_admin_file):
    # Membaca data dari csv universitas_attribute.csv
    universitas_data = {}
    with open(universitas_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_universitas = row[0].strip()  # Kolom namaUniversitas
            universitas_data[nama_universitas] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari universitas

    # Membaca data dari csv stafAdministratif_attribute.csv
    staf_admin_data = {}
    with open(staf_admin_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nip = row[0].strip()  # Kolom NIP
            staf_admin_data[nip] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari staf administratif

    # Validasi data di R25_Universitas_tempatKerja.csv
    errors = []
    with open(r25_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            nama_universitas = row[0].strip()  # Kolom namaUniversitas
            nip = row[1].strip()  # Kolom NIP

            # Validasi namaUniversitas
            if nama_universitas not in universitas_data:
                errors.append(f"Data salah pada baris {line_num}: namaUniversitas {nama_universitas} tidak ditemukan di universitas_attribute.csv")

            # Validasi NIP
            if nip not in staf_admin_data:
                errors.append(f"Data salah pada baris {line_num}: NIP {nip} tidak ditemukan di stafAdministratif_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r25_file} sesuai.")

# Contoh pemanggilan fungsi validate_universitas_tempatKerja
r25_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university\R25_Universitas_tempatKerja.csv'
universitas_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university\universitas_attribute.csv'
staf_admin_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_staff\stafAdministratif_attribute.csv'

validate_universitas_tempatKerja(r25_file, universitas_file, staf_admin_file)
