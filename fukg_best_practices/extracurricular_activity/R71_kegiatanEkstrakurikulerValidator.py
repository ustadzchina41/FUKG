import csv

def validate_kegiatan_diselenggarakan_oleh(r71_file, kegiatan_file, organisasi_file):
    # Membaca data kegiatan ekstrakurikuler dari csv kegiatanEkstrakurikuler_attribute.csv
    kegiatan_data = {}
    with open(kegiatan_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_kegiatan = row[0].strip()  # Kolom namaKegiatanEkstrakurikuler
            organisasi_penyelenggara = row[1].strip()  # Kolom organisasiPenyelenggara
            kegiatan_data[nama_kegiatan] = organisasi_penyelenggara

    # Membaca data organisasi mahasiswa dari csv organisasiMahasiswa.csv
    organisasi_data = {}
    with open(organisasi_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_organisasi = row[0].strip()  # Kolom namaOrganisasi
            organisasi_data[nama_organisasi] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari organisasi

    # Validasi data di R71_KegiatanEkstrakurikuler_diselenggarakanOleh.csv
    errors = []
    with open(r71_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            nama_kegiatan = row[0].strip()  # Kolom namaKegiatanEkstrakurikuler
            nama_organisasi = row[1].strip()  # Kolom namaOrganisasi

            # Validasi namaKegiatanEkstrakurikuler
            if nama_kegiatan not in kegiatan_data:
                errors.append(f"Data salah pada baris {line_num}: namaKegiatanEkstrakurikuler '{nama_kegiatan}' tidak ditemukan di kegiatanEkstrakurikuler_attribute.csv")
            else:
                # Validasi namaOrganisasi
                expected_organisasi = kegiatan_data[nama_kegiatan]
                if expected_organisasi != nama_organisasi:
                    errors.append(f"Data salah pada baris {line_num}: namaOrganisasi '{nama_organisasi}' tidak sesuai dengan '{expected_organisasi}' yang ada di kegiatanEkstrakurikuler_attribute.csv")

            # Validasi namaOrganisasi
            if nama_organisasi not in organisasi_data:
                errors.append(f"Data salah pada baris {line_num}: namaOrganisasi '{nama_organisasi}' tidak ditemukan di organisasiMahasiswa.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r71_file} sesuai.")

# Contoh pemanggilan fungsi validate_kegiatan_diselenggarakan_oleh
r71_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\extracurricular_activity\R71_KegiatanEkstrakurikuler_diselenggarakanOleh.csv'
kegiatan_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\extracurricular_activity\kegiatanEkstrakurikuler_attribute.csv'
organisasi_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\student_organization\organisasiMahasiswa_attribute.csv'

validate_kegiatan_diselenggarakan_oleh(r71_file, kegiatan_file, organisasi_file)
