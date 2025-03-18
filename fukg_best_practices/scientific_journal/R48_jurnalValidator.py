import csv

def validate_jurnal_terdapatDi(r48_file, jurnal_file, perpustakaan_file):
    # Membaca data jurnal dari csv jurnal_attribute.csv
    jurnal_data = {}
    with open(jurnal_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_jurnal = row[0].strip()  # Kolom namaJurnal
            jurnal_data[nama_jurnal] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari jurnal

    # Membaca data perpustakaan dari csv perpustakaan_attribute.csv
    perpustakaan_data = {}
    with open(perpustakaan_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_perpustakaan = row[0].strip()  # Kolom namaPerpustakaan
            perpustakaan_data[nama_perpustakaan] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari perpustakaan

    # Validasi data di R48_Jurnal_terdapatDi.csv
    errors = []
    with open(r48_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            nama_jurnal = row[0].strip()  # Kolom namaJurnal
            nama_perpustakaan = row[1].strip()  # Kolom namaPerpustakaan

            # Validasi namaJurnal
            if nama_jurnal not in jurnal_data:
                errors.append(f"Data salah pada baris {line_num}: namaJurnal '{nama_jurnal}' tidak ditemukan di jurnal_attribute.csv")

            # Validasi namaPerpustakaan
            if nama_perpustakaan not in perpustakaan_data:
                errors.append(f"Data salah pada baris {line_num}: namaPerpustakaan '{nama_perpustakaan}' tidak ditemukan di perpustakaan_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r48_file} sesuai.")

# Contoh pemanggilan fungsi validate_jurnal_terdapatDi
r48_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\scientific_journal\R48_Jurnal_terdapatDi.csv'
jurnal_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\scientific_journal\jurnal_attribute.csv'
perpustakaan_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\academic_library\perpustakaan_attribute.csv'

validate_jurnal_terdapatDi(r48_file, jurnal_file, perpustakaan_file)
