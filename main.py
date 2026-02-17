from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.logger import logging

if __name__ == "__main__":
    # Step 1: Data Ingestion
    logging.info("Starting Data Ingestion...")
    data_ingestion = DataIngestion()
    train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
    logging.info(f"Data Ingestion completed!")
    logging.info(f"Train data: {train_data_path}")
    logging.info(f"Test data: {test_data_path}")
    
    # Step 2: Data Transformation
    logging.info("Starting Data Transformation...")
    data_transformation = DataTransformation()
    train_arr, test_arr, preprocessor_path = data_transformation.initiate_data_transformation(
        train_data_path, 
        test_data_path
    )
    logging.info(f"Data Transformation completed!")
    logging.info(f"Preprocessor saved at: {preprocessor_path}")
    
    # Step 3: Model Training (to be implemented)
    logging.info("Data pipeline executed successfully!")
