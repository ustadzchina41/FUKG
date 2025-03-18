import csv
import re

def validate_staf_administratif_csv(csv_file):
    # Definisikan path lengkap ke file CSV
    csv_path = csv_file
    
    # Membuka file CSV
    with open(csv_path, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        
        # List untuk menyimpan pesan kesalahan
        errors = []
        
        # Definisikan opsi yang valid
        valid_departemen = ['Informatika', 'Elektro', 'Mesin', 'Industri']
        valid_jabatan_fungsional = ['Staf Departemen', 'Staf Fakultas', 'Staf Universitas']
        valid_pendidikan_tertinggi = ['S1', 'S2', 'S3']
        valid_status_ikatan_kerja = ['Jabatan Fungsionalitas Tertentu']
        valid_status_aktivitas = ['Aktif', 'Keluar']
        
        # Lewati baris pertama (judul kolom)
        next(csvreader, None)
        
        # Iterasi setiap baris data dalam CSV mulai dari baris kedua
        for line_num, row in enumerate(csvreader, start=2):
            if len(row) != 8:
                errors.append(f"Error! Jumlah kolom tidak sesuai pada baris {line_num}. Setiap kolom tidak boleh kosong. ")
                continue
            
            # Memeriksa kolom NIP
            nip = row[0].strip()
            if not re.match(r'^[a-zA-Z0-9]+$', nip):
                errors.append(f"Error! Format data salah pada baris {line_num}. Informasi kesalahan: NIP harus terdiri dari angka atau huruf atau kombinasi keduanya")
            
            # Memeriksa kolom nama
            nama = row[1].strip()
            if not nama.isupper() or '.' in nama:
                errors.append(f"Error! Format data salah pada baris {line_num}. Informasi kesalahan: Nama harus huruf besar semua tanpa titik dan gelar")
            
            # Memeriksa kolom departemen
            departemen = row[2].strip()
            if departemen not in valid_departemen:
                errors.append(f"Error! Format data salah pada baris {line_num}. Informasi kesalahan: Departemen harus salah satu dari: {', '.join(valid_departemen)}")
            
            # Memeriksa kolom jenis kelamin
            jenis_kelamin = row[3].strip()
            if jenis_kelamin not in ['Laki-laki', 'Perempuan']:
                errors.append(f"Error! Format data salah pada baris {line_num}. Informasi kesalahan: Jenis kelamin harus 'Laki-laki' atau 'Perempuan'")
            
            # Memeriksa kolom jabatan fungsional
            jabatan_fungsional = row[4].strip()
            if jabatan_fungsional not in valid_jabatan_fungsional:
                errors.append(f"Error! Format data salah pada baris {line_num}. Informasi kesalahan: Jabatan fungsional harus salah satu dari: {', '.join(valid_jabatan_fungsional)}")
            
            # Memeriksa kolom pendidikan tertinggi
            pendidikan_tertinggi = row[5].strip()
            if pendidikan_tertinggi not in valid_pendidikan_tertinggi:
                errors.append(f"Error! Format data salah pada baris {line_num}. Informasi kesalahan: Pendidikan tertinggi harus salah satu dari: {', '.join(valid_pendidikan_tertinggi)}")
            
            # Memeriksa kolom status ikatan kerja
            status_ikatan_kerja = row[6].strip()
            if status_ikatan_kerja not in valid_status_ikatan_kerja:
                errors.append(f"Error! Format data salah pada baris {line_num}. Informasi kesalahan: Status ikatan kerja yang tersedia hanya : {', '.join(valid_status_ikatan_kerja)} , Perhatikan penggunaan huruf Kapital di awal kata")
            
            # Memeriksa kolom status aktivitas
            status_aktivitas = row[7].strip()
            if status_aktivitas not in valid_status_aktivitas:
                errors.append(f"Error! Format data salah pada baris {line_num}. Informasi kesalahan: Status aktivitas harus salah satu dari: {', '.join(valid_status_aktivitas)}")
        
        # Cetak hanya kolom yang tidak memenuhi syarat
        if errors:
            for error in errors:
                print(error)
        else:
            print("Validasi sukses! CSV siap dipetakan.")

# Panggil fungsi validate_staf_administratif_csv dengan nama file CSV yang sesuai
csv_path = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_staff\stafAdministratif_attribute.csv'
validate_staf_administratif_csv(csv_path)
