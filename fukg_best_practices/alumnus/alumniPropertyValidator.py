import csv
import re

def validate_alumni_csv(csv_file):
    # Definisikan path lengkap ke file CSV
    csv_path = csv_file
    
    # Membuka file CSV
    with open(csv_path, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        
        # List untuk menyimpan pesan kesalahan
        errors = []
        
        # Definisikan opsi yang valid
        valid_program_studi = ['Teknik Informatika', 'Teknik Pertambangan', 'Teknik Mesin', 'Teknik Elektro']
        valid_jenjang = ['S1', 'S2', 'S3']
        valid_status_awal = ['Peserta didik baru', 'Peserta didik mutasi']
        
        # Lewati baris pertama (judul kolom)
        next(csvreader, None)
        
        # Iterasi setiap baris data dalam CSV mulai dari baris kedua
        for line_num, row in enumerate(csvreader, start=2):
            if len(row) != 8:
                errors.append(f"Jumlah kolom tidak sesuai pada baris {line_num}")
                continue
            
            # Memeriksa kolom nomorIndukMahasiswa
            nomor_induk = row[0].strip()
            if not re.match(r'^[a-zA-Z0-9]+$', nomor_induk):
                errors.append(f"Data salah pada baris {line_num}, informasi error: NIM harus terdiri dari angka atau huruf atau kombinasi keduanya")
            
            # Memeriksa kolom nama
            nama = row[1].strip()
            if not nama.isupper() or '.' in nama:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Nama harus huruf besar semua tanpa titik dan gelar")
            
            # Memeriksa kolom jenis kelamin
            jenis_kelamin = row[2].strip()
            if jenis_kelamin not in ['Laki-Laki', 'Perempuan']:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Jenis kelamin harus 'Laki-Laki' atau 'Perempuan'")
            
            # Memeriksa kolom program studi
            program_studi = row[3].strip()
            if program_studi not in valid_program_studi:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Program studi harus salah satu dari: {', '.join(valid_program_studi)}")
            
            # Memeriksa kolom jenjang
            jenjang = row[4].strip()
            if jenjang not in valid_jenjang:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Jenjang harus salah satu dari: {', '.join(valid_jenjang)}")
            
            # Memeriksa kolom semester awal
            semester_awal = row[5].strip()
            if not re.match(r'^(Genap|Ganjil)\s\d{4}$', semester_awal):
                errors.append(f"Data salah pada baris {line_num}, informasi error: Semester awal harus dalam format Genap/Ganjil tahun (contoh: Genap 2023)")
            
            # Memeriksa kolom status awal mahasiswa
            status_awal = row[6].strip()
            if status_awal not in valid_status_awal:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Status awal mahasiswa harus salah satu dari: {', '.join(valid_status_awal)}, Perhatikan huruf Kapital")
            
            # Memeriksa kolom nomorIjazah
            nomor_ijazah = row[7].strip()
            if not re.match(r'^[a-zA-Z0-9]+$', nomor_ijazah):
                errors.append(f"Data salah pada baris {line_num}, informasi error: Nomor ijazah harus terdiri dari angka atau huruf atau kombinasi keduanya")
        
        # Cetak hanya kolom yang tidak memenuhi syarat
        if errors:
            for error in errors:
                print(error)
        else:
            print("Validasi sukses! Data siap dipetakan.")

# Panggil fungsi validate_alumni_csv dengan nama file CSV yang sesuai
csv_path = r'C:\Users\RAJA\project\fukg\fukg_best_practices\alumnus\alumni_attribute.csv'
validate_alumni_csv(csv_path)
