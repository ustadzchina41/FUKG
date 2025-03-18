import csv
from datetime import datetime

def validate_upacara_wisuda_diselenggarakan_oleh(r73_file, wisuda_file, universitas_file):
    # Membaca data upacara wisuda dari csv upacaraWisuda_attribute.csv
    wisuda_data = {}
    with open(wisuda_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            tanggal_wisuda = datetime.strptime(row[0].strip(), '%d %B %Y').date()  # Kolom tanggalWisuda
            wisuda_data[tanggal_wisuda] = row  # Simpan seluruh baris data untuk validasi lebih lanjut

    # Membaca data universitas dari csv universitas_attribute.csv
    universitas_data = {}
    with open(universitas_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_universitas = row[0].strip()  # Kolom namaUniversitas
            universitas_data[nama_universitas] = row  # Simpan seluruh baris data untuk validasi lebih lanjut

    # Validasi data di R73_UpacaraWisuda_diselenggarakanOleh.csv
    errors = []
    with open(r73_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            tanggal_wisuda = row[0].strip()  # Kolom tanggalWisuda
            nama_universitas = row[1].strip()  # Kolom namaUniversitas

            # Validasi tanggalWisuda
            try:
                tanggal_wisuda_dt = datetime.strptime(tanggal_wisuda, '%d %B %Y').date()
                if tanggal_wisuda_dt not in wisuda_data:
                    errors.append(f"Data salah pada baris {line_num}: tanggalWisuda '{tanggal_wisuda}' tidak ditemukan di upacaraWisuda_attribute.csv")
            except ValueError:
                errors.append(f"Data salah pada baris {line_num}: format tanggalWisuda '{tanggal_wisuda}' tidak valid")

            # Validasi namaUniversitas
            if nama_universitas not in universitas_data:
                errors.append(f"Data salah pada baris {line_num}: namaUniversitas '{nama_universitas}' tidak ditemukan di universitas_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r73_file} sesuai.")

# Contoh pemanggilan fungsi validate_upacara_wisuda_diselenggarakan_oleh
r73_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\graduation_ceremony\R73_UpacaraWisuda_diselenggarakanOleh.csv'
wisuda_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\graduation_ceremony\upacaraWisuda_attribute.csv'
universitas_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university\universitas_attribute.csv'

validate_upacara_wisuda_diselenggarakan_oleh(r73_file, wisuda_file, universitas_file)
