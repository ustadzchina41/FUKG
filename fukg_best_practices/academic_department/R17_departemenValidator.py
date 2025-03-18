import csv

def validate_relations(r17_file, departemen_file, staf_administratif_file):
    # Membaca data dari csv departemen_attribute.csv
    departemen_data = {}
    with open(departemen_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_departemen = row[0].strip()  # Kolom namaDepartemen
            departemen_data[nama_departemen] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari departemen

    # Membaca data dari csv stafAdministratif_attribute.csv
    staf_administratif_data = {}
    with open(staf_administratif_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nip = row[0].strip()  # Kolom NIP
            staf_administratif_data[nip] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari staf administratif

    # Validasi data di R17_Departemen_tempatKerja.csv
    errors = []
    with open(r17_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            nama_departemen = row[0].strip()  # Kolom namaDepartemen
            nip = row[1].strip()  # Kolom NIP

            # Validasi namaDepartemen
            if nama_departemen not in departemen_data:
                errors.append(f"Data salah pada baris {line_num}: namaDepartemen {nama_departemen} tidak ditemukan di departemen_attribute.csv")

            # Validasi NIP
            if nip not in staf_administratif_data:
                errors.append(f"Data salah pada baris {line_num}: NIP {nip} tidak ditemukan di stafAdministratif_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r17_file} sesuai.")

# Panggil fungsi validate_relations dengan nama file CSV yang sesuai
r17_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\academic_department\R17_Departemen_tempatKerja.csv'
departemen_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\academic_department\departemen_attribute.csv'
staf_administratif_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_staff\stafAdministratif_attribute.csv'

validate_relations(r17_file, departemen_file, staf_administratif_file)
