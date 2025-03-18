import csv

def validate_gedung_akademik_tempat_kegiatan(r75_file, gedung_file, matakuliah_file):
    # Membaca data gedung dari csv gedungAkademik_attribute.csv
    gedung_data = set()
    with open(gedung_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_gedung = row[0].strip()  # Kolom namaGedung
            gedung_data.add(nama_gedung)  # Menyimpan nama gedung

    # Membaca data mata kuliah dari csv mataKuliah_attribute.csv
    matakuliah_data = set()
    with open(matakuliah_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            kode_mata_kuliah = row[0].strip()  # Kolom kodeMataKuliah
            matakuliah_data.add(kode_mata_kuliah)  # Menyimpan kode mata kuliah

    # Validasi data di R75_GedungAkademik_tempatKegiatan.csv
    errors = []
    with open(r75_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            nama_gedung = row[0].strip()  # Kolom namaGedung
            kode_mata_kuliah = row[1].strip()  # Kolom kodeMataKuliah

            # Validasi namaGedung
            if nama_gedung not in gedung_data:
                errors.append(f"Data salah pada baris {line_num}: namaGedung '{nama_gedung}' tidak ditemukan di gedungAkademik_attribute.csv")

            # Validasi kodeMataKuliah
            if kode_mata_kuliah not in matakuliah_data:
                errors.append(f"Data salah pada baris {line_num}: kodeMataKuliah '{kode_mata_kuliah}' tidak ditemukan di mataKuliah_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r75_file} sesuai.")

# Contoh pemanggilan fungsi validate_gedung_akademik_tempat_kegiatan
r75_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\academic_building\R75_GedungAkademik_tempatKegiatan.csv'
gedung_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\academic_building\academicBuilding_attributes.csv'
matakuliah_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_course\mataKuliah_attribute.csv'

validate_gedung_akademik_tempat_kegiatan(r75_file, gedung_file, matakuliah_file)
