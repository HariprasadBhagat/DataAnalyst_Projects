import pandas as pd
import numpy as np
import os
from sqlalchemy import create_engine
import logging
import time


engine = create_engine("sqlite:///E:/Projects/Marketing_Campaign_Data_Analyst_Project/Database/market_data.db")

os.makedirs('Logs', exist_ok=True)

logging.basicConfig(
    filename="E:/Projects/Marketing_Campaign_Data_Analyst_Project/Logs/log_file.log",
    level=logging.DEBUG,
    filemode="a",
    format="%(asctime)s %(levelname)s %(message)s"
)



def ingest(df,table_name,engine):
  df.to_sql(table_name,con=engine,if_exists="replace",index=False)


def load_raw_data():
  start=time.time()
  logging.info("Loading raw data")
  path="E:/Projects/Marketing_Campaign_Data_Analyst_Project/Dataset"
  for files in os.listdir(path):
    if files.endswith(".xlsx"):
      df=pd.read_excel(f"{path}/{files}")

      ingest(df,files[:-5],engine)
  end=time.time()
  logging.info(f"Raw data loaded in {end-start} seconds")
  logging.info("Data Loaded Successfully")

if __name__ == '__main__':
  load_raw_data()
  
