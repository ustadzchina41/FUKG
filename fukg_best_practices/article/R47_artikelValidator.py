import csv

def validate_artikel_digunakanOleh(r47_file, artikel_file, mahasiswa_file):
    # Step 1: Read mahasiswa data into a set for quick lookup
    mahasiswa_data = set()
    with open(mahasiswa_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Skip header
        for row in csvreader:
            nomor_induk_mahasiswa = row[4].strip()  # Kolom nomorIndukMahasiswa
            mahasiswa_data.add(nomor_induk_mahasiswa)

    # Step 2: Read artikel data into a set for quick lookup
    artikel_data = set()
    with open(artikel_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Skip header
        for row in csvreader:
            judul_artikel = row[0].strip()  # Kolom judulArtikel
            artikel_data.add(judul_artikel)

    # Step 3: Validate R47_Artikel_digunakanOleh.csv
    errors = []
    with open(r47_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Skip header
        for line_num, row in enumerate(csvreader, start=2):
            judul_artikel = row[0].strip()  # Kolom judulArtikel
            nomor_induk_mahasiswa = row[1].strip()  # Kolom nomorIndukMahasiswa

            # Validate nomorIndukMahasiswa
            if nomor_induk_mahasiswa not in mahasiswa_data:
                errors.append(f"Data salah pada baris {line_num}: nomorIndukMahasiswa {nomor_induk_mahasiswa} tidak ditemukan di {mahasiswa_file}")

            # Validate judulArtikel
            if judul_artikel not in artikel_data:
                errors.append(f"Data salah pada baris {line_num}: judulArtikel '{judul_artikel}' tidak ditemukan di {artikel_file}")

    # Step 4: Print validation results
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r47_file} sesuai.")

# Contoh pemanggilan fungsi validate_artikel_digunakanOleh
r47_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\article\R47_Artikel_digunakanOleh.csv'
artikel_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\article\artikel_attribute.csv'
mahasiswa_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_student\mahasiswa_attribute.csv'

validate_artikel_digunakanOleh(r47_file, artikel_file, mahasiswa_file)
