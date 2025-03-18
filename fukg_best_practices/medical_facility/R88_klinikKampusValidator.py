import csv

def validate_klinikKampus_melayani(r88_file, klinik_file, dosen_file):
    # Membaca data dari csv klinikKampus_attribute.csv
    klinik_data = {}
    with open(klinik_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_klinik = row[0].strip()  # Kolom namaKlinik
            klinik_data[nama_klinik] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari klinik

    # Membaca data dari csv dosen_attribute.csv
    dosen_data = {}
    with open(dosen_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nidn = row[0].strip()  # Kolom NIDN
            dosen_data[nidn] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari dosen

    # Validasi data di R88_KlinikKampus_melayani.csv
    errors = []
    with open(r88_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            nama_klinik = row[0].strip()  # Kolom namaKlinik
            nidn = row[1].strip()  # Kolom NIDN

            # Validasi namaKlinik
            if nama_klinik not in klinik_data:
                errors.append(f"Data salah pada baris {line_num}: namaKlinik {nama_klinik} tidak ditemukan di klinikKampus_attribute.csv")

            # Validasi NIDN
            if nidn not in dosen_data:
                errors.append(f"Data salah pada baris {line_num}: NIDN {nidn} tidak ditemukan di dosen_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r88_file} sesuai.")

# Contoh pemanggilan fungsi validate_klinikKampus_melayani
r88_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\medical_facility\R88_KlinikKampus_melayani.csv'
klinik_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\medical_facility\klinikKampus_attribute.csv'
dosen_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_lecture\dosen_attribute.csv'

validate_klinikKampus_melayani(r88_file, klinik_file, dosen_file)
