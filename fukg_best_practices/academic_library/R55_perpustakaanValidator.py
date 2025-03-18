import csv

def validate_perpustakaan_bagianDari(r55_file, perpustakaan_file, universitas_file):
    # Membaca data perpustakaan dari csv perpustakaan_attribute.csv
    perpustakaan_data = {}
    with open(perpustakaan_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_perpustakaan = row[0].strip()  # Kolom namaPerpustakaan
            perpustakaan_data[nama_perpustakaan] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari perpustakaan

    # Membaca data universitas dari csv universitas_attribute.csv
    universitas_data = {}
    with open(universitas_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_universitas = row[0].strip()  # Kolom namaUniversitas
            universitas_data[nama_universitas] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari universitas

    # Validasi data di R55_Perpustakaan_bagianDari.csv
    errors = []
    with open(r55_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            nama_perpustakaan = row[0].strip()  # Kolom namaPerpustakaan
            nama_universitas = row[1].strip()  # Kolom namaUniversitas

            # Validasi namaPerpustakaan
            if nama_perpustakaan not in perpustakaan_data:
                errors.append(f"Data salah pada baris {line_num}: namaPerpustakaan '{nama_perpustakaan}' tidak ditemukan di perpustakaan_attribute.csv")

            # Validasi namaUniversitas
            if nama_universitas not in universitas_data:
                errors.append(f"Data salah pada baris {line_num}: namaUniversitas '{nama_universitas}' tidak ditemukan di universitas_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r55_file} sesuai.")

# Contoh pemanggilan fungsi validate_perpustakaan_bagianDari
r55_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\academic_library\R55_Perpustakaan_bagianDari.csv'
perpustakaan_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\academic_library\perpustakaan_attribute.csv'
universitas_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university\universitas_attribute.csv'

validate_perpustakaan_bagianDari(r55_file, perpustakaan_file, universitas_file)
