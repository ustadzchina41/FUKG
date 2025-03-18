import csv

def validate_universitas_memiliki(r22_file, universitas_file, departemen_file):
    # Membaca data dari csv universitas_attribute.csv
    universitas_data = {}
    with open(universitas_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_universitas = row[0].strip()  # Kolom namaUniversitas
            universitas_data[nama_universitas] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari universitas

    # Membaca data dari csv departemen_attribute.csv
    departemen_data = {}
    with open(departemen_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_departemen = row[0].strip()  # Kolom namaDepartemen
            departemen_data[nama_departemen] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari departemen

    # Validasi data di R22_Universitas_memiliki.csv
    errors = []
    with open(r22_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            nama_universitas = row[0].strip()  # Kolom namaUniversitas
            nama_departemen = row[1].strip()  # Kolom namaDepartemen

            # Validasi namaUniversitas
            if nama_universitas not in universitas_data:
                errors.append(f"Data salah pada baris {line_num}: namaUniversitas {nama_universitas} tidak ditemukan di universitas_attribute.csv")

            # Validasi namaDepartemen
            if nama_departemen not in departemen_data:
                errors.append(f"Data salah pada baris {line_num}: namaDepartemen {nama_departemen} tidak ditemukan di departemen_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r22_file} sesuai.")

# Contoh pemanggilan fungsi validate_universitas_memiliki
r22_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university\R22_Universitas_memiliki.csv'
universitas_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university\universitas_attribute.csv'
departemen_file = r'C:\Users\RAJA\project\fukg\fukg_best_practicesacademic_department\departemen_attribute.csv'

validate_universitas_memiliki(r22_file, universitas_file, departemen_file)
