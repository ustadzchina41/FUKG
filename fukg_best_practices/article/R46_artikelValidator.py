import csv

def validate_artikel_digunakanOleh(r46_file, artikel_file, dosen_file):
    # Read data from artikel_attribute.csv and create dictionary
    artikel_data = {}
    with open(artikel_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Skip header
        for row in csvreader:
            judul_artikel = row[0].strip()  # JudulArtikel
            artikel_data[judul_artikel] = True  # Store in dictionary (using boolean value for existence check)

    # Read data from dosen_attribute.csv and create dictionary
    dosen_data = {}
    with open(dosen_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Skip header
        for row in csvreader:
            nidn = row[0].strip()  # NIDN
            dosen_data[nidn] = True  # Store in dictionary (using boolean value for existence check)

    # Validate data in R46_Artikel_digunakanOleh.csv
    errors = []
    with open(r46_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Skip header
        for line_num, row in enumerate(csvreader, start=2):
            judul_artikel = row[0].strip()  # JudulArtikel from R46_Artikel_digunakanOleh.csv
            nidn = row[1].strip()  # NIDN from R46_Artikel_digunakanOleh.csv

            # Validate JudulArtikel
            if judul_artikel not in artikel_data:
                errors.append(f"Data salah pada baris {line_num}: JudulArtikel '{judul_artikel}' tidak ditemukan di artikel_attribute.csv")

            # Validate NIDN
            if nidn not in dosen_data:
                errors.append(f"Data salah pada baris {line_num}: NIDN '{nidn}' tidak ditemukan di dosen_attribute.csv")

    # Print validation result
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r46_file} sesuai.")

# Example usage:
r46_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\article\R46_Artikel_digunakanOleh.csv'
artikel_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\article\artikel_attribute.csv'
dosen_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_lecture\dosen_attribute.csv'

validate_artikel_digunakanOleh(r46_file, artikel_file, dosen_file)
