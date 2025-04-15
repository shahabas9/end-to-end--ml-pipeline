from ml_project.config.configuration import ConfiguarationManager
from ml_project.components.data_transformation import DataTransformation
from ml_project import logger


STAGE_NAME = " Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfiguarationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.train_test_spliting()