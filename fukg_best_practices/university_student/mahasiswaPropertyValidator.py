import csv
import re

def validate_csv(csv_file):
    # Definisikan path lengkap ke file CSV
    csv_path = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_student\mahasiswa_attribute.csv'
    
    # Membuka file CSV
    with open(csv_path, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        
        # List untuk menyimpan pesan kesalahan
        errors = []
        
        # Definisikan opsi yang valid
        valid_program_studi = ['Teknik Informatika', 'Teknik Pertambangan', 'Teknik Mesin', 'Teknik Elektro']
        
        # Lewati baris pertama (judul kolom)
        next(csvreader, None)
        
        # Iterasi setiap baris data dalam CSV mulai dari baris kedua
        for line_num, row in enumerate(csvreader, start=2):
            if len(row) != 8:
                errors.append(f"Jumlah kolom tidak sesuai pada baris {line_num}")
                continue
            
            # Memeriksa kolom nama
            nama = row[0].strip()
            if not nama.isupper() or '.' in nama:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Nama harus huruf besar semua tanpa titik dan gelar")
            
            # Memeriksa kolom jenis kelamin
            jenis_kelamin = row[1].strip()
            if jenis_kelamin not in ['Laki-laki', 'Perempuan']:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Jenis kelamin harus 'Laki-laki' atau 'Perempuan'")
            
            # Memeriksa kolom program studi
            program_studi = row[2].strip()
            if program_studi not in valid_program_studi:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Program studi harus salah satu dari: {', '.join(valid_program_studi)}")
            
            # Memeriksa kolom jenjang
            jenjang = row[3].strip()
            if jenjang not in ['S1', 'S2', 'S3']:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Jenjang harus 'S1', 'S2', atau 'S3'")
            
            # Memeriksa kolom nomor induk mahasiswa (NIM)
            nim = row[4].strip()
            if not re.match(r'^[A-Z]\d{9}$', nim):
                errors.append(f"Data salah pada baris {line_num}, informasi error: NIM harus diawali dengan huruf besar dan terdiri dari 9 angka")
            
            # Memeriksa kolom semester awal
            semester_awal = row[5].strip()
            try:
                tahun = int(semester_awal.split()[-1])
                jenis = semester_awal.split()[0].capitalize()
                if tahun < 2000 or tahun > 3000 or jenis not in ['Genap', 'Ganjil']:
                    errors.append(f"Data salah pada baris {line_num}, informasi error: Format semester awal harus 'Genap/Ganjil tahun'")
            except ValueError:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Format semester awal tidak valid")
            
            # Memeriksa kolom status awal mahasiswa
            status_awal = row[6].strip()
            if status_awal not in ['Peserta didik baru', 'Peserta didik mutasi']:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Status awal mahasiswa harus 'Peserta didik baru' atau 'Peserta didik mutasi'")
            
            # Memeriksa kolom status mahasiswa saat ini
            status_saat_ini = row[7].strip()
            if status_saat_ini not in ['Aktif', 'Cuti', 'DO']:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Status mahasiswa saat ini harus 'Aktif', 'Cuti', atau 'DO'")
        
        # Cetak hanya kolom yang tidak memenuhi syarat
        if errors:
            for error in errors:
                print(error)
        else:
            print("Validasi sukses! Data siap dipetakan.")

# Panggil fungsi validate_csv dengan nama file CSV yang sesuai
validate_csv('mahasiswa_attribute.csv')
