import csv

def validate_kurikulum_terdiriDari(r35_file, kurikulum_file, mataKuliah_file):
    # Membaca data dari csv kurikulum_attribute.csv
    kurikulum_data = {}
    with open(kurikulum_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_kurikulum = row[0].strip()  # Kolom namaKurikulum
            tahun_ajaran_kurikulum = row[1].strip()  # Kolom tahunAjaranKurikulum
            kurikulum_data[(nama_kurikulum, tahun_ajaran_kurikulum)] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari kurikulum

    # Membaca data dari csv mataKuliah_attribute.csv
    mataKuliah_data = {}
    with open(mataKuliah_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            kode_mata_kuliah = row[0].strip()  # Kolom kodeMataKuliah
            mataKuliah_data[kode_mata_kuliah] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari mata kuliah

    # Validasi data di R35_Kurikulum_terdiriDari.csv
    errors = []
    with open(r35_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            tahun_ajaran_kurikulum = row[0].strip()  # Kolom tahunAjaranKurikulum
            kode_mata_kuliah = row[1].strip()  # Kolom kodeMataKuliah

            # Validasi kombinasi tahunAjaranKurikulum dan kodeMataKuliah
            if (nama_kurikulum, tahun_ajaran_kurikulum) not in kurikulum_data:
                errors.append(f"Data salah pada baris {line_num}: Tahun ajaran kurikulum {tahun_ajaran_kurikulum} tidak ditemukan di kurikulum_attribute.csv")

            # Validasi kodeMataKuliah
            if kode_mata_kuliah not in mataKuliah_data:
                errors.append(f"Data salah pada baris {line_num}: Kode mata kuliah {kode_mata_kuliah} tidak ditemukan di mataKuliah_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r35_file} sesuai.")

# Contoh pemanggilan fungsi validate_kurikulum_terdiriDari
r35_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_curriculum\R35_Kurikulum_terdiriDari.csv'
kurikulum_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_curriculum\kurikulum_attribute.csv'
mataKuliah_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_course\mataKuliah_attribute.csv'

validate_kurikulum_terdiriDari(r35_file, kurikulum_file, mataKuliah_file)
