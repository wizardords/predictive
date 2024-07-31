import pandas as pd
from sqlalchemy import create_engine

# Read the CSV file
csv_file = '/mnt/data/Electric_Vehicle_Population_Data_NoQuotes.csv'
df = pd.read_csv(csv_file)

# Create a SQLAlchemy engine
engine = create_engine('mysql+pymysql://username:password@localhost/ElectricVehicleData')

# Insert data into the SQL table
df.to_sql('Vehicles', con=engine, if_exists='append', index=False)
