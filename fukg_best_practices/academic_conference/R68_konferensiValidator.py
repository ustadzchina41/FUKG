import csv

def validate_konferensi_diselenggarakanOleh(r68_file, konferensi_file, departemen_file):
    # Membaca data konferensi dari csv konferensi_attribute.csv
    konferensi_data = {}
    with open(konferensi_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_konferensi = row[0].strip()  # Kolom namaKonferensi
            konferensi_data[nama_konferensi] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari konferensi

    # Membaca data departemen dari csv departemen_attribute.csv
    departemen_data = {}
    with open(departemen_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_departemen = row[0].strip()  # Kolom namaDepartemen
            departemen_data[nama_departemen] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari departemen

    # Validasi data di R68_Konferensi_diselenggarakanOleh.csv
    errors = []
    with open(r68_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            nama_konferensi = row[0].strip()  # Kolom namaKonferensi
            nama_departemen = row[1].strip()  # Kolom namaDepartemen

            # Validasi namaKonferensi
            if nama_konferensi not in konferensi_data:
                errors.append(f"Data salah pada baris {line_num}: namaKonferensi '{nama_konferensi}' tidak ditemukan di konferensi_attribute.csv")

            # Validasi namaDepartemen
            if nama_departemen not in departemen_data:
                errors.append(f"Data salah pada baris {line_num}: namaDepartemen '{nama_departemen}' tidak ditemukan di departemen_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r68_file} sesuai.")

# Contoh pemanggilan fungsi validate_konferensi_diselenggarakanOleh
r68_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\academic_conference\R68_Konferensi_diselenggarakanOleh.csv'
konferensi_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\academic_conference\konferensi_attribute.csv'
departemen_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\academic_department\departemen_attribute.csv'

validate_konferensi_diselenggarakanOleh(r68_file, konferensi_file, departemen_file)
