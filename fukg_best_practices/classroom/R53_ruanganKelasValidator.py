import csv

def validate_ruanganKelas_terdapatDi(r53_file, ruangan_file, fakultas_file):
    # Membaca data ruangan dari csv ruanganKelas_attribute.csv
    ruangan_data = {}
    with open(ruangan_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nomor_ruangan = row[0].strip()  # Kolom nomorRuangan
            ruangan_data[nomor_ruangan] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari ruangan

    # Membaca data fakultas dari csv fakultas_attribute.csv
    fakultas_data = {}
    with open(fakultas_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_fakultas = row[0].strip()  # Kolom namaFakultas
            fakultas_data[nama_fakultas] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari fakultas

    # Validasi data di R53_RuanganKelas_terdapatDi.csv
    errors = []
    with open(r53_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            nomor_ruangan = row[0].strip()  # Kolom nomorRuanganKelas
            nama_fakultas = row[1].strip()  # Kolom namaFakultas

            # Validasi nomorRuanganKelas
            if nomor_ruangan not in ruangan_data:
                errors.append(f"Data salah pada baris {line_num}: nomorRuanganKelas '{nomor_ruangan}' tidak ditemukan di ruanganKelas_attribute.csv")

            # Validasi namaFakultas
            if nama_fakultas not in fakultas_data:
                errors.append(f"Data salah pada baris {line_num}: namaFakultas '{nama_fakultas}' tidak ditemukan di fakultas_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r53_file} sesuai.")

# Contoh pemanggilan fungsi validate_ruanganKelas_terdapatDi
r53_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\classroom\R53_RuanganKelas_terdapatDi.csv'
ruangan_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\classroom\ruanganKelas_attribute.csv'
fakultas_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\faculty\fakultas_attribute.csv'

validate_ruanganKelas_terdapatDi(r53_file, ruangan_file, fakultas_file)
