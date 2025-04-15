from ml_project.config.configuration import ConfiguarationManager
from ml_project.components.data_ingestion import DataIngestion
from ml_project import logger



STAGE_NAME = " Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfiguarationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

