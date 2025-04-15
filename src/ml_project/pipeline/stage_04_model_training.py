
from ml_project.config.configuration import ConfiguarationManager
from ml_project.components.model_trainer import ModelTrainer
from ml_project import logger



STAGE_NAME = "Model Trainer stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfiguarationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()
