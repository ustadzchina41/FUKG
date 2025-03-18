import csv
import re

def validate_mata_kuliah_csv(csv_file):
    csv_path = csv_file
    
    with open(csv_path, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        
        errors = []
        
        next(csvreader, None)
        
        for line_num, row in enumerate(csvreader, start=2):
            if len(row) != 13:
                errors.append(f"Jumlah kolom tidak sesuai pada baris {line_num}")
                continue
            
            kode_mata_kuliah = row[0].strip()
            if not re.match(r'^[A-Za-z0-9]+$', kode_mata_kuliah):
                errors.append(f"Data salah pada baris {line_num}, informasi error: Kode mata kuliah harus terdiri dari angka, huruf atau kombinasi keduanya")
            
            nama_mata_kuliah = row[1].strip()
            if not re.match(r'^[A-Z][a-z]*(\s[A-Z][a-z]*)*$', nama_mata_kuliah):
                errors.append(f"Data salah pada baris {line_num}, informasi error: Nama mata kuliah harus kapital setiap kata")
            
            sks_mata_kuliah = row[2].strip()
            if not sks_mata_kuliah.isdigit():
                errors.append(f"Data salah pada baris {line_num}, informasi error: SKS mata kuliah harus angka")
            
            dosen_pengajar = row[3].strip()
            if not dosen_pengajar.isupper():
                errors.append(f"Data salah pada baris {line_num}, informasi error: Nama Dekan harus huruf besar semua")
            if '.' in dosen_pengajar:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Nama Dekan tidak boleh mengandung titik")
            
            deskripsi_mata_kuliah = row[4].strip()
            if len(deskripsi_mata_kuliah.split()) > 40:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Deskripsi mata kuliah tidak boleh lebih dari 40 kata")
            
            capaian_pembelajaran = row[5].strip()
            if len(capaian_pembelajaran.split()) > 40:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Capaian pembelajaran tidak boleh lebih dari 40 kata")
            
            prasyarat = row[6].strip()
            if ',' in prasyarat:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Prasyarat tidak boleh mengandung tanda koma")
            
            pokok_bahasan = row[7].strip()
            if ',' in pokok_bahasan:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Pokok bahasan tidak boleh mengandung tanda koma")
            
            tugas = row[8].strip()
            if ',' in tugas:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Tugas tidak boleh mengandung tanda koma")
            
            kerangka_matakuliah = row[9].strip()
            if ',' in kerangka_matakuliah:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Kerangka matakuliah tidak boleh mengandung tanda koma")
            
            pustaka = row[10].strip()
            if not re.match(r'^[A-Za-z0-9\s]+$', pustaka):
                errors.append(f"Data salah pada baris {line_num}, informasi error: Pustaka harus terdiri dari huruf, angka, dan spasi saja")
            
            pembobotan_nilai = row[11].strip()
            if ',' in pembobotan_nilai:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Pembobotan nilai tidak boleh mengandung tanda koma")
            
            distribusi_nilai = row[12].strip()
            if ',' in distribusi_nilai:
                errors.append(f"Data salah pada baris {line_num}, informasi error: Distribusi nilai tidak boleh mengandung tanda koma")
        
        if errors:
            for error in errors:
                print(error)
        else:
            print("Validasi sukses! Data siap dipetakan.")

# Panggil fungsi validate_mata_kuliah_csv dengan nama file CSV yang sesuai
csv_path = r'C:\Users\RAJA\project\fukg\fukg_best_practices\university_course\mataKuliah_attribute.csv'
validate_mata_kuliah_csv(csv_path)
