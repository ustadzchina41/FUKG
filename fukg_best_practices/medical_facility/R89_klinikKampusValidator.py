import csv

def validate_klinikKampus_melayani(r89_file, klinik_file, staf_file):
    # Membaca data dari csv klinikKampus_attribute.csv
    klinik_data = {}
    with open(klinik_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nama_klinik = row[0].strip()  # Kolom namaKlinik
            klinik_data[nama_klinik] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari klinik

    # Membaca data dari csv stafAdministratif_attribute.csv
    staf_data = {}
    with open(staf_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for row in csvreader:
            nip = row[0].strip()  # Kolom NIP
            staf_data[nip] = True  # Gunakan nilai boolean sederhana karena tidak perlu data lain dari staf administratif

    # Validasi data di R89_KlinikKampus_melayani.csv
    errors = []
    with open(r89_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # Lewati header
        for line_num, row in enumerate(csvreader, start=2):
            nama_klinik = row[0].strip()  # Kolom namaKlinik
            nip = row[1].strip()  # Kolom NIP

            # Validasi namaKlinik
            if nama_klinik not in klinik_data:
                errors.append(f"Data salah pada baris {line_num}: namaKlinik {nama_klinik} tidak ditemukan di klinikKampus_attribute.csv")

            # Validasi NIP
            if nip not in staf_data:
                errors.append(f"Data salah pada baris {line_num}: NIP {nip} tidak ditemukan di stafAdministratif_attribute.csv")

    # Cetak hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print(f"Validasi sukses! Semua data pada {r89_file} sesuai.")

# Contoh pemanggilan fungsi validate_klinikKampus_melayani
r89_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\medical_facility\R89_KlinikKampus_melayani.csv'
klinik_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\medical_facility\klinikKampus_attribute.csv'
staf_file = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_staff\stafAdministratif_attribute.csv'

validate_klinikKampus_melayani(r89_file, klinik_file, staf_file)
