import csv

def validate_saranaOlahraga_bagianDari(r77_file, sarana_file, universitas_file):
    # Membaca data dari csv saranaOlahraga_attribute.csv
    sarana_data = {}
    with open(sarana_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_fasilitas = row[0].strip()  # Kolom namaFasilitas
            sarana_data[nama_fasilitas] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari sarana olahraga

    # Membaca data dari csv universitas_attribute.csv
    universitas_data = {}
    with open(universitas_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_universitas = row[0].strip()  # Kolom namaUniversitas
            universitas_data[nama_universitas] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari universitas

    # Validasi data di R77_SaranaOlahraga_bagianDari.csv
    errors = []
    with open(r77_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            nama_fasilitas = row[0].strip()  # Kolom namaFasilitas
            nama_universitas = row[1].strip()  # Kolom namaUniversitas

            # Validasi namaFasilitas
            if nama_fasilitas not in sarana_data:
                errors.append(f"Data salah pada baris {line_num}: namaFasilitas {nama_fasilitas} tidak ditemukan di saranaOlahraga_attribute.csv")

            # Validasi namaUniversitas
            if nama_universitas not in universitas_data:
                errors.append(f"Data salah pada baris {line_num}: namaUniversitas {nama_universitas} tidak ditemukan di universitas_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r77_file} sesuai.")

# Contoh pemanggilan fungsi validate_saranaOlahraga_bagianDari
r77_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\sport_venue\R77_SaranaOlahraga_bagianDari.csv'
sarana_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\sport_venue\saranaOlahraga_attribute.csv'
universitas_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university\universitas_attribute.csv'

validate_saranaOlahraga_bagianDari(r77_file, sarana_file, universitas_file)
