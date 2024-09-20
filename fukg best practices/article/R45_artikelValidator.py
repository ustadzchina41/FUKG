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

    # Read data from perpustakaan_attribute.csv and create dictionary
    perpustakaan_data = {}
    with open(perpustakaan_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Skip header
        for row in csvreader:
            nama_perpustakaan = row[0].strip()  # NamaPerpustakaan
            perpustakaan_data[nama_perpustakaan] = True  # Store in dictionary (using boolean value for existence check)

    # Validate data in R45_Artikel_terdapatDi.csv
    errors = []
    with open(r45_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Skip header
        for line_num, row in enumerate(csvreader, start=2):
            judul_artikel = row[0].strip()  # JudulArtikel from R45_Artikel_terdapatDi.csv
            nama_perpustakaan = row[1].strip()  # NamaPerpustakaan from R45_Artikel_terdapatDi.csv

            # Validate JudulArtikel
            if judul_artikel not in artikel_data:
                errors.append(f"Data salah pada baris {line_num}: JudulArtikel '{judul_artikel}' tidak ditemukan di artikel_attribute.csv")

            # Validate NamaPerpustakaan
            if nama_perpustakaan not in perpustakaan_data:
                errors.append(f"Data salah pada baris {line_num}: NamaPerpustakaan '{nama_perpustakaan}' tidak ditemukan di perpustakaan_attribute.csv")

    # Print validation result
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r45_file} sesuai.")

# Example usage:
r45_file = r'C:\Users\RAJA\project\fukg\article\R45_Artikel_terdapatDi.csv'
artikel_file = r'C:\Users\RAJA\project\fukg\article\artikel_attribute.csv'
perpustakaan_file = r'C:\Users\RAJA\project\fukg\academic_library\perpustakaan_attribute.csv'

validate_artikel_terdapatDi(r45_file, artikel_file, perpustakaan_file)
