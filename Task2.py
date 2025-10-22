import pandas as pd
import re
from datetime import datetime

# Load data
df = pd.read_csv("validation_data.csv")

# Email validation
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
    return bool(re.match(pattern, email))

# Phone validation
def is_valid_phone(phone):
    pattern = r'^\+91\d{10}$'
    return bool(re.match(pattern, phone))

# DOB validation
def is_valid_dob(dob):
    formats = ["%Y-%m-%d", "%d/%m/%Y", "%d-%m-%Y"]
    for fmt in formats:
        try:
            datetime.strptime(dob, fmt)
            return True
        except ValueError:
            continue
    return False

# creating list for storing data
valid_rows = []
invalid_rows = []

# Loop through each row
for index, row in df.iterrows():
    email = row['email']
    phone = row['phone_number']
    dob = row['date_of_birth']

    # Validate fields
    email_valid = is_valid_email(email)
    phone_valid = is_valid_phone(phone)
    dob_valid = is_valid_dob(dob)

    if email_valid and phone_valid and dob_valid:
        valid_rows.append(row)
    else:
        invalid_rows.append(row)
        if not email_valid:
            print("Invalid Email:", email)
        if not phone_valid:
            print("Invalid Phone:", phone)
        if not dob_valid:
            print("Invalid DOB:", dob)


clean_df = pd.DataFrame(valid_rows)  
invalid_df = pd.DataFrame(invalid_rows)  

print (clean_df)
print (invalid_df)

clean_df.to_csv("cleaned_file" ,mode="a" ,index = False )
invalid_df.to_csv("uncleaned_file" ,mode="a" ,index = False )