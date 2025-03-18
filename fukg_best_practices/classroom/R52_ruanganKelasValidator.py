import csv

def validate_ruanganKelas_terdapatDi(r52_file, ruangan_file, departemen_file):
    # Membaca data ruangan dari csv ruanganKelas_attribute.csv
    ruangan_data = {}
    with open(ruangan_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nomor_ruangan = row[0].strip()  # Kolom nomorRuangan
            ruangan_data[nomor_ruangan] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari ruangan

    # Membaca data departemen dari csv departemen_attribute.csv
    departemen_data = {}
    with open(departemen_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_departemen = row[0].strip()  # Kolom namaDepartemen
            departemen_data[nama_departemen] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari departemen

    # Validasi data di R52_RuanganKelas_terdapatDi.csv
    errors = []
    with open(r52_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            nomor_ruangan = row[0].strip()  # Kolom nomorRuangan
            nama_departemen = row[1].strip()  # Kolom namaDepartemen

            # Validasi nomorRuangan
            if nomor_ruangan not in ruangan_data:
                errors.append(f"Data salah pada baris {line_num}: nomorRuangan '{nomor_ruangan}' tidak ditemukan di ruanganKelas_attribute.csv")

            # Validasi namaDepartemen
            if nama_departemen not in departemen_data:
                errors.append(f"Data salah pada baris {line_num}: namaDepartemen '{nama_departemen}' tidak ditemukan di departemen_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r52_file} sesuai.")

# Contoh pemanggilan fungsi validate_ruanganKelas_terdapatDi
r52_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\classroom\R52_RuanganKelas_terdapatDi.csv'
ruangan_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\classroom\ruanganKelas_attribute.csv'
departemen_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\academic_department\departemen_attribute.csv'

validate_ruanganKelas_terdapatDi(r52_file, ruangan_file, departemen_file)
