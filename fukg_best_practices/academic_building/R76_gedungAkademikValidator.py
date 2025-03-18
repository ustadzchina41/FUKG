import csv

def validate_gedungAkademik_tempatKegiatan(r76_file, gedung_file, seminar_file):
    # Membaca data dari csv gedungAkademik_attribute.csv
    gedung_data = {}
    with open(gedung_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_gedung = row[0].strip()  # Kolom namaGedung
            gedung_data[nama_gedung] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari gedung

    # Membaca data dari csv seminar_attribute.csv
    seminar_data = {}
    with open(seminar_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            judul_seminar = row[0].strip()  # Kolom judulSeminar
            seminar_data[judul_seminar] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari seminar

    # Validasi data di R76_GedungAkademik_tempatKegiatan.csv
    errors = []
    with open(r76_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            nama_gedung = row[0].strip()  # Kolom namaGedung
            judul_seminar = row[1].strip()  # Kolom judulSeminar

            # Validasi namaGedung
            if nama_gedung not in gedung_data:
                errors.append(f"Data salah pada baris {line_num}: namaGedung {nama_gedung} tidak ditemukan di gedungAkademik_attribute.csv")

            # Validasi judulSeminar
            if judul_seminar not in seminar_data:
                errors.append(f"Data salah pada baris {line_num}: judulSeminar {judul_seminar} tidak ditemukan di seminar_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r76_file} sesuai.")

# Contoh pemanggilan fungsi validate_gedungAkademik_tempatKegiatan
r76_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\academic_building\R76_GedungAkademik_tempatKegiatan.csv'
gedung_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\academic_building\academicBuilding_attributes.csv'
seminar_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\seminar\seminar_attribute.csv'

validate_gedungAkademik_tempatKegiatan(r76_file, gedung_file, seminar_file)
