import pandas as pd
from sqlalchemy import create_engine

# Load CSV
df = pd.read_csv(
    "C:/Users/Modern/Downloads/ICRISAT-District Level Data - ICRISAT-District Level Data.csv",
    low_memory=False
)

# SQLAlchemy Engine
engine = create_engine("mysql+pymysql://root:@localhost/agri")

# Insert into MySQL
try:
    df.to_sql(name="crop_production", con=engine, if_exists="fail", index=False)
    print("✅ Data inserted into 'crop_production' table successfully!")
except Exception as e:
    print("❌ Failed to insert data:", e)
