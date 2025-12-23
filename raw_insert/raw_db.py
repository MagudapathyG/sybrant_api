import pandas as pd
from sqlalchemy import create_engine, exc
import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, str(email)) is not None

try:
    df = pd.read_excel(r'D:\sybrant\raw_insert\Sample_Input.xlsx', engine='openpyxl')
    
    df.columns = ['id', 'name', 'email', 'phone', 'designation', 'department']
    
    df['phone'] = df['phone'].astype(str).str.strip().str.lstrip("'")
    df['phone'] = df['phone'].replace({'nan': None}).where(pd.notnull(df['phone']), None)
    
    invalid_emails = df[~df['email'].apply(is_valid_email)]
    if not invalid_emails.empty:
        print("⚠ Warning: These rows have invalid emails and will be skipped:")
        print(invalid_emails)
        df = df[df['email'].apply(is_valid_email)]
    
    DATABASE_URL = 'mysql+pymysql://root:root@localhost/sybrant'
    engine = create_engine(DATABASE_URL)
    
    df.to_sql('person_profiles', engine, if_exists='append', index=False)
    
    print(f"✅ Successfully inserted {len(df)} records into the database.")
    
except FileNotFoundError:
    print("❌ Error: Excel file not found. Check the path.")
except exc.IntegrityError as e:
    print("❌ Database Integrity Error: Possible duplicate primary key or unique constraint violation.")
    print(e)
except exc.DataError as e:
    print("❌ Data Error: Check data types for each column.")
    print(e)
except Exception as e:
    print("❌ An unexpected error occurred:")
    print(e)
