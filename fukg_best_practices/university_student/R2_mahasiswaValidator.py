import csv

def validate_relations(r2_file, mahasiswa_file, program_studi_file):
    # Membaca data dari csv mahasiswa_attribute.csv
    mahasiswa_data = {}
    with open(mahasiswa_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nomor_induk = row[4].strip()  # Kolom nomorIndukMahasiswa
            mahasiswa_data[nomor_induk] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari mahasiswa

    # Membaca data dari csv programStudi_attribute.csv
    program_studi_data = {}
    with open(program_studi_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            kode_program_studi = row[1].strip()  # Kolom kodeProgramStudi
            program_studi_data[kode_program_studi] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari program studi

    # Validasi data di R2_mahasiswa_terdaftarDi.csv
    errors = []
    with open(r2_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            nomor_induk = row[0].strip()  # Kolom nomorIndukMahasiswa
            kode_program_studi = row[1].strip()  # Kolom kodeProgramStudi

            # Validasi nomorIndukMahasiswa
            if nomor_induk not in mahasiswa_data:
                errors.append(f"Data salah pada baris {line_num}: nomorIndukMahasiswa {nomor_induk} tidak ditemukan di mahasiswa_attribute.csv")

            # Validasi kodeProgramStudi
            if kode_program_studi not in program_studi_data:
                errors.append(f"Data salah pada baris {line_num}: kodeProgramStudi {kode_program_studi} tidak ditemukan di programStudi_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r2_file} sesuai.")

# Panggil fungsi validate_relations dengan nama file CSV yang sesuai
r2_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_student\R2_mahasiswa_terdaftarDi.csv'
mahasiswa_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_student\mahasiswa_attribute.csv'
program_studi_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\program_of_study\programStudi_attribute.csv'

validate_relations(r2_file, mahasiswa_file, program_studi_file)
