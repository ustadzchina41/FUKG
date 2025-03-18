import csv

def validate_programStudi_terdiriDari(r33_file, programStudi_file, mataKuliah_file):
    # Membaca data dari csv programStudi_attribute.csv
    programStudi_data = {}
    with open(programStudi_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            kode_program_studi = row[1].strip()  # Kolom kodeProgramStudi
            programStudi_data[kode_program_studi] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari program studi

    # Membaca data dari csv mataKuliah_attribute.csv
    mataKuliah_data = {}
    with open(mataKuliah_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            kode_mata_kuliah = row[0].strip()  # Kolom kodeMataKuliah
            mataKuliah_data[kode_mata_kuliah] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari mata kuliah

    # Validasi data di R33_ProgramStudi_terdiriDari.csv
    errors = []
    with open(r33_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            kode_program_studi = row[0].strip()  # Kolom kodeProgramStudi
            kode_mata_kuliah = row[1].strip()  # Kolom kodeMataKuliah

            # Validasi kodeProgramStudi
            if kode_program_studi not in programStudi_data:
                errors.append(f"Data salah pada baris {line_num}: kodeProgramStudi {kode_program_studi} tidak ditemukan di programStudi_attribute.csv")

            # Validasi kodeMataKuliah
            if kode_mata_kuliah not in mataKuliah_data:
                errors.append(f"Data salah pada baris {line_num}: kodeMataKuliah {kode_mata_kuliah} tidak ditemukan di mataKuliah_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r33_file} sesuai.")

# Contoh pemanggilan fungsi validate_programStudi_terdiriDari
r33_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\program_of_study\R33_ProgramStudi_terdiriDari.csv'
programStudi_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\program_of_study\programStudi_attribute.csv'
mataKuliah_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_course\mataKuliah_attribute.csv'

validate_programStudi_terdiriDari(r33_file, programStudi_file, mataKuliah_file)
