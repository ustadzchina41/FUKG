import csv
import re

def validate_dosen_csv(csv_file):
    # Definisikan path lengkap ke file CSV
    csv_path = csv_file
    
    # Membuka file CSV
    with open(csv_path, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        
        # List untuk menyimpan pesan kesalahan
        errors = []
        
        # Definisikan opsi yang valid
        valid_program_studi = ['Teknik Informatika', 'Teknik Pertambangan', 'Teknik Mesin', 'Teknik Elektro']
        valid_jabatan_fungsional = ['Asisten Ahli', 'Lektor', 'Lektor Kepala', 'Profesor']
        valid_pendidikan_tertinggi = ['S2', 'S3']
        valid_status_ikatan_kerja = ['Dosen Tetap', 'Dosen Tidak Tetap', 'Dosen Honorer']
        valid_status_aktivitas = ['Aktif', 'Almarhum', 'Tugas Belajar', 'Ijin Belajar', 'Keluar']
        
        # Lewati baris pertama (judul kolom)
        next(csvreader, None)
        
        # Iterasi setiap baris data dalam CSV mulai dari baris kedua
        for line_num, row in enumerate(csvreader, start=2):
            if len(row) != 8:
                errors.append(f"Jumlah kolom tidak sesuai pada baris {line_num}")
                continue
            
            # Memeriksa kolom NIDN
            nidn = row[0].strip()
            if not re.match(r'^\d{10}$', nidn):
                errors.append(f"Data salah pada baris {line_num}, informasi error: NIDN harus terdiri dari 10 angka")
            
            # Memeriksa kolom nama
            nama = row[1].strip()
            if not nama.isupper() or '.' in nama:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Nama harus huruf besar semua tanpa titik dan gelar")
            
            # Memeriksa kolom program studi
            program_studi = row[2].strip()
            if program_studi not in valid_program_studi:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Program studi harus salah satu dari: {', '.join(valid_program_studi)}")
            
            # Memeriksa kolom jenis kelamin
            jenis_kelamin = row[3].strip()
            if jenis_kelamin not in ['Laki-laki', 'Perempuan']:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Jenis kelamin harus 'Laki-laki' atau 'Perempuan'")
            
            # Memeriksa kolom jabatan fungsional
            jabatan_fungsional = row[4].strip()
            if jabatan_fungsional not in valid_jabatan_fungsional:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Jabatan fungsional harus salah satu dari: {', '.join(valid_jabatan_fungsional)}")
            
            # Memeriksa kolom pendidikan tertinggi
            pendidikan_tertinggi = row[5].strip()
            if pendidikan_tertinggi not in valid_pendidikan_tertinggi:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Pendidikan tertinggi harus 'S2' atau 'S3'")
            
            # Memeriksa kolom status ikatan kerja
            status_ikatan_kerja = row[6].strip()
            if status_ikatan_kerja not in valid_status_ikatan_kerja:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Status ikatan kerja harus salah satu dari: {', '.join(valid_status_ikatan_kerja)}")
            
            # Memeriksa kolom status aktivitas
            status_aktivitas = row[7].strip()
            if status_aktivitas not in valid_status_aktivitas:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Status aktivitas harus salah satu dari: {', '.join(valid_status_aktivitas)}")
        
        # Cetak hanya kolom yang tidak memenuhi syarat
        if errors:
            for error in errors:
                print(error)
        else:
            print("Validasi sukses! Data siap dipetakan.")

# Panggil fungsi validate_dosen_csv dengan nama file CSV yang sesuai
csv_path = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_lecture\dosen_attribute.csv'
validate_dosen_csv(csv_path)
