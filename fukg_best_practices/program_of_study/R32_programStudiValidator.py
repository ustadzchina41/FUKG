import csv

def validate_programStudi_bagianDari(r32_file, programStudi_file, fakultas_file):
    # Membaca data dari csv programStudi_attribute.csv
    programStudi_data = {}
    with open(programStudi_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            kode_program_studi = row[1].strip()  # Kolom kodeProgramStudi
            programStudi_data[kode_program_studi] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari program studi

    # Membaca data dari csv fakultas_attribute.csv
    fakultas_data = {}
    with open(fakultas_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_fakultas = row[0].strip()  # Kolom namaFakultas
            fakultas_data[nama_fakultas] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari fakultas

    # Validasi data di R32_ProgramStudi_bagianDari.csv
    errors = []
    with open(r32_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            kode_program_studi = row[0].strip()  # Kolom kodeProgramStudi
            nama_fakultas = row[1].strip()  # Kolom namaFakultas

            # Validasi kodeProgramStudi
            if kode_program_studi not in programStudi_data:
                errors.append(f"Data salah pada baris {line_num}: kodeProgramStudi {kode_program_studi} tidak ditemukan di programStudi_attribute.csv")

            # Validasi namaFakultas
            if nama_fakultas not in fakultas_data:
                errors.append(f"Data salah pada baris {line_num}: namaFakultas {nama_fakultas} tidak ditemukan di fakultas_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r32_file} sesuai.")

# Contoh pemanggilan fungsi validate_programStudi_bagianDari
r32_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\program_of_study\R32_ProgramStudi_bagianDari.csv'
programStudi_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\program_of_study\programStudi_attribute.csv'
fakultas_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\faculty\fakultas_attribute.csv'

validate_programStudi_bagianDari(r32_file, programStudi_file, fakultas_file)
