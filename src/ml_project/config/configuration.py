from ml_project.constants import *
from ml_project.utils.common import read_yaml,create_directories
from ml_project.entity.config_entity import dataingestion_config

class ConfiguarationManager:
    def __init__(
        self,
        config_file = config_file_path,
        schema_file = schema_file_path,
        params_file = params_file_path):

        self.config = read_yaml(config_file)
        self.schema = read_yaml(schema_file)
        self.params = read_yaml(params_file)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self)->dataingestion_config:
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = dataingestion_config(
            root_dir = config.root_dir,
            source_url = config.source_url,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir
        )
        return data_ingestion_config
