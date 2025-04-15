from ml_project.config.configuration import ConfiguarationManager
from ml_project.components.data_validation import DataValiadtion
from ml_project import logger



STAGE_NAME = " Data Ingestion Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfiguarationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.validate_all_columns()
