import csv

def validate_ruanganKelas_digunakanUntuk(r54_file, ruangan_file, matakuliah_file):
    # Membaca data ruangan dari csv ruanganKelas_attribute.csv
    ruangan_data = {}
    with open(ruangan_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nomor_ruangan = row[0].strip()  # Kolom nomorRuangan
            ruangan_data[nomor_ruangan] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari ruangan

    # Membaca data mata kuliah dari csv mataKuliah_attribute.csv
    matakuliah_data = {}
    with open(matakuliah_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            kode_matakuliah = row[0].strip()  # Kolom kodeMataKuliah
            matakuliah_data[kode_matakuliah] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari mata kuliah

    # Validasi data di R54_RuanganKelas_digunakanUntuk.csv
    errors = []
    with open(r54_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            nomor_ruangan = row[0].strip()  # Kolom nomorRuanganKelas
            kode_matakuliah = row[1].strip()  # Kolom kodeMataKuliah

            # Validasi nomorRuanganKelas
            if nomor_ruangan not in ruangan_data:
                errors.append(f"Data salah pada baris {line_num}: nomorRuanganKelas '{nomor_ruangan}' tidak ditemukan di ruanganKelas_attribute.csv")

            # Validasi kodeMataKuliah
            if kode_matakuliah not in matakuliah_data:
                errors.append(f"Data salah pada baris {line_num}: kodeMataKuliah '{kode_matakuliah}' tidak ditemukan di mataKuliah_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r54_file} sesuai.")

# Contoh pemanggilan fungsi validate_ruanganKelas_digunakanUntuk
r54_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\classroom\R54_RuanganKelas_digunakanUntuk.csv'
ruangan_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\classroom\ruanganKelas_attribute.csv'
matakuliah_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_course\mataKuliah_attribute.csv'

validate_ruanganKelas_digunakanUntuk(r54_file, ruangan_file, matakuliah_file)
