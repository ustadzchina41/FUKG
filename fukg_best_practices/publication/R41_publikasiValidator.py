import csv

def validate_publikasi_berasalDari(r41_file, publikasi_file, penelitian_file):
    # Read data from publikasi_attribute.csv and create dictionary
    publikasi_data = {}
    with open(publikasi_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Skip header
        for row in csvreader:
            judul_publikasi = row[0].strip()  # JudulPublikasi
            publikasi_data[judul_publikasi] = True  # Store in dictionary (using boolean value for existence check)

    # Read data from penelitian_attribute.csv and create dictionary
    penelitian_data = {}
    with open(penelitian_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Skip header
        for row in csvreader:
            judul_penelitian = row[0].strip()  # JudulPenelitian
            penelitian_data[judul_penelitian] = True  # Store in dictionary (using boolean value for existence check)

    # Validate data in R41_Publikasi_berasalDari.csv
    errors = []
    with open(r41_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Skip header
        for line_num, row in enumerate(csvreader, start=2):
            judul_publikasi = row[0].strip()  # JudulPublikasi from R41_Publikasi_berasalDari.csv
            judul_penelitian = row[1].strip()  # JudulPenelitian from R41_Publikasi_berasalDari.csv

            # Validate JudulPublikasi
            if judul_publikasi not in publikasi_data:
                errors.append(f"Data salah pada baris {line_num}: JudulPublikasi '{judul_publikasi}' tidak ditemukan di publikasi_attribute.csv")

            # Validate JudulPenelitian
            if judul_penelitian not in penelitian_data:
                errors.append(f"Data salah pada baris {line_num}: JudulPenelitian '{judul_penelitian}' tidak ditemukan di penelitian_attribute.csv")

    # Print validation result
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r41_file} sesuai.")

# Example usage:
r41_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\publication\R41_Publikasi_berasalDari.csv'
publikasi_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\publication\publikasi_attribute.csv'
penelitian_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\research\penelitian_attribute.csv'

validate_publikasi_berasalDari(r41_file, publikasi_file, penelitian_file)
