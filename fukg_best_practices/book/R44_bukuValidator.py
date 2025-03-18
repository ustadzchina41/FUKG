import csv

def validate_buku_digunakanOleh(r44_file, buku_file, mahasiswa_file):
    # Read data from buku_attribute.csv and create dictionary
    buku_data = {}
    with open(buku_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Skip header
        for row in csvreader:
            judul_buku = row[0].strip()  # JudulBuku
            buku_data[judul_buku] = True  # Store in dictionary (using boolean value for existence check)

    # Read data from mahasiswa_attribute.csv and create dictionary
    mahasiswa_data = {}
    with open(mahasiswa_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Skip header
        for row in csvreader:
            nomor_induk = row[4].strip()  # NomorIndukMahasiswa
            mahasiswa_data[nomor_induk] = True  # Store in dictionary (using boolean value for existence check)

    # Validate data in R44_Buku_digunakanOleh.csv
    errors = []
    with open(r44_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Skip header
        for line_num, row in enumerate(csvreader, start=2):
            judul_buku = row[0].strip()  # JudulBuku from R44_Buku_digunakanOleh.csv
            nomor_induk = row[1].strip()  # NomorIndukMahasiswa from R44_Buku_digunakanOleh.csv

            # Validate JudulBuku
            if judul_buku not in buku_data:
                errors.append(f"Data salah pada baris {line_num}: JudulBuku '{judul_buku}' tidak ditemukan di buku_attribute.csv")

            # Validate NomorIndukMahasiswa
            if nomor_induk not in mahasiswa_data:
                errors.append(f"Data salah pada baris {line_num}: NomorIndukMahasiswa '{nomor_induk}' tidak ditemukan di mahasiswa_attribute.csv")

    # Print validation result
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r44_file} sesuai.")

# Example usage:
r44_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\book\R44_Buku_digunakanOleh.csv'
buku_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\buku_attribute.csv'
mahasiswa_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_student\mahasiswa_attribute.csv'

validate_buku_digunakanOleh(r44_file, buku_file, mahasiswa_file)
