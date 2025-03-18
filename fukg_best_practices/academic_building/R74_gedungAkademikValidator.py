import csv

def validate_gedung_akademik_bagian_dari(r74_file, gedung_file, universitas_file):
    # Membaca data gedung dari csv gedungAkademik_attribute.csv
    gedung_data = {}
    with open(gedung_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_gedung = row[0].strip()  # Kolom namaGedung
            gedung_data[nama_gedung] = row  # Simpan seluruh baris data untuk validasi lebih lanjut

    # Membaca data universitas dari csv universitas_attribute.csv
    universitas_data = {}
    with open(universitas_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_universitas = row[0].strip()  # Kolom namaUniversitas
            universitas_data[nama_universitas] = row  # Simpan seluruh baris data untuk validasi lebih lanjut

    # Validasi data di R74_GedungAkademik_bagianDari.csv
    errors = []
    with open(r74_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            nama_gedung = row[0].strip()  # Kolom namaGedung
            nama_universitas = row[1].strip()  # Kolom namaUniversitas

            # Validasi namaGedung
            if nama_gedung not in gedung_data:
                errors.append(f"Data salah pada baris {line_num}: namaGedung '{nama_gedung}' tidak ditemukan di gedungAkademik_attribute.csv")

            # Validasi namaUniversitas
            if nama_universitas not in universitas_data:
                errors.append(f"Data salah pada baris {line_num}: namaUniversitas '{nama_universitas}' tidak ditemukan di universitas_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r74_file} sesuai.")

# Contoh pemanggilan fungsi validate_gedung_akademik_bagian_dari
r74_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\academic_building\R74_GedungAkademik_bagianDari.csv'
gedung_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\academic_building\academicBuilding_attributes.csv'
universitas_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university\universitas_attribute.csv'

validate_gedung_akademik_bagian_dari(r74_file, gedung_file, universitas_file)
