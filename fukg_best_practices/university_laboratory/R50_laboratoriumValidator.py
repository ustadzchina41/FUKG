import csv

def validate_laboratorium_bagianDari(r50_file, laboratorium_file, departemen_file):
    # Membaca data laboratorium dari csv laboratorium_attribute.csv
    laboratorium_data = {}
    with open(laboratorium_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_laboratorium = row[0].strip()  # Kolom namaLaboratorium
            laboratorium_data[nama_laboratorium] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari laboratorium

    # Membaca data departemen dari csv departemen_attribute.csv
    departemen_data = {}
    with open(departemen_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_departemen = row[0].strip()  # Kolom namaDepartemen
            departemen_data[nama_departemen] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari departemen

    # Validasi data di R50_Laboratorium_bagianDari.csv
    errors = []
    with open(r50_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            nama_laboratorium = row[0].strip()  # Kolom namaLaboratorium
            nama_departemen = row[1].strip()  # Kolom namaDepartemen

            # Validasi namaLaboratorium
            if nama_laboratorium not in laboratorium_data:
                errors.append(f"Data salah pada baris {line_num}: namaLaboratorium '{nama_laboratorium}' tidak ditemukan di laboratorium_attribute.csv")

            # Validasi namaDepartemen
            if nama_departemen not in departemen_data:
                errors.append(f"Data salah pada baris {line_num}: namaDepartemen '{nama_departemen}' tidak ditemukan di departemen_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r50_file} sesuai.")

# Contoh pemanggilan fungsi validate_laboratorium_bagianDari
r50_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_laboratory\R50_Laboratorium_bagianDari.csv'
laboratorium_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_laboratory\laboratorium_attribute.csv'
departemen_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\academic_department\departemen_attribute.csv'

validate_laboratorium_bagianDari(r50_file, laboratorium_file, departemen_file)
