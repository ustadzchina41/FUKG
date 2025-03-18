import csv

def validate_buku_terdapatDi(r42_file, buku_file, perpustakaan_file):
    # Read data from buku_attribute.csv and create dictionary
    buku_data = {}
    with open(buku_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Skip header
        for row in csvreader:
            judul_buku = row[0].strip()  # JudulBuku
            buku_data[judul_buku] = True  # Store in dictionary (using boolean value for existence check)

    # Read data from perpustakaan_attribut.csv and create dictionary
    perpustakaan_data = {}
    with open(perpustakaan_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Skip header
        for row in csvreader:
            nama_perpustakaan = row[0].strip()  # NamaPerpustakaan
            perpustakaan_data[nama_perpustakaan] = True  # Store in dictionary (using boolean value for existence check)

    # Validate data in R42_Buku_terdapatDi.csv
    errors = []
    with open(r42_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Skip header
        for line_num, row in enumerate(csvreader, start=2):
            judul_buku = row[0].strip()  # JudulBuku from R42_Buku_terdapatDi.csv
            nama_perpustakaan = row[1].strip()  # NamaPerpustakaan from R42_Buku_terdapatDi.csv

            # Validate JudulBuku
            if judul_buku not in buku_data:
                errors.append(f"Data salah pada baris {line_num}: JudulBuku '{judul_buku}' tidak ditemukan di buku_attribute.csv")

            # Validate NamaPerpustakaan
            if nama_perpustakaan not in perpustakaan_data:
                errors.append(f"Data salah pada baris {line_num}: NamaPerpustakaan '{nama_perpustakaan}' tidak ditemukan di perpustakaan_attribut.csv")

    # Print validation result
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r42_file} sesuai.")

# Example usage:
r42_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\book\R42_Buku_terdapatDi.csv'
buku_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\book\buku_attribute.csv'
perpustakaan_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\academic_library\perpustakaan_attribute.csv'

validate_buku_terdapatDi(r42_file, buku_file, perpustakaan_file)
