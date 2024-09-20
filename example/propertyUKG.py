import pandas as pd

# Load the CSV file
file_path = r'C:\Users\RAJA\project\fukg\propsubclass\1_8_listProperty.csv'
csv_data = pd.read_csv(file_path)

# Define domain mappings
domain_mapping = {
    range(1, 9): 'http://example.com/fukg/SubClass/Mahasiswa',
    range(9, 17): 'http://example.com/fukg/SubClass/Dosen',
    range(17, 25): 'http://example.com/fukg/SubClass/Staff',
    range(25, 33): 'http://example.com/fukg/SubClass/Alumni',
    range(33, 38): 'http://example.com/fukg/SubClass/Universitas',
    range(38, 43): 'http://example.com/fukg/SubClass/Fakultas',
    range(43, 48): 'http://example.com/fukg/SubClass/Departemen',
    range(48, 53): 'http://example.com/fukg/SubClass/Organisasi',
    range(53, 66): 'http://example.com/fukg/SubClass/MataKuliah',
    range(66, 84): 'http://example.com/fukg/SubClass/ProgramStudi',
    range(84, 90): 'http://example.com/fukg/SubClass/Kurikulum',
    range(90, 95): 'http://example.com/fukg/SubClass/Penelitian',
    range(95, 100): 'http://example.com/fukg/SubClass/Publikasi',
    range(100, 105): 'http://example.com/fukg/SubClass/Buku',
    range(105, 110): 'http://example.com/fukg/SubClass/Artikel',
    range(110, 115): 'http://example.com/fukg/SubClass/Jurnal',
    range(115, 120): 'http://example.com/fukg/SubClass/Laboratorium',
    range(120, 125): 'http://example.com/fukg/SubClass/RuanganKelas',
    range(125, 130): 'http://example.com/fukg/SubClass/Perpustakaan',
    range(130, 135): 'http://example.com/fukg/SubClass/Seminar',
    range(135, 140): 'http://example.com/fukg/SubClass/Workshop',
    range(140, 145): 'http://example.com/fukg/SubClass/Konferensi',
    range(145, 150): 'http://example.com/fukg/SubClass/KegiatanEkstrakurikuler',
    range(150, 155): 'http://example.com/fukg/SubClass/Wisuda',
    range(155, 160): 'http://example.com/fukg/SubClass/Gedung',
    range(160, 165): 'http://example.com/fukg/SubClass/SaranaOlahraga',
    range(165, 170): 'http://example.com/fukg/SubClass/Asrama',
    range(170, 175): 'http://example.com/fukg/SubClass/Kafetaria',
    range(175, 180): 'http://example.com/fukg/SubClass/KlinikKampus'
}

# Function to map PID to domain
def get_domain(pid):
    pid_number = int(pid[1:])  # Extract the number part from PID
    for key in domain_mapping:
        if pid_number in key:
            return domain_mapping[key]
    return 'http://example.com/fukg/SubClass/Unknown'

# Function to create N-Triples definition for a property with domain and range
def create_property_ntriples(row):
    pid = row['PID']
    label_id = row['labelId']
    description_id = row['descriptionId']
    domain = get_domain(pid)
    range_ = 'http://www.w3.org/2001/XMLSchema#string'  # Default range for all properties
    
    subject = f"<http://example.com/fukg/data/Property:{pid.replace(' ', '')}>"
    predicate_a = "<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>"
    object_a = "<http://www.w3.org/1999/02/22-rdf-syntax-ns#Property>"
    predicate_label = "<http://www.w3.org/2000/01/rdf-schema#label>"
    object_label = f"\"{label_id}\""
    predicate_comment = "<http://www.w3.org/2000/01/rdf-schema#comment>"
    object_comment = f"\"{description_id}\""
    predicate_domain = "<http://www.w3.org/2000/01/rdf-schema#domain>"
    object_domain = f"<{domain}>"
    predicate_range = "<http://www.w3.org/2000/01/rdf-schema#range>"
    object_range = f"<{range_}>"

    ntriples = f"""
{subject} {predicate_a} {object_a} .
{subject} {predicate_label} {object_label} .
{subject} {predicate_comment} {object_comment} .
{subject} {predicate_domain} {object_domain} .
{subject} {predicate_range} {object_range} .
"""
    return ntriples.strip()  # Remove leading and trailing whitespace

# Generate N-Triples definitions for all properties with domain and range
ntriples_definitions = "\n".join(csv_data.apply(create_property_ntriples, axis=1))

# Output the generated N-Triples definitions
output_path = r'C:\Users\RAJA\Documents\TugasAkhir\Tools2\FUKG\PROPERTY\property_definitions.nt'
with open(output_path, 'w') as file:
    file.write(ntriples_definitions)
