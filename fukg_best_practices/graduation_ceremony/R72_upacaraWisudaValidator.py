import csv
from datetime import datetime

def validate_wisuda_diikuti_oleh(r72_file, wisuda_file, alumni_file):
    # Membaca data upacara wisuda dari csv upacaraWisuda_attribute.csv
    wisuda_data = {}
    with open(wisuda_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            tanggal_wisuda = datetime.strptime(row[0].strip(), '%d %B %Y').date()  # Kolom tanggalWisuda
            wisuda_data[tanggal_wisuda] = row  # Simpan seluruh baris data untuk validasi lebih lanjut

    # Membaca data alumni dari csv alumni_attribute.csv
    alumni_data = {}
    with open(alumni_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nomor_induk = row[0].strip()  # Kolom nomorIndukMahasiswa
            alumni_data[nomor_induk] = row  # Simpan seluruh baris data untuk validasi lebih lanjut

    # Validasi data di R72_UpacaraWisuda_diikutiOleh.csv
    errors = []
    with open(r72_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            tanggal_wisuda = row[0].strip()  # Kolom tanggalWisuda
            nomor_induk = row[1].strip()  # Kolom nomorIndukMahasiswa

            # Validasi tanggalWisuda
            try:
                tanggal_wisuda_dt = datetime.strptime(tanggal_wisuda, '%d %B %Y').date()
                if tanggal_wisuda_dt not in wisuda_data:
                    errors.append(f"Data salah pada baris {line_num}: tanggalWisuda '{tanggal_wisuda}' tidak ditemukan di upacaraWisuda_attribute.csv")
            except ValueError:
                errors.append(f"Data salah pada baris {line_num}: format tanggalWisuda '{tanggal_wisuda}' tidak valid")

            # Validasi nomorIndukMahasiswa
            if nomor_induk not in alumni_data:
                errors.append(f"Data salah pada baris {line_num}: nomorIndukMahasiswa '{nomor_induk}' tidak ditemukan di alumni_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r72_file} sesuai.")

# Contoh pemanggilan fungsi validate_wisuda_diikuti_oleh
r72_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\graduation_ceremony\R72_UpacaraWisuda_diikutiOleh.csv'
wisuda_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\graduation_ceremony\upacaraWisuda_attribute.csv'
alumni_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\alumnus\alumni_attribute.csv'

validate_wisuda_diikuti_oleh(r72_file, wisuda_file, alumni_file)
