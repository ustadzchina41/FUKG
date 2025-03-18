import csv

def validate_fakultas_tempatKerja(r20_file, fakultas_file, staf_administratif_file):
    # Membaca data dari csv fakultas_attribute.csv
    fakultas_data = {}
    with open(fakultas_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_fakultas = row[0].strip()  # Kolom namaFakultas
            fakultas_data[nama_fakultas] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari fakultas

    # Membaca data dari csv stafAdministratif_attribute.csv
    staf_admin_data = {}
    with open(staf_administratif_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nip = row[0].strip()  # Kolom NIP
            staf_admin_data[nip] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari staf administratif

    # Validasi data di R20_Fakultas_tempatKerja.csv
    errors = []
    with open(r20_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            nama_fakultas = row[0].strip()  # Kolom namaFakultas
            nip = row[1].strip()  # Kolom NIP

            # Validasi namaFakultas
            if nama_fakultas not in fakultas_data:
                errors.append(f"Data salah pada baris {line_num}: namaFakultas {nama_fakultas} tidak ditemukan di fakultas_attribute.csv")

            # Validasi NIP
            if nip not in staf_admin_data:
                errors.append(f"Data salah pada baris {line_num}: NIP {nip} tidak ditemukan di stafAdministratif_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r20_file} sesuai.")

# Contoh pemanggilan fungsi validate_fakultas_tempatKerja
r20_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\faculty\R20_Fakultas_tempatKerja.csv'
fakultas_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\faculty\fakultas_attribute.csv'
staf_administratif_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_staff\stafAdministratif_attribute.csv'

validate_fakultas_tempatKerja(r20_file, fakultas_file, staf_administratif_file)
