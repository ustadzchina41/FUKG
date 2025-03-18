import csv
import re
from datetime import datetime

def validate_program_studi_csv(csv_file):
    csv_path = csv_file
    
    with open(csv_path, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        
        errors = []
        
        next(csvreader, None)
        
        for line_num, row in enumerate(csvreader, start=2):
            if len(row) != 18:
                errors.append(f"Jumlah kolom tidak sesuai pada baris {line_num}")
                continue
            
            status_program_studi = row[0].strip()
            if status_program_studi not in ["Aktif", "Tidak Aktif"]:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Status program studi harus 'Aktif' atau 'Tidak Aktif'")
            
            kode_program_studi = row[1].strip()
            if not kode_program_studi.isdigit():
                errors.append(f"Data salah pada baris {line_num}, informasi error: Kode program studi harus angka")
            
            nama_program_studi = row[2].strip()
            if not re.match(r'^[A-Z][a-z]*(\s[A-Z][a-z]*)*$', nama_program_studi):
                errors.append(f"Data salah pada baris {line_num}, informasi error: Nama program studi harus kapital setiap kata")
            
            jenjang = row[3].strip()
            if jenjang not in ["S1", "S2", "S3"]:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Jenjang harus 'S1', 'S2', atau 'S3'")
            
            akreditasi = row[4].strip()
            if akreditasi not in ["A", "B", "C", "Unggul", "Baik"]:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Akreditasi harus 'A', 'B', 'C', 'Unggul', atau 'Baik'")
            
            tanggal_berdiri = row[5].strip()
            try:
                datetime.strptime(tanggal_berdiri, '%d %B %Y')
            except ValueError:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Tanggal berdiri harus dalam format 'DD MMMM YYYY'")
            
            sk_penyelenggaraan = row[6].strip()
            if ',' in sk_penyelenggaraan:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Pembobotan nilai tidak boleh mengandung tanda koma")
            
            tanggal_sk = row[7].strip()
            try:
                datetime.strptime(tanggal_sk, '%d %B %Y')
            except ValueError:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Tanggal SK harus dalam format 'DD MMMM YYYY'")
            
            alamat_program_studi = row[8].strip()
            # No specific validation rule for alamat_program_studi
            
            kode_pos = row[9].strip()
            if not kode_pos.isdigit():
                errors.append(f"Data salah pada baris {line_num}, informasi error: Kode pos harus angka")
            
            telepon = row[10].strip()
            if not telepon.isdigit():
                errors.append(f"Data salah pada baris {line_num}, informasi error: Telepon harus angka")
            
            faximile = row[11].strip()
            # No specific validation rule for faximile
            
            email = row[12].strip()
            if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
                errors.append(f"Data salah pada baris {line_num}, informasi error: Email harus dalam format yang valid")
            
            website = row[13].strip()
            
            deskripsi = row[14].strip()
            # No specific validation rule for deskripsi
            
            visi = row[15].strip()
            # No specific validation rule for visi
            
            misi = row[16].strip()
            # No specific validation rule for misi
            
            kompetensi_program_studi = row[17].strip()
            # No specific validation rule for kompetensi_program_studi
        
        if errors:
            for error in errors:
                print(error)
        else:
            print("Validasi sukses! Data siap dipetakan.")

# Panggil fungsi validate_program_studi_csv dengan nama file CSV yang sesuai
csv_path = r'C:\Users\RAJA\project\fukg\fukg_best_practices\program_of_study\programStudi_attribute.csv'
validate_program_studi_csv(csv_path)
