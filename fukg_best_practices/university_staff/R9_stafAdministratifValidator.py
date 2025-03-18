import csv

def validate_relations(r9_file, staf_admin_file, departemen_file):
    # Membaca data dari csv stafAdministratif_attribute.csv
    staf_admin_data = {}
    with open(staf_admin_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nip = row[0].strip()  # Kolom NIP
            staf_admin_data[nip] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari staf administratif

    # Membaca data dari csv departemen_attribute.csv
    departemen_data = {}
    with open(departemen_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_departemen = row[0].strip()  # Kolom namaDepartemen
            departemen_data[nama_departemen] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari departemen

    # Validasi data di R9_StafAdministratif_bekerjaDi.csv
    errors = []
    with open(r9_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            nip = row[0].strip()  # Kolom NIP
            nama_departemen = row[1].strip()  # Kolom namaDepartemen

            # Validasi NIP
            if nip not in staf_admin_data:
                errors.append(f"Data salah pada baris {line_num}: NIP {nip} tidak ditemukan di stafAdministratif_attribute.csv")

            # Validasi namaDepartemen
            if nama_departemen not in departemen_data:
                errors.append(f"Data salah pada baris {line_num}: namaDepartemen '{nama_departemen}' tidak ditemukan di departemen_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r9_file} sesuai.")

# Panggil fungsi validate_relations dengan nama file CSV yang sesuai
r9_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_staff\R9_StafAdministratif_bekerjaDi.csv'
staf_admin_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_staff\stafAdministratif_attribute.csv'
departemen_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\academic_departement\departemen_attribute.csv'

validate_relations(r9_file, staf_admin_file, departemen_file)
