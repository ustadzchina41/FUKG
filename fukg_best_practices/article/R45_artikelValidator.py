import csv

def validate_artikel_terdapatDi(r45_file, artikel_file, perpustakaan_file):
    # Read data from artikel_attribute.csv and create dictionary
    artikel_data = {}
    with open(artikel_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Skip header
        for row in csvreader:
            judul_artikel = row[0].strip()  # JudulArtikel
            artikel_data[judul_artikel] = True  # Store in dictionary (using boolean value for existence check)

   # Membaca data jurnal dari csv jurnal_attribute.csv
    jurnal_data = {}
    with open(jurnal_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_jurnal = row[0].strip()  # Kolom namaJurnal
            jurnal_data[nama_jurnal] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari jurnal

    # Validate data in R45_Artikel_terdapatDi.csv
    errors = []
    with open(r45_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Skip header
        for line_num, row in enumerate(csvreader, start=2):
            judul_artikel = row[0].strip()  # JudulArtikel from R45_Artikel_terdapatDi.csv
            nama_jurnal = row[1].strip()  # NamaJurnal from R45_Artikel_terdapatDi.csv

            # Validate JudulArtikel
            if judul_artikel not in artikel_data:
                errors.append(f"Data salah pada baris {line_num}: JudulArtikel '{judul_artikel}' tidak ditemukan di artikel_attribute.csv")

            # Validate NamaPerpustakaan
            if nama_jurnal not in jurnal_data:
                errors.append(f"Data salah pada baris {line_num}: NamaJurnal '{nama_jurnal}' tidak ditemukan di jurnal_attribute.csv")

    # Print validation result
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r45_file} sesuai.")

# Example usage:
r45_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\article\R45_Artikel_terdapatDi.csv'
artikel_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\article\artikel_attribute.csv'
jurnal_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\scientific_journal\jurnal_attribute.csv'

validate_artikel_terdapatDi(r45_file, artikel_file, jurnal_file)
