import csv

def validate_jurnal_mengandung(r49_file, jurnal_file, artikel_file):
    # Membaca data jurnal dari csv jurnal_attribute.csv
    jurnal_data = {}
    with open(jurnal_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_jurnal = row[0].strip()  # Kolom namaJurnal
            jurnal_data[nama_jurnal] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari jurnal

    # Membaca data artikel dari csv artikel_attribute.csv
    artikel_data = {}
    with open(artikel_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            judul_artikel = row[0].strip()  # Kolom judulArtikel
            artikel_data[judul_artikel] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari artikel

    # Validasi data di R49_Jurnal_mengandung.csv
    errors = []
    with open(r49_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            nama_jurnal = row[0].strip()  # Kolom namaJurnal
            judul_artikel = row[1].strip()  # Kolom judulArtikel

            # Validasi namaJurnal
            if nama_jurnal not in jurnal_data:
                errors.append(f"Data salah pada baris {line_num}: namaJurnal '{nama_jurnal}' tidak ditemukan di jurnal_attribute.csv")

            # Validasi judulArtikel
            if judul_artikel not in artikel_data:
                errors.append(f"Data salah pada baris {line_num}: judulArtikel '{judul_artikel}' tidak ditemukan di artikel_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r49_file} sesuai.")

# Contoh pemanggilan fungsi validate_jurnal_mengandung
r49_file = r'C:\Users\RAJA\project\fukg\fukg_best_practicesscientific_journal\R49_Jurnal_mengandung.csv'
jurnal_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\scientific_journal\jurnal_attribute.csv'
artikel_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\article\artikel_attribute.csv'

validate_jurnal_mengandung(r49_file, jurnal_file, artikel_file)
