import csv

def validate_klinikKampus_melayani(r87_file, klinik_file, mahasiswa_file):
    # Membaca data dari csv klinikKampus_attribute.csv
    klinik_data = {}
    with open(klinik_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_klinik = row[0].strip()  # Kolom namaKlinik
            klinik_data[nama_klinik] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari klinik

    # Membaca data dari csv mahasiswa_attribute.csv
    mahasiswa_data = {}
    with open(mahasiswa_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nomor_induk_mahasiswa = row[4].strip()  # Kolom nomorIndukMahasiswa
            mahasiswa_data[nomor_induk_mahasiswa] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari mahasiswa

    # Validasi data di R87_KlinikKampus_melayani.csv
    errors = []
    with open(r87_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            nama_klinik = row[0].strip()  # Kolom namaKlinik
            nomor_induk_mahasiswa = row[1].strip()  # Kolom nomorIndukMahasiswa

            # Validasi namaKlinik
            if nama_klinik not in klinik_data:
                errors.append(f"Data salah pada baris {line_num}: namaKlinik {nama_klinik} tidak ditemukan di klinikKampus_attribute.csv")

            # Validasi nomorIndukMahasiswa
            if nomor_induk_mahasiswa not in mahasiswa_data:
                errors.append(f"Data salah pada baris {line_num}: nomorIndukMahasiswa {nomor_induk_mahasiswa} tidak ditemukan di mahasiswa_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r87_file} sesuai.")

# Contoh pemanggilan fungsi validate_klinikKampus_melayani
r87_file = r'C:\Users\RAJA\project\fukg\medical_facility\R87_KlinikKampus_melayani.csv'
klinik_file = r'C:\Users\RAJA\project\fukg\medical_facility\klinikKampus_attribute.csv'
mahasiswa_file = r'C:\Users\RAJA\project\fukg\university_student\mahasiswa_attribute.csv'

validate_klinikKampus_melayani(r87_file, klinik_file, mahasiswa_file)