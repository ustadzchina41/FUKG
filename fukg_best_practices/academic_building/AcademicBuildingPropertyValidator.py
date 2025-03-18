import pandas as pd

def validate_building_csv(csv_file):
    # Read the CSV file using pandas
    df = pd.read_csv(csv_file)
    
    # List to store error messages
    errors = []
    
    # Check the number of columns
    expected_columns = ['buildingName', 'location', 'yearBuilt', 'numberOfFloors', 'facilities']
    if list(df.columns) != expected_columns:
        errors.append("CSV columns do not match the expected columns.")
    
    # Iterate through each row in the DataFrame
    for index, row in df.iterrows():
        line_num = index + 2  # CSV rows start from 2 because of the header
        
        # Check the buildingName column
        building_name = row['buildingName']
        if ',' in str(building_name):
            errors.append(f"Invalid data at line {line_num}, error: Building name should not contain a comma.")
        
        # Check the location column
        location = row['location']
        if ',' in str(location):
            errors.append(f"Invalid data at line {line_num}, error: Location should not contain a comma.")
        
        # Check the yearBuilt column
        year_built = str(row['yearBuilt'])
        if not year_built.isdigit():
            errors.append(f"Invalid data at line {line_num}, error: Year built should be a number.")
        
        # Check the numberOfFloors column
        number_of_floors = str(row['numberOfFloors'])
        if not number_of_floors.isdigit():
            errors.append(f"Invalid data at line {line_num}, error: Number of floors should be a number.")
        
        # Check the facilities column
        facilities = row['facilities']
        if ',' in str(facilities):
            errors.append(f"Invalid data at line {line_num}, error: Facilities should not contain a comma.")
    
    # Print only the columns that do not meet the criteria
    if errors:
        for error in errors:
            print(error)
    else:
        print("Validation successful! Data is ready to be processed.")

# Call the validate_building_csv function with the appropriate CSV file path
csv_path = r'C:\Users\RAJA\project\fukg\fukg_best_practices\academic_building\academicBuilding_attributes.csv'
validate_building_csv(csv_path)
