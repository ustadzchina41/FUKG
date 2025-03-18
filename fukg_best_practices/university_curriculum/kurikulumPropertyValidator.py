import csv
import re

def validate_kurikulum_csv(csv_file):
    # Membuka file CSV
    with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        
        # List untuk menyimpan pesan kesalahan
        errors = []
        
        # Lewati baris pertama (judul kolom)
        next(csvreader, None)
        
        # Daftar program studi yang valid
        valid_program_studi = ['Teknik Informatika', 'Teknik Mesin', 'Teknik Elektro']
        
        # Iterasi setiap baris data dalam CSV mulai dari baris kedua
        for line_num, row in enumerate(csvreader, start=2):
            if len(row) != 6:
                errors.append(f"Jumlah kolom tidak sesuai pada baris {line_num}")
                continue
            
            # Memeriksa kolom namaKurikulum
            nama_kurikulum = row[0].strip()
            if not re.match(r'^Kurikulum\s+\d{4}$', nama_kurikulum):
                errors.append(f"Data salah pada baris {line_num}, informasi error: Nama kurikulum harus diawali dengan 'Kurikulum' dan diikuti dengan tahun (misalnya 'Kurikulum 2019')")
            
            # Memeriksa kolom tahunAjaranKurikulum
            tahun_ajaran_kurikulum = row[1].strip()
            if not re.match(r'^\d{4}/\d{4}$', tahun_ajaran_kurikulum):
                errors.append(f"Data salah pada baris {line_num}, informasi error: Tahun ajaran kurikulum harus dalam format tahun/tahun (misalnya 2022/2023)")
            
            # Memeriksa kolom deskripsiKurikulum
            deskripsi_kurikulum = row[2].strip()
            if ',' in deskripsi_kurikulum:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Deskripsi kurikulum tidak boleh mengandung koma")
            if len(deskripsi_kurikulum.split()) > 40:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Deskripsi kurikulum harus maksimal 40 kata")
            
            # Memeriksa kolom jumlahMataKuliahKurikulum
            jumlah_mata_kuliah = row[3].strip()
            if not jumlah_mata_kuliah.isdigit():
                errors.append(f"Data salah pada baris {line_num}, informasi error: Jumlah mata kuliah kurikulum harus angka")
            
            # Memeriksa kolom programStudi
            program_studi = row[4].strip()
            if program_studi not in valid_program_studi:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Program studi tidak valid. Harus salah satu dari: {', '.join(valid_program_studi)}")
            
            # Memeriksa kolom updateTerakhirKurikulum
            update_terakhir_kurikulum = row[5].strip()
            if not update_terakhir_kurikulum.isdigit():
                errors.append(f"Data salah pada baris {line_num}, informasi error: Update terakhir kurikulum harus angka")
        
        # Cetak hanya kolom yang tidak memenuhi syarat
        if errors:
            for error in errors:
                print(error)
        else:
            print("Validasi sukses! Data siap dipetakan.")

# Panggil fungsi validate_kurikulum_csv dengan nama file CSV yang sesuai
csv_path = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_curriculum\kurikulum_attribute.csv'
validate_kurikulum_csv(csv_path)
