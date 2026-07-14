
from data_ingestion import load_raw_data 
from data_transformation import run_transformation_pipeline

def main():
   
  
    DATABASE_NAME = 'E:/Projects/Marketing_Campaign_Data_Analyst_Project/Database/market_data.db'
    RAW_TABLE = 'marketing_campaign'
    TRANSFORMED_TABLE = 'transformed_marketing_data'
    FINAL_CSV_EXPORT = 'marketing_dashboard_data.csv'
    
    print("========== MASTER PIPELINE STARTED ==========")
    
    try:
      
        print("Triggering Data Ingestion...")
        load_raw_data()
        
        
        
        print("Triggering Data Transformation...")
        run_transformation_pipeline(
            db_name=DATABASE_NAME, 
            input_table=RAW_TABLE, 
            output_table=TRANSFORMED_TABLE, 
            output_csv_path=FINAL_CSV_EXPORT
        )
        
        print("========== MASTER PIPELINE COMPLETED SUCCESSFULLY ==========")
        
    except Exception as e:
        print(f"========== MASTER PIPELINE TERMINATED WITH ERRORS: {e} ==========")


if __name__ == "__main__":
    main()