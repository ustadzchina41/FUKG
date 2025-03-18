import csv

def validate_universitas_tempatBelajar(r23_file, universitas_file, mahasiswa_file):
    # Membaca data dari csv universitas_attribute.csv
    universitas_data = {}
    with open(universitas_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_universitas = row[0].strip()  # Kolom namaUniversitas
            universitas_data[nama_universitas] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari universitas

    # Membaca data dari csv mahasiswa_attribute.csv
    mahasiswa_data = {}
    with open(mahasiswa_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nomor_induk_mahasiswa = row[4].strip()  # Kolom nomorIndukMahasiswa
            mahasiswa_data[nomor_induk_mahasiswa] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari mahasiswa

    # Validasi data di R23_Universitas_tempatBelajar.csv
    errors = []
    with open(r23_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            nama_universitas = row[0].strip()  # Kolom namaUniversitas
            nomor_induk_mahasiswa = row[1].strip()  # Kolom nomorIndukMahasiswa

            # Validasi namaUniversitas
            if nama_universitas not in universitas_data:
                errors.append(f"Data salah pada baris {line_num}: namaUniversitas {nama_universitas} tidak ditemukan di universitas_attribute.csv")

            # Validasi nomorIndukMahasiswa
            if nomor_induk_mahasiswa not in mahasiswa_data:
                errors.append(f"Data salah pada baris {line_num}: nomorIndukMahasiswa {nomor_induk_mahasiswa} tidak ditemukan di mahasiswa_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r23_file} sesuai.")

# Contoh pemanggilan fungsi validate_universitas_tempatBelajar
r23_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university\R23_Universitas_tempatBelajar.csv'
universitas_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university\universitas_attribute.csv'
mahasiswa_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_student\mahasiswa_attribute.csv'

validate_universitas_tempatBelajar(r23_file, universitas_file, mahasiswa_file)
