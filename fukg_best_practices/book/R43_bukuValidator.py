import csv

def validate_buku_digunakanOleh(r43_file, buku_file, dosen_file):
    # Read data from buku_attribute.csv and create dictionary
    buku_data = {}
    with open(buku_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Skip header
        for row in csvreader:
            judul_buku = row[0].strip()  # JudulBuku
            buku_data[judul_buku] = True  # Store in dictionary (using boolean value for existence check)

    # Read data from dosen_attribute.csv and create dictionary
    dosen_data = {}
    with open(dosen_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Skip header
        for row in csvreader:
            nidn = row[0].strip()  # NIDN
            dosen_data[nidn] = True  # Store in dictionary (using boolean value for existence check)

    # Validate data in R43_Buku_digunakanOleh.csv
    errors = []
    with open(r43_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Skip header
        for line_num, row in enumerate(csvreader, start=2):
            judul_buku = row[0].strip()  # JudulBuku from R43_Buku_digunakanOleh.csv
            nidn = row[1].strip()  # NIDN from R43_Buku_digunakanOleh.csv

            # Validate JudulBuku
            if judul_buku not in buku_data:
                errors.append(f"Data salah pada baris {line_num}: JudulBuku '{judul_buku}' tidak ditemukan di buku_attribute.csv")

            # Validate NIDN
            if nidn not in dosen_data:
                errors.append(f"Data salah pada baris {line_num}: NIDN '{nidn}' tidak ditemukan di dosen_attribute.csv")

    # Print validation result
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r43_file} sesuai.")

# Example usage:
r43_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\book\R43_Buku_digunakanOleh.csv'
buku_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\book\buku_attribute.csv'
dosen_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_lecture\dosen_attribute.csv'

validate_buku_digunakanOleh(r43_file, buku_file, dosen_file)
