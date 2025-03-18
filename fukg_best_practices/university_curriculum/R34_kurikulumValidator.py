import csv

def validate_kurikulum_berlakuUntuk(r34_file, kurikulum_file, programStudi_file):
    # Membaca data dari csv programStudi_attribute.csv
    programStudi_data = {}
    with open(programStudi_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            kode_program_studi = row[1].strip()  # Kolom kodeProgramStudi
            programStudi_data[kode_program_studi] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari program studi

    # Membaca data dari csv kurikulum_attribute.csv
    kurikulum_data = {}
    with open(kurikulum_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            tahun_ajaran_kurikulum = row[1].strip()  # Kolom tahunAjaranKurikulum
            kurikulum_data[tahun_ajaran_kurikulum] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari kurikulum

    # Validasi data di R34_Kurikulum_berlakuUntuk.csv
    errors = []
    with open(r34_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            tahun_ajaran_kurikulum = row[0].strip()  # Kolom tahunAjaranKurikulum
            kode_program_studi = row[1].strip()  # Kolom kodeProgramStudi

            # Validasi tahunAjaranKurikulum
            if tahun_ajaran_kurikulum not in kurikulum_data:
                errors.append(f"Data salah pada baris {line_num}: tahunAjaranKurikulum {tahun_ajaran_kurikulum} tidak ditemukan di kurikulum_attribute.csv")

            # Validasi kodeProgramStudi
            if kode_program_studi not in programStudi_data:
                errors.append(f"Data salah pada baris {line_num}: kodeProgramStudi {kode_program_studi} tidak ditemukan di programStudi_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r34_file} sesuai.")

# Contoh pemanggilan fungsi validate_kurikulum_berlakuUntuk
r34_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_curriculum\R34_Kurikulum_berlakuUntuk.csv'
kurikulum_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_curriculum\kurikulum_attribute.csv'
programStudi_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\program_of_study\programStudi_attribute.csv'

validate_kurikulum_berlakuUntuk(r34_file, kurikulum_file, programStudi_file)
