import pandas as pd
import numpy as np
import sqlite3
import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("Logs/etl_pipeline.log"), 
        logging.StreamHandler()                  
    ]
)

def run_transformation_pipeline(db_name, input_table, output_table, output_csv_path):
    logging.info(f"Starting transformation pipeline for '{input_table}' -> '{output_table}'")
    
    try:
        logging.info("1. Extracting data from database...")
        conn = sqlite3.connect(db_name)
        
        df = pd.read_sql(f"SELECT * FROM {input_table}", conn)
        
        logging.info(f"Successfully extracted {len(df)} rows.")
        
        logging.info("2. Cleaning Data...")
    
        df['Income'] = df['Income'].fillna(df['Income'].median())
   
        df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'])
 
        initial_rows = len(df)
        df = df.drop_duplicates()
        logging.info(f"Dropped {initial_rows - len(df)} duplicate rows.")
        
        logging.info("3. Feature Engineering & Calculating KPIs...")
     
        df['Total_Purchases'] = df[['NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases']].sum(axis=1)
        
    
        product_cols = ['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']
        df['Total_Spend'] = df[product_cols].sum(axis=1)
        

        campaign_cols = ['AcceptedCmp1', 'AcceptedCmp2', 'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5']
        df['Total_Conversions'] = df[campaign_cols].sum(axis=1)
        
   
        df['Conversion_Rate'] = df['Total_Conversions'] / df[campaign_cols].sum(axis=1)
        df['Conversion_Rate'] = df['Conversion_Rate'].fillna(0)
        
   
        df['CPA'] = df['Z_CostContact'] / df['Total_Conversions']
        df['CPA'] = np.where(np.isinf(df['CPA']) | df['CPA'].isna(), 0, df['CPA'])
        

        df['ROI'] = ((df['Z_Revenue'] - df['Z_CostContact']) / df['Z_CostContact']) * 100
    

        lead_sources = ['NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases']
        df['Max_Leads_Source'] = df[lead_sources].idxmax(axis=1)
        
        
        
        logging.info(f"4. Loading {len(df)} transformed rows to database table '{output_table}'...")

        df.to_sql(output_table, conn, index=False, if_exists='replace')
        
        logging.info(f"5. Exporting data to CSV for visualization: '{output_csv_path}'...")
  
        df.to_csv(output_csv_path, index=False)
        logging.info("CSV export completed successfully.")
        
        logging.info("Pipeline execution completed successfully!")
        return df

    except Exception as e:
        
        logging.error(f"Pipeline failed due to an error: {str(e)}")
        raise
        
    finally:

        if 'conn' in locals():
            conn.close()
            logging.info("Database connection closed.")

if __name__ == "__main__":
    transformed_df = run_transformation_pipeline(
        db_name='E:/Projects/Marketing_Campaign_Data_Analyst_Project/Database/market_data.db',
        input_table='marketing_campaign',
        output_table='transformed_marketing_data',
        output_csv_path='Updated_Dataset/marketing_dashboard_data.csv' 
    )