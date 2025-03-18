import csv

def validate_klinikKampus_bagianDari(r86_file, klinik_file, universitas_file):
    # Membaca data dari csv klinikKampus_attribute.csv
    klinik_data = {}
    with open(klinik_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_klinik = row[0].strip()  # Kolom namaKlinik
            klinik_data[nama_klinik] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari klinik

    # Membaca data dari csv universitas_attribute.csv
    universitas_data = {}
    with open(universitas_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_universitas = row[0].strip()  # Kolom namaUniversitas
            universitas_data[nama_universitas] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari universitas

    # Validasi data di R86_KlinikKampus_bagianDari.csv
    errors = []
    with open(r86_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            nama_klinik = row[0].strip()  # Kolom namaKlinik
            nama_universitas = row[1].strip()  # Kolom namaUniversitas

            # Validasi namaKlinik
            if nama_klinik not in klinik_data:
                errors.append(f"Data salah pada baris {line_num}: namaKlinik {nama_klinik} tidak ditemukan di klinikKampus_attribute.csv")

            # Validasi namaUniversitas
            if nama_universitas not in universitas_data:
                errors.append(f"Data salah pada baris {line_num}: namaUniversitas {nama_universitas} tidak ditemukan di universitas_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r86_file} sesuai.")

# Contoh pemanggilan fungsi validate_klinikKampus_bagianDari
r86_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\medical_facility\R86_KlinikKampus_bagianDari.csv'
klinik_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\medical_facility\klinikKampus_attribute.csv'
universitas_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university\universitas_attribute.csv'

validate_klinikKampus_bagianDari(r86_file, klinik_file, universitas_file)
